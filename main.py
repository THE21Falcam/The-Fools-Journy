# pip install pygame
import pygame
from pygame.locals import *
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

pygame.init()
flags = pygame.SCALED
Display = pygame.display.set_mode((320, 184), flags)
pygame.display.set_caption('Berktown Caves')

run = True
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()  #Updating The Screen

pygame.quit()  #CloseWindow
