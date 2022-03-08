# splitting original image into red green and blue color

from matplotlib.image import imread                          # importing matplotlib library for image reading
import matplotlib.pyplot as plt                              # importing matplotlib library for plotting
import numpy as np                                           # import numpy library for arrays
import cv2                                                   # opencv files
from PIL import Image                                        # for importing image
from numpy import asarray                                    # from numpy library import array

img = cv2.imread("photo.jpeg")                               # reading the input
img1 = cv2.resize(img,(500,800))                             # resizing the input image

cv2.imshow("original image",img1)                            # show/display the input image
# cv2.waitKey(0)
b,g,r = cv2.split(img1)                                      # splitting the original image
zeros_ch = np.zeros(img1.shape[0:2],dtype="uint8")           # zero channel
red = cv2.merge([zeros_ch,zeros_ch,r])                       # In red first 2 coordinates are zero
green = cv2.merge([zeros_ch,g,zeros_ch])                     # In red first and last coordinates are zero
blue = cv2.merge([b,zeros_ch,zeros_ch])                      # In red last 2 coordinates are zero
cv2.imshow("Red image",red)                                  # show/display the Red color image
cv2.imshow("Green image",green)                              # show/display the green color image
cv2.imshow("Blue image",blue)                                # show/display the blue color image
cv2.waitKey(0)
