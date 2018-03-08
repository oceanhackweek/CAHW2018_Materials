
import os
import pandas as pd

## convert time range to days
from datetime import timedelta, date

__CSV_PATH__ = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

valid_platforms = ['PC01A', 'PC01B', 'PC03A', 'SC01A', 'SC01B', 'SC03A']


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)+1):
        yield start_date + timedelta(n)

def is_science_pod( platform):
    return platform[0] == 'S'


def csv_path():
    return __CSV_PATH__


def make_csv_filename( platform, day ):
    if is_science_pod(platform):
        return "sp_log_%s_%s.csv" % (platform.lower(), day.strftime("%Y%m%d"))
    else:
        return "%s_ahrsdata_%s.csv" % (platform.lower(), day.strftime("%Y%m%d"))


def make_csv_path( platform, day ):
    return os.path.join( csv_path(),
                        day.strftime("%Y-%m-%d"),
                        make_csv_filename(platform,day) )

def load_sp_eng_data(platform, start_time, end_time, source='csv' ):
    platform = platform.upper()

    if not platform in valid_platforms:
        raise RuntimeError("Sorry, can't handle platform %s" % platform)

    if source == 'csv':
        return load_sp_eng_csv( platform, start_time, end_time )
    else:
        print("I can't do right now")
        ## Load through M2M

def load_sp_eng_csv(platform, start_time, end_time):
    data = pd.DataFrame()

    for this_day in daterange(start_time, end_time):
        this_day = pd.read_csv( make_csv_path( platform, this_day ) )

        ## Custom masssaging
        if is_science_pod( platform ):
            this_day['timestamp'] = pd.to_datetime(this_day['wtime'],unit='s')
            this_day = this_day.drop('wtime', axis='columns')

            ## Map SC data file columns to same names as PC
            this_day.rename( columns={'sax': 'Ax', 'say': 'Ay', 'saz': 'Az',
                                      'sroll': 'roll', 'spitch': 'pitch', 'syaw': 'yaw'},
                             inplace=True)
        else:
            this_day['timestamp'] = pd.to_datetime(this_day['timestamp'])

        data = data.append(this_day)

    ##TODO: subset to start_time:end_time

    return data
