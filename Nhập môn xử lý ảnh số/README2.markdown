# README - XLA Lab 2 Image Processing Project

## Giới thiệu
Đây là một dự án Python thực hiện các kỹ thuật xử lý ảnh cơ bản và nâng cao, bao gồm biến đổi ảnh (đảo ngược, gamma), biến đổi Fourier (FFT, bộ lọc Butterworth), và các phép biến đổi ngẫu nhiên trên kênh màu và tần số. Dự án được chia thành các bài tập thực hành với giao diện tương tác.

## Công nghệ sử dụng
- **Framework**: Mã sử dụng Python với các thư viện sau:
  - `PIL (Python Imaging Library)`: Để mở, xử lý và chuyển đổi ảnh (chuyển sang thang độ xám với `.convert('L')`).
  - `numpy`: Để thực hiện các phép toán mảng và xử lý dữ liệu ảnh dưới dạng mảng số.
  - `matplotlib.pyplot`: Để trực quan hóa ảnh và hiển thị kết quả.
  - `scipy.fftpack`: Để thực hiện biến đổi Fourier nhanh (FFT) và các bộ lọc liên quan.
- Cấu hình này tập trung vào xử lý ảnh cơ bản và phân tích tần số, không yêu cầu GPU mà chủ yếu chạy trên CPU.

## Thuật toán sử dụng
Mã triển khai nhiều thuật toán xử lý ảnh khác nhau, được chia thành các bài tập và công cụ tương tác, giải thích chi tiết dưới đây:

### 1. Bài tập 1: Biến đổi cơ bản
- **Giải thích cách hoạt động**
  - **Image Inverse Transformation**: Đảo ngược giá trị pixel của ảnh. Hàm `image_inverse(img_path)` đọc ảnh, chuyển sang thang độ xám, thực hiện phép toán `255 - im_arr` để đảo ngược (giá trị tối đa 255 trở thành 0 và ngược lại), sau đó tạo ảnh mới từ mảng đã xử lý và hiển thị cả ảnh gốc và ảnh đảo ngược.
    - **Cách hoạt động**: Lấy mỗi pixel, trừ giá trị của nó khỏi 255 để tạo hiệu ứng âm bản.
  - **Gamma Correction**: Điều chỉnh độ sáng của ảnh dựa trên hàm mũ. Hàm `gamma_correction(img_path, gamma=0.5)` chuẩn hóa ảnh về khoảng [0, 1], áp dụng `np.power(im_norm, gamma)` để điều chỉnh độ tương phản, sau đó nhân với 255 và giới hạn giá trị trong [0, 255].
    - **Cách hoạt động**: Giá trị gamma < 1 làm sáng ảnh, > 1 làm tối ảnh, hiển thị kết quả so sánh với ảnh gốc.
  - **Các phương pháp khác (Log Transformation, Histogram Equalization, Contrast Stretching)**: Hiện tại chỉ có mã khung, chưa được triển khai đầy đủ, nhưng dự kiến sẽ điều chỉnh độ sáng và tương phản theo các phương pháp thống kê và phân phối histogram.

### 2. Bài tập 2: Biến đổi Fourier
- **Giải thích cách hoạt động**
  - **Fast Fourier Transform (FFT)**: Chuyển đổi ảnh từ miền không gian sang miền tần số. Hàm `fast_fourier_transform(img_path)` sử dụng `fftpack.fft2` để tính FFT, dịch chuyển với `fftpack.fftshift`, áp dụng log để tăng độ tương phản (`np.log(1 + fft_shifted)`), và chuẩn hóa về [0, 255] để hiển thị.
    - **Cách hoạt động**: Hiển thị phổ tần số, cho phép phân tích thành phần tần số của ảnh.
  - **Butterworth Filter**: Áp dụng bộ lọc thông thấp (`lowpass`) hoặc thông cao (`highpass`). Hàm `butterworth_filter(img_path, filter_type='lowpass', d0=30, order=1)` tính FFT, tạo mặt nạ Butterworth dựa trên khoảng cách từ tâm (`D = np.sqrt((X - center_col)**2 + (Y - center_row)**2)`), nhân với FFT đã dịch chuyển, và chuyển ngược về miền không gian với `fftpack.ifft2`.
    - **Cách hoạt động**: Bộ lọc thông thấp loại bỏ tần số cao (chi tiết), thông cao loại bỏ tần số thấp (nền), với `d0` là tần số cắt và `order` là bậc của bộ lọc.

