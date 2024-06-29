import ctypes
import os
from subprocess import run

def compile_cuda_kernel():
    kernel_code = """
    extern "C"
    __global__ void testKernel() {
        printf("Hello from CUDA kernel!\\n");
    }
    """
    kernel_file = 'test_kernel.cu'
    binary_file = 'test_kernel'

    with open(kernel_file, 'w') as f:
        f.write(kernel_code)
    
    result = run(['nvcc', kernel_file, '-o', binary_file])
    if result.returncode != 0:
        raise RuntimeError("CUDA kernel compilation failed")
    
    return binary_file

def run_cuda_kernel(binary_file):
    result = run(['./' + binary_file])
    if result.returncode != 0:
        raise RuntimeError("CUDA kernel execution failed")

def test_cuda_compile_run():
    binary_file = compile_cuda_kernel()
    try:
        run_cuda_kernel(binary_file)
    finally:
        os.remove(binary_file)
        os.remove('test_kernel.cu')

if __name__ == "__main__":
    test_cuda_compile_run()
