import pygame
from pygame.locals import *
import sys
import random
import time
from tkinter import filedialog
from tkinter import *


pygame.init()  # Begin pygame

# Declaring variables to be used through the program
vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

# Create the display
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


# light shade of the button 
color_light = (170,170,170)
color_dark = (100,100,100)
color_white = (255,255,255) 
  
# defining a font
headingfont = pygame.font.SysFont("Verdana", 40)
regularfont = pygame.font.SysFont('Corbel',25)
smallerfont = pygame.font.SysFont('Corbel',16) 
text = regularfont.render('LOAD' , True , color_light)
 



class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("Background.png")
            self.rectBGimg = self.bgimage.get_rect()        
            self.bgY = 0
            self.bgX = 0

      def render(self):
            displaysurface.blit(self.bgimage, (self.bgX, self.bgY))


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Ground.png")
        self.rect = self.image.get_rect(center = (350, 350))

    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))     
          

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
    

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
 
      
    
player = Player()
background = Background()
ground = Ground()



while True:
      
    for event in pygame.event.get():
        # Will run when the close window button is clicked    
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
            
        # For events that occur upon clicking the mouse (left click) 
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass


        # Event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN:
              pass
            
    background.render()
    ground.render()