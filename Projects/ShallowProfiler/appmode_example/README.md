The shell script `make_appmode_environment.sh` will create a conda environment "appmode"
and install the `appmode` plugin in it.   I found the current conda-forge `appmode`
package does not do all of the necessary post-install steps --- the script handles that as well.

Then switch to the new environment and run a jupyter notebook:

    source activate appmode
    jupyter notebook

The notebook "example_app.ipynb" in this directory is the example from the [appmode repo](https://github.com/oschuett/appmode)
