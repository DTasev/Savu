#!/bin/bash

# set compiler wrapper
mpicc=$(command -v mpicc)
mpi=${mpicc%/bin/mpicc}
# export LD_LIBRARY_PATH=$mpi:$mpi/lib:$mpi/include:$LD_LIBRARY_PATH
export LD_RUN_PATH=$LD_LIBRARY_PATH

# check anaconda distribution
# ana_path=$(command -v savu)

CC=$mpicc ./configure --with-zlib --enable-parallel --enable-shared --prefix=$PREFIX
make
# Sets the real amount of cores available.
# HDF5 tries to allocate 6 by default,
# which will cause an error if the build machine
# doesn't have that many
export NPROCS=$(nproc)
# make check
make install

# rm -rf $PREFIX/share/hdf5_examples

