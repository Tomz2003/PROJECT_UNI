# Tài liệu Hướng dẫn (README) cho Mã Xử lý Ảnh

## Giới thiệu
Tài liệu này giải thích chi tiết cách hoạt động của mã Python được cung cấp, tập trung vào xử lý ảnh với các thư viện phổ biến. Mã được thiết kế để thực hiện các thao tác cơ bản và nâng cao trên ảnh, tương tự như cách tài liệu tiếng Việt trong hình ảnh được cấu trúc.

## Công nghệ sử dụng
- **Framework**: Python với các thư viện:
  - `numpy`: Xử lý mảng đa chiều, tương tự tensor trong PyTorch.
  - `imageio.v2`: Đọc và lưu file ảnh.
  - `scipy.ndimage`: Thực hiện các biến đổi hình học và xử lý ảnh nâng cao.
  - `matplotlib.pyplot`: Trực quan hóa ảnh.
- Cấu hình tập trung vào xử lý ảnh trên CPU, tương tự framework mạng nơ-ron hỗ trợ GPU.

## Thuật toán sử dụng

### 1. Hàm mất mát (Loss Function)
- **Mean Square Error (MSE)**: Tính trung bình bình phương sai số giữa đầu vào và mục tiêu.
  - Công thức: `torch.mean((output - target) ** 2)`.
  - Cách hoạt động: Tính hiệu, bình phương, rồi lấy trung bình.
- **Cross Entropy Loss**: Đo lường hiệu suất phân loại với đầu ra là xác suất.
  - Công thức: `torch.cross_entropy(output.unsqueeze(0), target.unsqueeze(0))`.
  - Cách hoạt động: Sử dụng softmax và log-likelihood âm.
- **Binary Cross Entropy (BCE)**: Mất mát cho phân loại nhị phân.
  - Công thức: `-torch.sum(output * torch.log(target) + (1 - output) * torch.log(1 - target)) / n`.
  - Cách hoạt động: Nhân từng phần tử, logarit, tổng hợp và chuẩn hóa.

### 2. Kỹ thuật xử lý ảnh
- **Cắt và lưu ảnh**: Trích xuất vùng (ví dụ: `data[800:1200, 570:980]`) và lưu bằng `iio.imsave`.
- **Dịch chuyển**: Dịch pixel với `nd.shift(data, (100, 25))`, hiển thị xám bằng `plt.imshow`.
- **Phóng to**: Tăng kích thước với `nd.zoom(data, 2)`, điều chỉnh kích thước cụ thể.
- **Xoay**: Xoay ảnh với `nd.rotate(data, 20)`, tùy chọn `reshape`.
- **Dãn nhị phân**: Chuyển nhị phân và dãn với `nd.binary_dilation`.
- **Bản đồ tọa độ**: Tạo méo mó ngẫu nhiên với `nd.map_coordinates`.
- **Biến đổi hình học**: Biến dạng với hàm tùy chỉnh `GeoFun` qua `nd.geometric_transform`.

### 3. Bài tập thực hành
- **Bài 1**: Cắt dâu tây từ `fruit.jpg`, lưu thành `strawberry.jpg`.
- **Bài 2**: Trích xuất `melon` và `apple`, hoán đổi kênh màu, hiển thị song song.
- **Bài 3**: Xoay `mountain` và `boat` từ `quang_ninh.jpg` 45 độ, lưu kết quả.
- **Bài 4**: Phóng to `pagoda` từ `pagoda.jpg` gấp 5 lần.
- **Bài 5**: Công cụ tương tác với các hàm dịch chuyển, xoay, phóng to/thu nhỏ, bản đồ tọa độ, và hoán đổi màu, hỗ trợ nhập liệu và lưu ảnh.

## Tổng kết
Mã sử dụng các thư viện Python để xử lý ảnh từ cơ bản đến nâng cao, phản ánh cấu trúc tài liệu tiếng Việt với giải thích công nghệ, thuật toán, và ứng dụng thực tế.