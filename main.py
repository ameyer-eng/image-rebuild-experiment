import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random



def color_block(image):

    rand_color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    
    rand_x1 =random.randint(0,1100)
    rand_x2 =random.randint(rand_x1, 1100)
    
    rand_y1 =random.randint(0,620)
    rand_y2 =random.randint(rand_y1, 620)

    for x in range(rand_x1,rand_x2):
        for y in range(rand_y1, rand_y2):
            image[y,x] = rand_color

#load an image from the computer
img = mpimg.imread('tired_woman.jpg')

#print(img)

"""fig, axs = plt.subplots(1, 3, figsize=(18,3) ) 

for c, ax in zip(range(3), axs):
    tmp_img = np.zeros(img.shape, dtype="uint8")
    tmp_img[:,:,c] = img[:,:,c]
    ax.imshow(tmp_img)
    ax.set_aspect("equal")
    ax.set_axis_off()
#display the image from the number array
imgplot = plt.imshow(img)
plt.subplots_adjust(wspace=0, hspace=0)

plt.show() """

#print("Hello World!")
#print(img.shape)
#input("")


new_img = np.zeros(img.shape, dtype = "uint8")
print(new_img.shape)

"""for c in new_img:
    for x in c:
        for y in x:
            print(y)"""

print(new_img[0,0,0])

"""#for c in range(3):
for x in range(10,100):
    for y in range(10,1000):
        new_img[x,y] = [255,0,0]"""

plt.show()

for n in range(3):
    color_block(new_img)
    img2plot = plt.imshow(new_img)
    plt.draw() 


       




