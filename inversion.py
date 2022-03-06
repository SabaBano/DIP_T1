# This is a sample Python script.
from matplotlib.image import imread  # import imread to read the image
import matplotlib.pyplot as plt      # plt for plotting
import numpy as np                   # numpy library
import cv2                           # cv file
from PIL import Image                # for importing image
from numpy import asarray            # for array

image_src = imread("photo.jpeg")     # reading input image saved as photo
image_i = 255 - image_src            # inversion
cmap_val = 'gray'                    # for gray image
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 20))  # image axis
ax1.axis("off")                       # axis 1
ax1.title.set_text('Original')        # labeling output image as "Original"
ax2.axis("off")                       # axis 2
ax2.title.set_text("Inverted")        # labeling output image as "Inverted"
ax1.imshow(image_src, cmap=cmap_val)  # for display the output image
ax2.imshow(image_i, cmap=cmap_val)    # for display the output image
plt.show()