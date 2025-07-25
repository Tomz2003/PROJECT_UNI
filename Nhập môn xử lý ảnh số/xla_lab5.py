# -*- coding: utf-8 -*-
"""xla_lab5

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DRPUuFxPolmlbvhQFsmpIg4_D78nr9LM
"""

!pip install opencv-python numpy matplotlib scikit-image
2.1
from PIL import Image
import numpy as np
import imageio.v2 as iio
from skimage.morphology import label
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage.filters.thresholding import threshold_otsu
from google.colab import files


uploaded = files.upload()
data = Image.open('geometric.png').convert('L')
a = np.asarray(data)


thresh = threshold_otsu(a)
b = (a > thresh).astype(np.uint8)


c = label(b)

c_normalized = ((c - c.min()) * 255 / (c.max() - c.min())).astype(np.uint8)
cl = Image.fromarray(c_normalized)
iio.imsave('label_output.jpg', cl)


d = regionprops(c)


fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
ax.imshow(c, cmap='YlOrRd')


for i in d:
    if 'BoundingBox' in i:
        lr, lc, ur, uc = i['BoundingBox']
        rec_width = uc - lc
        rec_height = ur - lr
        rect = mpatches.Rectangle((lc, lr), rec_width, rec_height, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(rect)

plt.show()
2.2
from PIL import Image
import numpy as np
import imageio.v2 as iio
import scipy.ndimage as nd
from skimage.morphology import label
from skimage.measure import regionprops
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
from skimage.filters.thresholding import threshold_otsu

data = Image.open('geometric.png').convert('L')
bmg = abs(data - nd.shift(data, (0, 1), order=0))
plt.imshow(bmg)
plt.show()
2.3
from PIL import Image
import numpy as np
import cv2
import imageio.v2 as iio
import scipy.ndimage as nd
from skimage.morphology import label
from skimage.measure import regionprops
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
from skimage.filters.thresholding import threshold_otsu

data = Image.open('geometric.png')
a = nd.sobel(data, axis=0)
b = nd.sobel(data, axis=1)
bmg = abs(a) + abs(b)
plt.imshow(bmg)
plt.show()
2.4
from PIL import Image
import numpy as np
import cv2
import imageio.v2 as iio
import scipy.ndimage as nd
from skimage.morphology import label
from skimage.measure import regionprops
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
from skimage.filters.thresholding import threshold_otsu

def Harris(indata, alpha=0.2):
    x = nd.sobel(indata, 0)
    y = nd.sobel(indata, 1)
    x1 = x ** 2
    y1 = y ** 2
    xy = abs(x * y)
    x1 = nd.gaussian_filter(x1,3)
    y1 = nd.gaussian_filter(y1,3)
    xy = nd.gaussian_filter(xy,3)

    detC = x1 * y1 - 2 * xy
    trC = x1 + y1
    R = detC - alpha * trC**2
    return R

data = Image.open('geometric.png')
bmg = Harris(data)
plt.imshow(bmg)
plt.show()
