#FROM nvidia/cuda:11.5.1-cudnn8-runtime-ubuntu20.04
FROM nvidia/cuda:11.5.0-cudnn8-runtime-ubuntu20.04

RUN apt-get -y update && apt-get -y install --no-install-recommends procps python3 python3-dev python3-pip python-is-python3 libgomp1 ffmpeg libsm6 libxext6

RUN pip install numpy==1.21.4 scipy tifffile fire \
     dask-image "dask[distributed]" imagecodecs \
     scipy scikit-image cupy-cuda115 ome-zarr==0.4.1 trackpy shapely \
      --no-cache-dir
ENV LD_LIBRARY_PATH=/usr/local/cuda-11.5/compat/
