# Tài liệu Hướng dẫn (README) cho Mã Xử lý Ảnh Lab 4

## Giới thiệu
Tài liệu này giải thích chi tiết cách hoạt động của các mã Python trong file `lab4.py`, tập trung vào xử lý và phân vùng ảnh với các kỹ thuật khác nhau. Mã được thiết kế để thực hiện các thao tác như ngưỡng Otsu, Adaptive Thresholding, Binary Closing, và các biến đổi hình học/morphology, tương tự cách tài liệu tiếng Việt trong hình ảnh được cấu trúc.

## Công nghệ sử dụng
- **Framework**: Python với các thư viện:
  - `opencv-python`: Đọc và xử lý ảnh, áp dụng ngưỡng Otsu.
  - `numpy`: Xử lý mảng đa chiều, hỗ trợ các phép toán trên ảnh.
  - `imageio.v2`: Đọc và lưu file ảnh.
  - `scipy.ndimage`: Thực hiện các biến đổi hình học và morphology (dilation, erosion, closing, opening).
  - `matplotlib.pyplot`: Trực quan hóa ảnh.
  - `scikit-image`: Cung cấp phương pháp Adaptive Thresholding.
  - `PIL (Pillow)`: Xử lý và chuyển đổi định dạng ảnh.
- Cấu hình này sử dụng CPU để xử lý ảnh, phù hợp với môi trường Google Colab.

## Thuật toán sử dụng

### 1. Giải thích cách hoạt động
- **Ngưỡng Otsu (Otsu Thresholding)**: Tự động xác định ngưỡng tối ưu để phân chia ảnh thành hai vùng (sáng và tối) dựa trên histogram. Sử dụng `cv2.threshold` với `cv2.THRESH_OTSU`.
  - **Cách hoạt động**: Tính toán ngưỡng sao cho độ lệch chuẩn giữa các vùng tối đa, sau đó áp dụng để tạo ảnh nhị phân.
- **Adaptive Thresholding**: Chia ảnh thành các vùng nhỏ và tính ngưỡng cục bộ bằng `threshold_local` từ `skimage.filters`.
  - **Cách hoạt động**: Xác định ngưỡng dựa trên giá trị trung bình hoặc Gaussian của khu vực lân cận, cải thiện độ chính xác phân vùng.
- **Binary Closing**: Kết hợp dilation và erosion để lấp đầy lỗ nhỏ và kết nối vùng trắng, thực hiện bằng `nd.binary_closing`.
  - **Cách hoạt động**: Mở rộng vùng trắng (dilation) rồi co lại (erosion) để giữ nguyên hình dạng nhưng lấp các khoảng trống.
- **Biến đổi hình học (Geometric Transformation)**: Bao gồm xoay (`rotate`), phóng to (`zoom`), và dịch chuyển (`shift`) bằng `scipy.ndimage`.
  - **Cách hoạt động**: Thay đổi tọa độ pixel theo các thông số góc, tỷ lệ, hoặc dịch chuyển.
- **Binary Morphology**: Bao gồm dilation, erosion, và opening, sử dụng `nd.binary_dilation`, `nd.binary_erosion`, `nd.binary_opening`.
  - **Cách hoạt động**: Mở rộng (dilation), co lại (erosion), hoặc kết hợp (opening) các vùng trắng dựa trên cấu trúc phần tử và số lần lặp.

### 2. Kỹ thuật xử lý ảnh
- **Ngưỡng Otsu**: Trích xuất từ `cv2.imread` và áp dụng `cv2.threshold` để tạo ảnh nhị phân từ `dalat.jpg`.
- **Adaptive Thresholding**: Sử dụng `threshold_local` để xử lý `dalat.jpg`, chuyển đổi thành ảnh nhị phân với ngưỡng cục bộ.
- **Binary Closing**: Áp dụng `nd.binary_closing` trên `dalat.jpg` với 10 lần lặp, hiển thị kết quả.
- **Menu Biến đổi**: Tích hợp các hàm như `rotate_image`, `scale_image`, `shift_image`, `otsu_thresholding`, `adaptive_thresholding`, `binary_dilation`, `binary_erosion`, `binary_opening`, `binary_closing`, cho phép người dùng chọn qua giao diện dòng lệnh.

### 3. Bài tập thực hành
- **Bài 1**: Phân vùng ảnh `dalat.jpg` bằng ngưỡng Otsu, hiển thị ảnh gốc và ảnh phân vùng.
- **Bài 2**: Áp dụng Adaptive Thresholding trên `dalat.jpg`, hiển thị kết quả phân vùng.
- **Bài 3**: Thực hiện Binary Closing trên `dalat.jpg` với 10 lần lặp, hiển thị kết quả.
- **Bài 4**: Triển khai menu tương tác với các biến đổi (xoay, phóng to, dịch chuyển, Otsu, Adaptive Thresholding, dilation, erosion, opening, closing), cho phép người dùng chọn và xem kết quả.
