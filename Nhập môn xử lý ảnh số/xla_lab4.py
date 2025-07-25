# -*- coding: utf-8 -*-
"""lab4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PEc3L0e3BbG4vegjZYSCt2kxbvwTax6V
"""

!pip install opencv-python numpy imageio scipy matplotlib scikit-image

import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('dalat.jpg', cv2.IMREAD_GRAYSCALE)
_, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('ảnh gốc')
plt.subplot(122), plt.imshow(thresh, cmap='gray'), plt.title('lang_biang.jpg')
plt.show()

from PIL import Image
import numpy as np
import imageio.v2 as iio
from skimage.filters import threshold_local
import matplotlib.pyplot as plt

# Đọc ảnh và chuyển sang thang độ xám
data = Image.open('dalat.jpg').convert('L')
a = np.array(data)

# Áp dụng Adaptive Thresholding
p = threshold_local(a, 39, offset=10)
b = (a > p).astype(np.uint8) * 255  # Chuyển thành ảnh nhị phân
b = Image.fromarray(b)

# Hiển thị kết quả
plt.imshow(b, cmap='gray')
plt.title('ho_xuan_huong.jpg.')
plt.show()

from PIL import Image
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt

# Đọc ảnh và chuyển sang thang độ xám
data = Image.open('dalat.jpg').convert('L')

# Áp dụng Binary Closing
p = nd.binary_closing(data, iterations=10)
c = Image.fromarray(p)

# Hiển thị kết quả
plt.imshow(c, cmap='gray')
plt.title('Ảnh sau Binary Closing (10 iterations)')
plt.show()

from PIL import Image
import numpy as np
import scipy.ndimage as nd
from skimage.filters import threshold_local
import matplotlib.pyplot as plt
import cv2

# Hàm thực hiện các biến đổi
def rotate_image(image_array, angle=45):
    return nd.rotate(image_array, angle, reshape=True)

def scale_image(image_array, factor=2):
    return nd.zoom(image_array, factor)

def shift_image(image_array, dx=50, dy=20):
    return nd.shift(image_array, (dy, dx))

def otsu_thresholding(image_array):
    _, thresh = cv2.threshold(image_array, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def adaptive_thresholding(image_array):
    thresh = threshold_local(image_array, 39, offset=10)
    return (image_array > thresh).astype(np.uint8) * 255

def binary_dilation(image_array, iterations=5):
    return nd.binary_dilation(image_array, iterations=iterations)

def binary_erosion(image_array, iterations=5):
    return nd.binary_erosion(image_array, iterations=iterations)

def binary_opening(image_array, iterations=5):
    return nd.binary_opening(image_array, iterations=iterations)

def binary_closing(image_array, iterations=5):
    return nd.binary_closing(image_array, iterations=iterations)

def display_image(image_array, title):
    plt.imshow(image_array, cmap='gray')
    plt.title(title)
    plt.show()
def main():
    data = Image.open('dalat.jpg').convert('L')
    data_array = np.array(data)

    while True:
        # Hiển thị menu
        print("\n=== MENU BIẾN ĐỔI HÌNH HỌC VÀ PHÂN VÙNG ===")
        print("1. Rotate (Xoay)")
        print("2. Scale (Phóng to)")
        print("3. Shift (Dịch chuyển)")
        print("4. Otsu Thresholding")
        print("5. Adaptive Thresholding")
        print("6. Binary Dilation")
        print("7. Binary Erosion")
        print("8. Binary Opening")
        print("9. Binary Closing")
        print("10. Thoát")

        choice = input("Chọn một tùy chọn (1-10): ")

        if choice == '1':
            rotated = rotate_image(data_array)
            display_image(rotated, 'Ảnh sau khi xoay 45°')
        elif choice == '2':
            scaled = scale_image(data_array)
            display_image(scaled, 'Ảnh sau khi phóng to 2x')
        elif choice == '3':
            shifted = shift_image(data_array)
            display_image(shifted, 'Ảnh sau khi dịch chuyển')
        elif choice == '4':
            otsu = otsu_thresholding(data_array)
            display_image(otsu, 'Ảnh sau Otsu Thresholding')
        elif choice == '5':
            adaptive = adaptive_thresholding(data_array)
            display_image(adaptive, 'Ảnh sau Adaptive Thresholding')
        elif choice == '6':
            binary = adaptive_thresholding(data_array)
            dilated = binary_dilation(binary)
            display_image(dilated, 'Ảnh sau Binary Dilation')
        elif choice == '7':
            binary = adaptive_thresholding(data_array)
            eroded = binary_erosion(binary)
            display_image(eroded, 'Ảnh sau Binary Erosion')
        elif choice == '8':
            binary = adaptive_thresholding(data_array)
            opened = binary_opening(binary)
            display_image(opened, 'Ảnh sau Binary Opening')
        elif choice == '9':
            binary = adaptive_thresholding(data_array)
            closed = binary_closing(binary)
            display_image(closed, 'Ảnh sau Binary Closing')
        elif choice == '10':
            print("Đã thoát chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại (1-10).")

if __name__ == "__main__":
    main()