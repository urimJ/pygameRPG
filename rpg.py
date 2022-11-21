import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *
from Background import *

pygame.init()

vec = pygame.math.Vector2
HEIGHT, WIDTH = (350, 700)
FPS = 60
FPS_CLOCK = pygame.time.Clock()

ACC = 0.3
FRIC = -0.10

COUNT = 0

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("파이게임 RPG")

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

    # Render Functions -----
    bg = Background()
    bg.backgournd.render()
    bg.ground.render()

    pygame.display.update()
    FPS_CLOCK.tick(FPS)