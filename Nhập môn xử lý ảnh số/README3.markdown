# README - XLA Lab 3 Image Processing Project

## Giới thiệu
Đây là một dự án Python thực hiện các kỹ thuật xử lý ảnh cơ bản và nâng cao sử dụng các thư viện như `numpy`, `scipy.ndimage`, `imageio.v2`, và `matplotlib.pyplot`. Dự án bao gồm các bài tập thực hành và một công cụ tương tác để biến đổi ảnh theo nhiều cách khác nhau.

## Yêu cầu hệ thống
- Python 3.x
- Các thư viện sau (cài đặt bằng `pip install`):
  - `numpy`
  - `scipy`
  - `imageio`
  - `matplotlib`

## Cấu trúc dự án
- File chính: `xla_lab3.py`
- Ảnh đầu vào: `fruit.jpg`, `world_cup.jpg`, `quang_ninh.jpg`, `pagoda.jpg` (cần đặt trong cùng thư mục với file Python).

## Chức năng
### 1. Xử lý cơ bản
- **Cắt ảnh**: Trích xuất vùng cụ thể từ ảnh (ví dụ: dâu tây, cam).
- **Lưu ảnh**: Lưu kết quả dưới dạng file mới (ví dụ: `strawberry.jpg`, `orange.jpg`).

### 2. Biến đổi nâng cao
- **Dịch chuyển**: Di chuyển ảnh theo các offset đã chỉ định.
- **Phóng to/Thu nhỏ**: Thay đổi kích thước ảnh với các yếu tố phóng to/thu nhỏ khác nhau.
- **Xoay**: Xoay ảnh theo góc độ tùy chọn, với hoặc không giữ nguyên kích thước.
- **Dilate nhị phân**: Mở rộng vùng trắng trong ảnh nhị phân.
- **Ánh xạ tọa độ**: Tạo hiệu ứng méo mó ngẫu nhiên.
- **Biến dạng hình học**: Áp dụng biến dạng dựa trên hàm cosin tùy chỉnh.

### 3. Công cụ tương tác
- Cho phép người dùng chọn ảnh (`fruit.jpg`, `quang_ninh.jpg`, `pagoda.jpg`).
- Hỗ trợ các phép biến đổi:
  - Tịnh tiến (dịch theo chiều ngang/chiều dọc).
  - Xoay (theo góc độ).
  - Phóng to/thu nhỏ (theo tỉ lệ).
  - Ánh xạ tọa độ (biến dạng ngẫu nhiên).
  - Đổi màu (hoán đổi kênh Red-Green hoặc Red-Blue).
- Kết quả có thể được trực quan hóa và lưu dưới dạng file `result.jpg`.

## Hướng dẫn sử dụng
1. Đặt các file ảnh (`fruit.jpg`, `world_cup.jpg`, `quang_ninh.jpg`, `pagoda.jpg`) trong cùng thư mục với `xla_lab3.py`.
2. Chạy file `xla_lab3.py` bằng lệnh:
   ```
   python xla_lab3.py
   ```
3. Theo hướng dẫn trên màn hình:
   - Chọn ảnh bằng cách nhập số (1-3).
   - Chọn phép biến đổi (T, X, P, H, C, M, Q).
   - Nhập các tham số cần thiết (ví dụ: offset, góc xoay, tỉ lệ).
   - Chọn lưu ảnh (y/n) nếu muốn.

