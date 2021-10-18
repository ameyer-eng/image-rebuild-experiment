import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy.core.numeric import indices

#original_img = np.zeros((200,1), dtype="uint8")

#load an image from the computer
img = mpimg.imread('happy2.jpg')
original_img = np.zeros(img.shape, dtype="uint8")
#original_img[:,:,:] = img[:,:,:]
original_img = img[:,:,0]
original_img = original_img.astype(np.int16)

width = 10

shift = 5

x = np.linspace(-width + shift, width + shift, 300)
x1 = np.sinc(x)*255
x2 =[x1]
xconc =[x1]

for y in range(299):
    xconc = np.concatenate((xconc, x2), axis=0)

#out_images = np.array(X_train)[indices.astype(int)]

print(xconc)

print(xconc.shape)

rect3plot = plt.imshow(xconc, cmap='gray')
plt.show()

rect2plot = plt.imshow(original_img, cmap='gray')
plt.show()

print(original_img.shape)

d_img = original_img - xconc

rect2plot = plt.imshow(d_img, cmap='gray')
plt.show()











#print(x1)
#print(x1.shape)
#print(x1[50])
