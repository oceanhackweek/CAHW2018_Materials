## Getting Started
Log in at https://ooinet.oceanobservatories.org/ and obtain your username and token under your profile (top right corner). Use CILogon to log in without filling out the registration form.

## Content
`netcdf_basic_example.ipynb` -  Programatically download and work with OOI NetCDF data without leaving the notebook.

`json_basic_example.ipynb` - Request OOI data as a synchronous (instantaneous) JSON data response. Data are decimated down to 20,000 data points. This data response type is useful for building real-time data display applications.


## Local Setup Instructions

<b>For use on your local machine only.</b> You do not need to proceed if you are using the jupyterhub server.

Download anaconda or [miniconda](https://conda.io/miniconda.html), then add the conda-forge channel.

```
conda config --add channels conda-forge
```

Create a virtual environment for this exercise called ooi2.

```
$ conda create -n ooi2 python=2 ipykernel requests thredds_crawler xarray netcdf4 pandas numpy matplotlib
```


Add the `ooi2` environment to jupyter as a selectable kernel for your user.

```
$ python -m ipykernel install --user --name ooi2 --display-name "Python2 OOI"

```

Launch the local notebook server

```
$ jupyter notebook

```
