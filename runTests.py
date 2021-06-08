import os
CUDA_PATH = "/usr/local/apps/cuda/cuda-10.1"
CUDA_BIN_PATH = (f"${CUDA_PATH}/bin")
CUDA_NVCC = ("${CUDA_BIN_PATH}/nvcc")
PATH = "/usr/local/apps/cuda/cuda-10.1/bin"

for np in [2, 4, 6, 8, 16, 24, 32]:
    cmd = ("mpic++ -o project7 main.cpp")

    os.system(cmd)
    cmd = (f"mpiexec -mca btl self,tcp -np {np} project7 ")
    os.system(cmd)
