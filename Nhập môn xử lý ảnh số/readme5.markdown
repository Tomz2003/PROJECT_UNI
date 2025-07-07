

## Công nghệ sử dụng
- **Framework**: Python với các thư viện:
  - `opencv-python`: Đọc và xử lý ảnh, áp dụng ngưỡng Otsu.
  - `numpy`: Xử lý mảng đa chiều, hỗ trợ các phép toán trên ảnh.
  - `imageio.v2`: Đọc và lưu file ảnh.
  - `scipy.ndimage`: Thực hiện các biến đổi hình học và lọc (Sobel, Gaussian).
  - `matplotlib.pylab`/`matplotlib.pyplot`: Trực quan hóa ảnh.
  - `skimage.morphology`/`skimage.measure`/`skimage.filters.thresholding`: Cung cấp các công cụ gán nhãn, tính thuộc tính vùng, và ngưỡng Otsu.
  - `PIL (Pillow)`: Xử lý và chuyển đổi định dạng ảnh.
  - `google.colab.files`: Tải file lên Google Colab.
- Cấu hình này sử dụng CPU để xử lý ảnh, phù hợp với môi trường Google Colab.

## Thuật toán sử dụng

### 1. Giải thích cách hoạt động
- **Ngưỡng Otsu và Gán nhãn**: Sử dụng `threshold_otsu` để xác định ngưỡng tối ưu, sau đó `label` gán nhãn cho các vùng liên kết trong ảnh nhị phân.
  - **Cách hoạt động**: Tính ngưỡng dựa trên histogram để phân chia ảnh thành hai vùng, sau đó gán nhãn cho mỗi vùng liên kết, vẽ hộp bao quanh (BoundingBox) dựa trên `regionprops`.
- **Dò tìm cạnh với Shift**: Sử dụng `nd.shift` để dịch chuyển ảnh và tính độ chênh lệch tuyệt đối (`abs`) giữa ảnh gốc và ảnh dịch để phát hiện cạnh.
  - **Cách hoạt động**: Tạo ảnh chênh lệch dọc bằng cách dịch chuyển 1 pixel theo trục y, hiển thị kết quả trực quan.
- **Dò tìm cạnh với Sobel Filter**: Áp dụng `nd.sobel` theo trục x và y, tính tổng độ lớn gradient để phát hiện cạnh.
  - **Cách hoạt động**: Sử dụng kernel Sobel để tính gradient, sau đó cộng giá trị tuyệt đối để tạo ảnh cạnh.
- **Harris Corner Detector**: Xây dựng hàm `Harris` để phát hiện góc dựa trên gradient và ma trận cấu trúc.
  - **Cách hoạt động**: Tính gradient theo x và y, áp dụng Gaussian filter để làm mịn, tính determinant và trace của ma trận cấu trúc, sau đó áp dụng công thức R để phát hiện góc.

### 2. Kỹ thuật xử lý ảnh
- **Gán nhãn và BoundingBox**: Sử dụng `label` để gán nhãn, `regionprops` để tính thuộc tính (Area, Centroid, BoundingBox), và `mpatches.Rectangle` để vẽ hộp bao quanh.
- **Dò tìm cạnh Shift**: Tính chênh lệch giữa ảnh gốc và ảnh dịch bằng `nd.shift` và `abs`.
- **Dò tìm cạnh Sobel**: Áp dụng `nd.sobel` theo hai trục, tổng hợp gradient để tạo ảnh cạnh.
- **Harris Corner**: Tích hợp các bước tính gradient, làm mịn bằng Gaussian, và áp dụng công thức R để phát hiện góc.

### 3. Bài tập thực hành
- **Bài 1**: Gán nhãn phân vùng ảnh `geometric.png` bằng ngưỡng Otsu, vẽ hộp bao quanh các vùng, và lưu kết quả thành `label_output.jpg`.
- **Bài 2**: Dò tìm cạnh bằng phương pháp Shift, hiển thị ảnh chênh lệch.
- **Bài 3**: Dò tìm cạnh bằng Sobel Filter, hiển thị ảnh gradient.
- **Bài 4**: Phát hiện góc bằng Harris Corner Detector, hiển thị bản đồ góc.

## Tổng kết
Mã tận dụng các thư viện Python để thực hiện các kỹ thuật xử lý ảnh từ cơ bản (ngưỡng Otsu, gán nhãn) đến nâng cao (Sobel, Harris). Nó phản ánh cấu trúc tài liệu tiếng Việt bằng cách giải thích công nghệ (thư viện), thuật toán (các phương pháp xử lý), và ứng dụng thực tế (bài tập)