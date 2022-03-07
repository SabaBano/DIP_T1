# This is a sample Python script.
import numpy as np                                 # importing numpy library
import cv2                                         # importing cv2 file
from matplotlib import pyplot as plt               # importing matplotlib library for plotting graph

img = cv2.imread("photo.jpeg");                    # read input image

hist,bins=np.histogram(img.flatten(),256,[0,256])  # bin range of the width of a single bar of histogram

cdf=hist.cumsum()                                  # cumulative distribution func of histogram
cdf_normalized = cdf*hist.max()/cdf.max()            # cdf of normalized
plt.plot(cdf_normalized,color='b')                 # plotting of normalized cdf
plt.hist(img.flatten(),256,[0,256],color='r')
plt.xlim([0,256])                                  # limit of x-axis
plt.legend(('cdf','histogram'),loc='upper left')   # plotting with label
plt.show()

cdf_m = np.ma.masked_equal(cdf,0)                  # masked_where with condition cdf=0
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())     # calculating cdf_m
cdf = np.ma.filled(cdf_m,0).astype('uint8')        # return input as an array with masked data replaced by a fill value

img2 = cdf[img]                                    # cdf of input image

hist,bins = np.histogram(img2.flatten(),256,[0,256])

cdf = hist.cumsum()                                 # cumulative sum
cdf_normalized = cdf*hist.max()/cdf.max()           # calculating cdf_normalized

plt.plot(cdf_normalized,color='b')                # plotting cdf_normalized
plt.hist(img2.flatten(),256,[0,256],color='r')    # histogram
plt.xlim([0,256])                                 # x-axis limit
plt.legend(('cdf','histogram'),loc='upper left')  # labeling
plt.show()                                        # plot

# cv2.imshow("Original Image",img)
cv2.imshow("Histogram Equalized Image",img2)      # histogram equalized image
cv2.waitKey(0)                                    # delay
cv2.imwrite("photo.jpeg",img2)
cv2.waitKey(0)