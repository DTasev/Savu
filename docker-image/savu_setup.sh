#!bin/bash
export PATH=/usr/local/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export PYTHONUSERSITE True
source /usr/local/miniconda/bin/activate /usr/local/miniconda
# export PATH=/miniconda/bin:$PATH
# export LD_LIBRARY_PATH=/miniconda/bin/lib:$LD_LIBRARY_PATH
# export LD_LIBRARY_PATH=/miniconda/lib/python2.7/site-packages/astra/lib:$LD_LIBRARY_PATH
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
export FFTWDIR=/usr/local
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH