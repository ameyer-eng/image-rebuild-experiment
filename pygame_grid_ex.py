import pygame
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#load an image from the computer
img = mpimg.imread('happy2.jpg')
tmp_img = np.zeros(img.shape, dtype="uint8")
tmp_img[:,:,:] = img[:,:,:]



class Viewer:
    def __init__(self, update_func, display_size):
        self.update_func = update_func
        pygame.init()
        self.display = pygame.display.set_mode(display_size)
    
    def set_title(self, title):
        pygame.display.set_caption(title)
    
    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            Z = self.update_func()
            surf = pygame.surfarray.make_surface(Z)
            self.display.blit(surf, (0, 0))

            pygame.display.update()

        pygame.quit()

def color_block(image):

    rand_color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    
    rand_x1 =random.randint(0,200)
    rand_x2 =random.randint(rand_x1, 200)
    
    rand_y1 =random.randint(0,200)
    rand_y2 =random.randint(rand_y1, 200)

    for x in range(rand_x1,rand_x2):
        for y in range(rand_y1, rand_y2):
            image[y,x] = rand_color

            
#todo add functions that help the update function convert from numpy 16 bit 
#and undo color slicing to get function back to Uint8 3 channel for pygame

def update():
    #image = np.random.random((600, 600, 3)) * 255.0
    image = np.zeros(tmp_img.shape, dtype = "uint8")
    image[:,:,:] = tmp_img[:,:,:]

    for n in range(3):
        color_block(image)

    row_1 = np.concatenate((image, tmp_img, tmp_img),axis=0)
    row_2 = np.concatenate((image, tmp_img, tmp_img),axis=0)
    row_3 = np.concatenate((image, tmp_img, tmp_img),axis=0)

    grid_image = np.concatenate((row_1,row_2,row_3), axis=1)
    

    return grid_image.astype('uint8')



##This code is from outside of the classes

viewer = Viewer(update, (900, 900))
viewer.start()

