import numpy as np
import tinycudann as tcnn
import torch
import json
import os
from NTC import NeuralTransformationCache
from renderer_cuda import GaussianDataCUDA, gaus_cuda_from_cpu
from util_gau import load_ply

def load_NTCs(FVV_path, gau_cuda:GaussianDataCUDA):
    NTC_paths=[os.path.join(FVV_path, NTCs, f'NTC_{frame_id:06}.pth') for frame_id in range(0, 299)]
    config_path=os.path.join(FVV_path, NTCs, 'config.json')
    xyz_bound = gau_cuda
    with open(config_path) as f:
        NTC_conf = json.load(f)
    model=tcnn.NetworkWithInputEncoding(n_input_dims=3, n_output_dims=8, encoding_config=NTC_conf["encoding"], network_config=NTC_conf["network"]).to(torch.device("cuda"))
    NTCs=[NeuralTransformationCache(model,xyz_bound[0],xyz_bound[1]).load_state_dict(torch.load(path)) for path in NTC_paths]
    return NTCs

def load_Additions(FVV_path):
    addition_paths=[os.path.join(FVV_path, 'additional_3dgs', f'additions_{frame_id:06}.ply') for frame_id in range(0, 299)]
    additions_gaus=[load_ply(path) for path in addition_paths]
    additions_gaus_cuda=[gaus_cuda_from_cpu(gaus) for gaus in additions_gaus]
    return additions_gaus_cuda