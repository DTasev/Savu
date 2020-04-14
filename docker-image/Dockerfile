FROM nvidia/cuda:9.0-devel-centos7

USER root

# Deps
RUN yum groupinstall -y 'Development Tools' && yum install -y mesa-libGL-devel mesa-libGLU-devel wget boost-devel && yum clean all && rm -rf /var/cache/yum

ENV VERSION=2.4
ENV FTTW=3.3.8
ENV OPENMPI=3.1.3

# Install FTTW3
ADD http://fftw.org/fftw-${FTTW}.tar.gz /fftw-${FTTW}.tar.gz
RUN tar -xf fftw-${FTTW}.tar.gz && \
    /fftw-${FTTW}/configure --enable-threads --enable-shared --disable-static && make -j32 /fftw-${FTTW}/ && make install /fftw-${FTTW}/ && make clean /fftw-${FTTW}/ && \
    /fftw-${FTTW}/configure --enable-threads --enable-shared --enable-float --disable-static && make -j32 /fftw-${FTTW}/ && make install /fftw-${FTTW}/ && make clean /fftw-${FTTW}/ && \
    /fftw-${FTTW}/configure --enable-threads --enable-shared --enable-long-double --disable-static && make -j32 /fftw-${FTTW}/ && make install /fftw-${FTTW}/ && rm -rf /fftw*

# Download openmpi ${OPENMPI} and build it
ADD https://www.open-mpi.org/software/ompi/v3.1/downloads/openmpi-${OPENMPI}.tar.gz /openmpi-${OPENMPI}.tar.gz
RUN tar -xf openmpi-${OPENMPI}.tar.gz && \
    /openmpi-${OPENMPI}/configure --with-sge --enable-orterun-prefix-by-default --disable-static && make -j32 /openmpi-${OPENMPI}/ && make install /openmpi-${OPENMPI}/ && rm -rf /openmpi*

# Get and install Savu
COPY get-and-install-savu.sh /get-and-install-savu.sh
RUN chmod +x /get-and-install-savu.sh && \
    /get-and-install-savu.sh $VERSION && \
    /miniconda/bin/conda clean --all --yes && \
    rm -rf /tmp/*

RUN /miniconda/bin/python -m pip install gnureadline==6.3.8
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
RUN ldconfig

RUN useradd --create-home --shell /bin/bash savu

COPY savu_setup.sh /savu_setup.sh

# Source Savu setup script on Bash startup
RUN echo '. /savu_setup.sh' >> /etc/bashrc && echo '. /savu_setup.sh' >> /etc/profile

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
