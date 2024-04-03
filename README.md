# Tiny 3DGStreamViewer
This is a fork of [3DGStreamViewer](https://github.com/SJoJoK/3DGStreamViewer) which also is a fork of [GaussianSplattingViewer](https://github.com/limacv/GaussianSplattingViewer).

It is used to dynamicaly render a stream of per frame static 3DGS as a video while still having full control of the viewpoint camera.

## Availble 3DGS from Dyn-3DGS:

TODO

## Usage
Install the dependencies:
```
pip install -r requirements.txt
```
Install [Pytorch](https://pytorch.org/) w/ CUDA

Install the [diff-gaussian-rasterization](https://github.com/graphdeco-inria/diff-gaussian-rasterization) following the guidance [here](https://github.com/graphdeco-inria/gaussian-splatting). 

Install the [tiny-cuda-nn](https://github.com/NVlabs/tiny-cuda-nn).

Install the following package:
```
pip install cuda-python
```

Launch the viewer:
```
python main.py
```
## Contributing

This project is a tiny viewer designed for simplicity and ease of use. We welcome contributions that aim to improve performance or extend functionality. If you have ideas or improvements, please feel free to submit a pull request.

## Acknowledgements
We would like to express our gratitude to the original repository [GaussianSplattingViewer](https://github.com/limacv/GaussianSplattingViewer) for providing the foundation upon which this work is built.

