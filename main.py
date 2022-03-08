from matplotlib.image import imread                                    # importing matplotlib library for image reading
import matplotlib.pyplot as plt                                        # importing matplotlib library for plotting
import numpy as np                                                     # import numpy library for arrays
import cv2                                                             # opencv files
from PIL import Image                                                  # for importing image
from numpy import asarray                                              # from numpy library import array

# Assignment 1 Grayscale_image
# (R+G+B)/3"
input_image = imread("photo.jpeg")                                       # input image
img1 = cv2.imread("photo.jpeg")
gamma= 1.04
r,g,b=input_image[: ,:,0 ],input_image[: ,: ,1], input_image[:,:,2]   # r,g,b of input image
r_const,g_const,b_const=0.33,0.33,0.33                                # assign constant for r,b,g
grayscale_image = r_const * r*gamma + g_const * g*gamma + b_const *b*gamma                # grayscale value

# Assignment 2 Binary image
# using opencv converting rgb to binary"
img = cv2.imread("photo.jpeg",2)                                        # read input image
ret , binary_image=cv2.threshold(input_image,128,255,cv2.THRESH_BINARY)       # binary image

# Assignment 3 Addition of input and binary image
Assignment_3 = input_image + binary_image                              # input + binary_image

# Assignment 4 Addition of grayscale image and constant number 20
Assignment_4= grayscale_image + 20.0                                   # grayscale_image + 20
# images = [input_image,grayscale_image,binary_image,Assignment_3,Assignment_4]
plt.show()

cv2.imshow("INPUT IMAGE",img1)                                        # show the input image
cv2.imshow("OUTPUT OF ASSIGNMENT 1",img)                              # output of assignment 1
cv2.imshow("OUTPUT OF ASSIGNMENT 2",binary_image)                     # output of assignment 2
cv2.imshow("OUTPUT OF ASSIGNMENT 3",Assignment_3)                     # output of assignment 3
cv2.waitKey(0)                                                        # delay of 0 sec
cv2.imshow("OUTPUT OF ASSIGNMENT 4",Assignment_4)                     # output of assignment 4
cv2.waitKey(0)