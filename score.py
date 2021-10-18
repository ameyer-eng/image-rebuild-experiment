
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#load an image from the computer
img = mpimg.imread('happy2.jpg')
original_img = np.zeros(img.shape, dtype="uint8")
#original_img[:,:,:] = img[:,:,:]
#original_img = img[:,:,0]
#original_img = original_img.astype(np.int16)




def convert_2_gray_np16(in_img):
    
       #convert the original image into a writable NP array 

       out_img = np.zeros(in_img.shape, dtype="uint8")

       #slice out the red channel to convert to single channel(grey_scale)
       out_img = img[:,:,0]
       #convert the np array from uint8 to int16 for math reasons
       out_img = out_img.astype(np.int16)

       print("out image shape is:" + str(out_img.shape[0]))
       return out_img

    
def convert_back_rgb(in_img):
    #create a np array of appropriate size for the new image
    out_size = (in_img.shape[0], in_img.shape[1], 3)
    out_img = np.zeros(out_size, dtype="uint8")

    #clip the data in the rgb color range
    for x in in_img:
        for y in x:
              
              if y > 255:
                  y = 255
              if y < 0:
                  y = 0

    #convert the array type back to uint8
    in_img = in_img.astype("uint8")

    #copy the first channel to the other channels

    out_img[:,:,0] = in_img[:,:]
    out_img[:,:,1] = in_img[:,:]
    out_img[:,:,2] = in_img[:,:]
    
    return out_img

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
#####################################################################
#####################################################################
#####################################################################
#####################################################################

original_img = convert_2_gray_np16(img)

converted_img = convert_back_rgb(original_img)

#####################################################################
#####################################################################
#####################################################################
#####################################################################





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

rect3plot = plt.imshow(converted_img)
plt.show()

score = generator_0.score(original_img)

print(score)