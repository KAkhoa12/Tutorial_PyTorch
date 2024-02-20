# Cài đặt Cuda
1. Nếu như bạn nào sử dụng window thì điều đầu tiên sử dụng được pytorch thì chúng ta sẽ tải Cuda, tại trang chủ cuda [CUDA Toolkit 12.1](https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_network)
2. Sau đó chọn các thông số để tải Cuda về 
![Hình ảnh trang chủ Tải Cuda](./img/Screenshot%202024-02-20%20222916.png)


# Cài đặt Pytorch   
1. Sau khi đã cài đặt CUDA và tải về xong và quay lại trang [Pytorch Download](https://pytorch.org/get-started/locally/) như sau 
![Hình ảnh tải về Pytorch](./img/Screenshot%202024-02-20%20223456_pytorch.png)
2. Mở terminal và chạy lệnh 
```
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```