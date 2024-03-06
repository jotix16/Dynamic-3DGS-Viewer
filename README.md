# Tiny 3DGStreamViewer
This is a fork of [GaussianSplattingViewer](https://github.com/limacv/GaussianSplattingViewer), as a simple 3DGStreamViewer built with PyOpenGL / CUDARasterizer.

Note this is not the renderer we used to evaluate the render performance of [3DGStream](https://github.com/SJoJoK/3DGStream) in our paper "3DGStream: On-the-Fly Training of 3D Gaussians for Efficient Streaming of Photo-Realistic Free-Viewpoint Videos", but is still efficient enough for real-time rendering.

# Usage
Install the dependencies:
```
pip install -r requirements.txt
```

Launch the viewer:
```
python main.py
```

You can check how to use UI in the "help" panel.

The Gaussian file loader is compatiable with the official implementation. 
Therefore, download pretrained Gaussian PLY file from [this official link](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/datasets/pretrained/models.zip), and select the "point_cloud.ply" you like by clicking the 'open ply' button, and you are all set!

## To view Free-Viewpoint Videos of 3DGStream

We are actively working on this and anticipate uploading test cases within the next few hours/days, at which point we will also provide detailed usage instructions.

# Optional dependencies:

- If you want to use `cuda` backend for rendering, please install the [diff-gaussian-rasterization](https://github.com/graphdeco-inria/diff-gaussian-rasterization) following the guidance [here](https://github.com/graphdeco-inria/gaussian-splatting). And also install the following package:
```
pip install cuda-python
```

- For sorting, we provide three backend: `torch`, `cupy`, and `cpu`. The implementation will choose the first available one based on this priority order: `torch -> cupy -> cpu`. If you have `torch` or `cupy` backend, turning on `auto sort` will achieve nearly real-time sorting.
    - If you want to use `torch` as sorting backend, install any version of [PyTorch](https://pytorch.org/get-started/locally/).

    - If you want to use `cupy` to accelerate sorting, you should install the following package:
    ```
    pip install cupy-cuda11x // for cuda 11
    pip install cupy-cuda12x // for cuda 12
    ```
