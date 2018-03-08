#!/usr/bin/env sh

conda create --yes -n appmode python=3 jupyter

source activate appmode &&
  conda install --yes --channel conda-forge appmode ipywidgets &&
  jupyter nbextension     enable --py --sys-prefix widgetsnbextension &&
  jupyter nbextension     enable --py --sys-prefix appmode &&
  jupyter serverextension enable --py --sys-prefix appmode

echo "Now \"source activate appmode\" to activate the conda environment"
