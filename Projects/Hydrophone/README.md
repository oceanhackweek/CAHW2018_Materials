# cahw2018_hydrophone


[Interactive Demo Notebook](https://github.com/oceanhackweek/cahw2018_hydrophone/blob/master/notebooks/OOI_Hydrophone_BB.ipynb)

Interactive demo of streaming spectrograms and sound with ipywidgets.

### Data Access

- many files of different size
- about 2GB for 2hours around eclipse
- require concatenating and merging into one mseed stream

[Merging Notebook](https://github.com/oceanhackweek/cahw2018_hydrophone/blob/master/notebooks/OOI_mseed_merge.ipynb)

### Data processing 
- we need to efficiently calculate spectrograms of many files
- so far we calculate spectrograms sequentially and store them line by line into a csv file
- need to allow to parallelize
- need to preserve time stamps of spectrograms
- need to store into an xarray/netcdf/hdf5 -like format with time stamps and chunk


### Clustering 
- chunks of 5 secs
- dimensionality reduction with TSNE

[Spectrogram Storing & Clusteirng Notebook](https://github.com/oceanhackweek/cahw2018_hydrophone/blob/master/notebooks/spectrogram-store-cluster.ipynb)

### Advanced Visualization

#### clustering points with a thumbnail 

- static scikit learn

http://bebi103.caltech.edu.s3-website-us-east-1.amazonaws.com/2016/tutorials/aux8_tsne.html

- javascript tsne

https://github.com/scienceai/tsne-js

- D3.js tsne 

https://github.com/karpathy/tsnejs

- 3D Point Clustering with Plotly

https://plot.ly/python/3d-point-clustering/

#### Project Repo:

https://github.com/oceanhackweek/cahw2018_hydrophone

