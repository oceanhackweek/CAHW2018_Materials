import re
from requests.packages.urllib3.util.retry import Retry
import concurrent.futures
import time
import xarray as xr
import pickle as pk
import pandas as pd
import json
import os
import datetime
import requests
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import netCDF4 as nc

# authenticate
import netrc
netrc = netrc.netrc()
remoteHostName = "ooinet.oceanobservatories.org"
info = netrc.authenticators(remoteHostName)
username = info[0]
token = info[2]

# establish session
session = requests.session()
retry = Retry(total=10, backoff_factor=0.3,)
adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100, max_retries=retry, pool_block=True)
session.mount('https://', adapter)

# set up pool
pool = concurrent.futures.ThreadPoolExecutor(max_workers=20)

def get_array(array):
	DATA_TEAM_PORTAL_URL = 'http://ooi.visualocean.net/data-streams/science/'
	array_url = DATA_TEAM_PORTAL_URL + array
	array_df = pd.read_csv(array_url)
	array_df = array_df[['reference_designator','method', 'stream_name','parameter_name']]
	array_df = array_df.drop_duplicates()

	return array_df

def cabled_array_only():
	Cabled_CE_platforms = ['CE02SHBP', 'CE04OSBP', 'CE04OSPS']
	RS = get_array('RS')
	CE = get_array('CE')
	CE = CE[CE.reference_designator.str.contains('|'.join(Cabled_CE_platforms))==True]
	CA = pd.concat([RS, CE])

	return CA

def sp_only():
	# sp_platforms = ['RS03AXPS', "RS01SBPS", "CE04OSPS"]
	sp_platforms = ['CE04OSPS']
	CA = cabled_array_only()
	CA_sp = CA[CA.reference_designator.str.contains('|'.join(sp_platforms))==True]
	
	return CA_sp


def build_sp_requests(start_time, end_time):
	DATA_URL = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/'
	request_inputs = sp_only()
	request_inputs = request_inputs[['reference_designator','method', 'stream_name','parameter_name']]
	request_inputs = request_inputs.drop_duplicates()
	request_inputs['subsite'] = request_inputs.reference_designator.str[:8]
	request_inputs['platform'] = request_inputs.reference_designator.str[9:14]
	request_inputs['instrument'] = request_inputs.reference_designator.str[15:27]
	request_inputs['start_time'] = start_time
	request_inputs['end_time'] = end_time
	request_inputs['urls'] = DATA_URL+\
							request_inputs.subsite+\
							'/'+request_inputs.platform+\
							'/'+request_inputs.instrument+\
							'/'+request_inputs.method+\
							'/'+request_inputs.stream_name+\
							'?beginDT='+request_inputs.start_time+\
							'&endDT='+request_inputs.end_time+\
							'&limit=20000'

	return request_inputs


def request_data(url):
	auth = (username, token)
	return session.get(url,auth=auth)



	
def send_data_requests(start_time, end_time):

	request_inputs = build_sp_requests(start_time, end_time)
	request_urls = request_inputs['urls'].values.tolist()
	request_urls = request_urls[0:2]

	sp_parameter_data = pd.DataFrame()

	future_to_url = {pool.submit(request_data, url): url for url in request_urls}
	for future in concurrent.futures.as_completed(future_to_url):
		url = future_to_url[future]
		# url = future_to_url[future]
		try:
			data = future.result() 
			data = data.json()

			refdes_list = []
			parameter_list = []
			method_list = []
			stream_list = []
			timestamp_list = []
			value_list = []
			
			refdes = data[-1]['pk']['subsite'] + '-' + data[-1]['pk']['node'] + '-' + data[-1]['pk']['sensor']
			method = data[-1]['pk']['method']
			stream = data[-1]['pk']['stream']

			y = request_inputs[request_inputs['reference_designator'] == refdes]

			for i in range(len(data)):
				refdes_list.append(refdes)
				method_list.append(method)
				stream_list.append(stream)
				parameter_list.append('time')
				timestamp = data[i]['time']
				value_list.append(timestamp)
				timestamp = nc.num2date(timestamp,'seconds since 1900-01-01').replace(microsecond=0)
				timestamp_list.append(timestamp)

				for var in y.parameter_name.values:
					for j in data[i].keys():
						if var == j:
							z = data[i][j]
							
							if type(z) != list:
								refdes_list.append(refdes)
								method_list.append(method)
								stream_list.append(stream)
								parameter_list.append(var)
								value_list.append(z)
								timestamp_list.append(timestamp)
							else:
								pass
								## conditional to handle 2d datasets seperately
								# refdes_list.append(refdes)
								# method_list.append(method)
								# stream_list.append(stream)
								# parameter_list.append(var)
								# value_list.append(u)
								# timestamp_list.append(timestamp)

			# create data frame from lists collected above
			data_dict = {
				'refdes':refdes_list,
				'method':method_list,
				'stream':stream_list,
				'parameter':parameter_list,
				'value':value_list,
				'time':timestamp_list}
			response_data = pd.DataFrame(data_dict, columns = ['refdes','method','stream','parameter','value','time'])
				
		except:
			pass

		sp_parameter_data = sp_parameter_data.append(response_data)

		with open('out.pk', 'wb') as fh:
			pk.dump(sp_parameter_data ,fh)

	return sp_parameter_data