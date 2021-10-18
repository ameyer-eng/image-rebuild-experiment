
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#load an image from the computer
img = mpimg.imread('happy2.jpg')
original_img = np.zeros(img.shape, dtype="uint8")
#original_img[:,:,:] = img[:,:,:]
original_img = img[:,:,0]

original_img = original_img.astype(np.int16)
print(original_img)

#new_img[:,:,:] = original_img[:,:,:]

"""
def difference_images_sum(original_arr, new_arr):

    difference_sum = 0
    difference_array = original_arr - new_arr
    
    for x in difference_array:
        for y in x:
             for z in y:
                difference_sum = difference_sum + abs(z)
    
    return difference_sum
"""

class image_generator:
    def __init__(self, img_shape):
        print(img_shape)
        self.img = np.zeros(img_shape)
        self.blank_img = np.zeros(img_shape)
    
    def create_square(self):
        square_0 = square(10, 10, 50, 100,self.img)
        square_0.paint()

    def clear(self):
        self.img = self.blank_img
    
    def score(self, image):
        difference_sum = 0
        difference_array = image - self.img
        
        for x in difference_array:
            for y in x:
                    difference_sum = difference_sum + abs(y)
        
        return difference_sum
        
      




class square:
    def __init__(self, x, y, W_H, color, image):
        self.x = x
        self.y = y
        self.W_H = W_H
        self.color = color
        self.original_image = image
        self.image = image


    def paint(self):
            #add code to add the rectangle from the image
        for x in range(self.x, self.x + self.W_H):
            for y in range(self.y, self.y + self.W_H):
                    self.image[y,x] = self.color
        

      


    
generator_0 = image_generator(original_img.shape)
generator_0.create_square()


rect2plot = plt.imshow(generator_0.img, cmap='gray')
plt.show()

diff_img = original_img - generator_0.img

rect3plot = plt.imshow(diff_img, cmap='gray')
plt.show()

score = generator_0.score(original_img)

print(score)