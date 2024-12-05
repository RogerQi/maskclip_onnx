## System-level Prereq

If you don't have conda/miniconda, I recommend miniconda, which is a lightweight version of anaconda that has essential features.

You can get the installation [here](https://docs.anaconda.com/free/miniconda/).

Follow the instruction [here](https://stackoverflow.com/questions/76760906/installing-mamba-on-a-machine-with-conda) to set up Mamba, a fast environment solver for conda.

```bash
## prioritize 'conda-forge' channel
conda config --add channels conda-forge

## update existing packages to use 'conda-forge' channel
conda update -n base --all

## install 'mamba'
conda install -n base mamba
```

Note: technically, the mamba solver should behave the same as the default solver. However, there have been cases where dependencies
can not be properly set up with the default mamba solver. The following instructions have **only** been tested on mamba solver.

### Install Basic packages

```bash
conda create -y -n maskclip_onnx python=3.8 && conda activate maskclip_onnx
# This is the testing command I used, but any latest pytorch should be fine
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu118
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit
pip install git+https://github.com/RogerQi/maskclip_onnx
```

### Install TensorRT dependencies

If you want to accelerate model inference speed with tensorRT, you need these dependencies.

```bash
pip install tensorrt-cu11  # change cu11 to your cuda version used above
pip install pycuda
pip install onnx onnxruntime
```

### FAQ

1. If you encounter the following error:
```
ImportError: cannot import name 'packaging' from 'pkg_resources' 
```

It may be due to the version of setuptools. You can downgrade the version of setuptools by running the following command:
```
pip install setuptools==69.5.1
```