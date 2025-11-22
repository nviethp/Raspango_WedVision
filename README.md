# Raspango
Source code web server dùng để cung cấp API xử lý ảnh. Sử dụng Django chạy trên nhiều hệ điều hành như Windows, Centos, Ubuntu và Raspbian để xử lý ảnh, nhận diện vật thể và trả về cho client. Đối với Raspberry Pi còn có thêm chức năng đọc tín hiệu cảm biến, xuất tín hiệu ra các chân GPIO,...


## 1. Hướng dẫn cài đặt

### Bước 1 Cài đặt thư viện
- Cài đặt Python 3.10
- Cài đặt Python package
- Cài đặt Pytorch Pytorch 2.7.0 CUDA

`pip install torch==2.7.0 torchvision==0.22.0 torchaudio==2.7.0 --index-url https://download.pytorch.org/whl/cu118`

- Cài đặt ultralytics:
`pip install ultralytics==8.2.28`

### Bước 2 Cài đặt công cụ lập trình
- Visual Studio Code
- DB Browser for SQLite

Bước 3: Clone source code Raspango
Bước 4: Cài đặt các thư viện pip bằng lệnh pip install -r requirements.txt
Bước 5: chạy file start.bat
Bước 6: mở Chrome nhập địa chỉ localhost, trang web sẽ yêu cầu nhập username và password
	Username: admin
	Password: admin
## Hướng dẫn sử dụng

### Chạy server
Trên Windows chạy start.bat, trên Linux chạy file start.sh
`sudo bash start.sh`

*Cần sudo vì server chạy port 80*

### Tài khoản đăng nhập
Username: admin
Password: admin
