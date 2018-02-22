## Getting Started
Log in at https://ooinet.oceanobservatories.org/ and obtain your username and token under your profile (top right corner). Use CILogon to log in without filling out the registration form.


## Local Setup Instructions

During the workshop you will be provided with a JupyterHub workspace on the cloud and your environment will already be set up for you. If you would like to try out these notebooks on your local machine, you can proceed with the following instructions.

Download anaconda or [miniconda](https://conda.io/miniconda.html), then add the conda-forge channel.

```
conda config --add channels conda-forge
```

Create an environment for this exercise called ooi3.

```
$ conda create -n ooi3 python=3 ipykernel requests xarray netcdf4 pandas numpy matplotlib holoviews datashader bokeh plotly
```


Add the `ooi3` environment to jupyter as a selectable kernel for your user.

```
$ python -m ipykernel install --user --name ooi3 --display-name "Python3 OOI"

```

Launch the local notebook server

```
$ jupyter notebook

```
