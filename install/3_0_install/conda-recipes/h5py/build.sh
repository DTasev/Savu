#!/bin/bash

# set compiler wrapper
mpicc=$(command -v mpicc)
mpi=${mpicc%/bin/mpicc}

# set anaconda distribution
ana_path=$(command -v savu)
ana_path=${ana_path%/bin/savu}
hdf5_version=1.10.5
hdf5_build_no=1

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ana_path/lib
export LD_RUN_PATH=$LD_LIBRARY_PATH
export CC=$mpicc

source $ana_path/bin/activate $ana_path
export PYTHONPATH=$PYTHONPATH:$ana_path/lib/python3.7/site-packages

echo Running with Python: $(which python)
$PYTHON setup.py configure --mpi --hdf5=$ana_path --hdf5-version=$hdf5_version
$PYTHON setup.py build
$PYTHON setup.py install