### 3. Câu 3: Biến đổi ngẫu nhiên (RGB và độ xám)
- **Giải thích cách hoạt động**
  - **Random RGB Swap**: Hàm `random_rgb_swap(img_path)` tách ảnh thành các kênh R, G, B, xáo trộn ngẫu nhiên thứ tự kênh bằng `random.shuffle`, sau đó hợp nhất lại thành ảnh mới.
    - **Cách hoạt động**: Tạo hiệu ứng đổi màu ngẫu nhiên dựa trên sắp xếp kênh.
  - **Apply Random Transformation 1**: Hàm `apply_random_transformation_1(img)` chọn ngẫu nhiên một trong các phương pháp (`inverse`, `gamma`, `log`, `histogram`, `contrast`) trên ảnh thang độ xám. Mỗi phương pháp được áp dụng như sau:
    - `inverse`: Đảo ngược giá trị pixel (`255 - im_arr`).
    - `gamma`: Điều chỉnh gamma với giá trị ngẫu nhiên từ 0.3 đến 2.0.
    - `log`: Áp dụng logarit để nén dải động (`128.0 * np.log(1 + im_float)`).
    - `histogram`: Bình đẳng hóa histogram bằng cách tính CDF (phân phối tích lũy) và ánh xạ lại giá trị.
    - `contrast`: Giãn tương phản dựa trên giá trị min/max của mảng.
    - **Cách hoạt động**: Kết quả được giới hạn trong [0, 255] và hiển thị so sánh với ảnh gốc và ảnh sau khi đổi RGB.

### 4. Câu 4: Biến đổi ngẫu nhiên (Fourier)
- **Giải thích cách hoạt động**
  - **Apply Random Transformation 2**: Hàm `apply_random_transformation_2(img)` chọn ngẫu nhiên một trong các phương pháp (`fft`, `lowpass`, `highpass`) trên ảnh thang độ xám. Mỗi phương pháp được áp dụng như sau:
    - `fft`: Tính FFT và hiển thị phổ tần số như trong bài 2.
    - `lowpass`: Áp dụng bộ lọc Butterworth thông thấp với `d0` và `order` ngẫu nhiên, thêm lọc min để làm mịn.
    - `highpass`: Áp dụng bộ lọc Butterworth thông cao với `d0` và `order` ngẫu nhiên, thêm lọc max để tăng chi tiết.
    - **Cách hoạt động**: Kết quả được chuẩn hóa và hiển thị so sánh với ảnh gốc và ảnh sau khi đổi RGB.

## Yêu cầu hệ thống
- Python 3.x
- Các thư viện sau (cài đặt bằng `pip install`):
  - `Pillow` (PIL)
  - `numpy`
  - `matplotlib`
  - `scipy`

## Cấu trúc dự án
- Ảnh đầu vào: `quang_ninh.jpg`, `ha-long-bay-in-vietnam.jpg` (cần đặt trong cùng thư mục với file Python).

## Chức năng
### 1. Bài tập 1: Biến đổi cơ bản
- **Image Inverse Transformation**: Đảo ngược giá trị pixel để tạo hiệu ứng âm bản.
- **Gamma Correction**: Điều chỉnh độ sáng và tương phản dựa trên giá trị gamma.
- **Các phương pháp khác**: Log Transformation, Histogram Equalization, Contrast Stretching (chưa hoàn thiện).

### 2. Bài tập 2: Biến đổi Fourier
- **Fast Fourier Transform (FFT)**: Chuyển ảnh sang miền tần số để phân tích.
- **Butterworth Filter**: Áp dụng bộ lọc thông thấp hoặc thông cao với tần số cắt và bậc tùy chọn.

### 3. Câu 3: Biến đổi ngẫu nhiên (RGB và độ xám)
- **Random RGB Swap**: Xáo trộn ngẫu nhiên thứ tự kênh màu (R, G, B).
- **Random Transformation**: Áp dụng ngẫu nhiên một trong các phép biến đổi (inverse, gamma, log, histogram, contrast) trên ảnh thang độ xám.

### 4. Câu 4: Biến đổi ngẫu nhiên (Fourier)
- **Random Transformation**: Áp dụng ngẫu nhiên FFT, bộ lọc thông thấp hoặc thông cao, với xử lý bổ sung để làm mịn hoặc tăng chi tiết.

## Hướng dẫn sử dụng
1. Đặt các file ảnh (`quang_ninh.jpg`, `ha-long-bay-in-vietnam.jpg`) trong cùng thư mục với `xla_lab2.py`.
2. Chạy file `xla_lab2.py` 
3. Theo hướng dẫn trên màn hình:
   - **Bài 1**: Chọn phương pháp (I, G, L, H, C, Q), nhập giá trị gamma nếu cần.
   - **Bài 2**: Chọn phương pháp (F, L, H, Q), nhập đường dẫn ảnh và tham số bộ lọc (nếu cần).
   - Kết quả được hiển thị trực quan qua matplotlib.


# Tổng kết
 Sử dụng các thư viện Python để thực hiện các biến đổi ảnh cơ bản (đảo ngược, gamma) và nâng cao (FFT, bộ lọc Butterworth), cùng với các phép biến đổi ngẫu nhiên trên kênh màu và tần số. Nó cung cấp giao diện tương tác để người dùng chọn phương pháp, hiển thị kết quả trực quan, và phản ánh cấu trúc tài liệu bằng cách giải thích công nghệ, thuật toán và ứng dụng thực tế qua các bài tập.