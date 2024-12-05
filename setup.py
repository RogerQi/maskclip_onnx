from setuptools import find_packages, setup

setup(
    name="maskclip_onnx",
    version="1.0",
    install_requires=["torch", "jupyter", "ipython", "matplotlib", "tqdm", "ftfy", "regex", "Pillow"],
    include_package_data=True,
    package_data={'maskclip_onnx': ['bpe_simple_vocab_16e6.txt.gz']},
    packages=find_packages(exclude="notebooks"),
    extras_require={
        "all": ["pycocotools", "opencv-python", "onnx", "onnxruntime"],
        "dev": ["flake8", "isort", "black", "mypy"],
    },
)
