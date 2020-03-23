#!/bin/bash

export LD_RUN_PATH=$LD_LIBRARY_PATH

# set compiler wrapper
mpicc=$(command -v mpicc)
CC=$mpicc ./configure --with-zlib --enable-parallel --enable-shared --prefix=$PREFIX

export NPROCS=$(nproc)

make -j$NPROCS
# Sets the real amount of cores available.
# HDF5 tries to allocate 6 by default,
# which will cause an error if the build machine
# doesn't have that many
# make check
make install

# rm -rf $PREFIX/share/hdf5_examples

