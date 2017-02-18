"""
Note - this must be one level down from the main directory in order to run correctly. See the current_dir
variable for the reasoning
"""

import pygame
from Falling.classes import FallDrop
from random import randrange
import os

# This gives the resource path - where all the images are store.
current_dir = os.path.dirname(__file__).split('/')
current_dir.pop(-1)
current_dir = ("/".join(current_dir))
resource_path = current_dir + '/resources'
bg_image_path = resource_path + '/background.png'

pygame.init()

name = 'template'

height = 600
width = 800

white = (255, 255, 255)
black = (0, 0, 0)
dark_blue = (50, 100, 125)
light_blue = (50, 200, 250)

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption(name)
bg = pygame.image.load(bg_image_path) # used as background later


font = pygame.font.SysFont(None, 25)  # setting font for later

FPS = 60
clock = pygame.time.Clock()  # Limiting the FPS here

gameExit = False

dropnumber = 100

# a = FallDrop(xLim=width, yLim=height, radius=10, vel=1, color=light_blue, )
droplets = [FallDrop(xLim=width, yLim=height, radius=10, vel=10, color=light_blue) for i in range(dropnumber)]

# TODO implement multiple objects above
# TODO add a fall acceleration or velocity parameter to FallDrp class

while not gameExit:
    timer = pygame.time.get_ticks()  # Trandrange(0.1, vel)his will give time in milliseconds
    secondTicker = int(timer / 1000)  # Will return whole seconds only
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # handle the quit case
            gameExit = True

    gameDisplay.blit(bg,(0,0))
    # show time stamp
    label = font.render("Time: {}".format(secondTicker), 1, (255, 255, 0))
    gameDisplay.blit(label, (0, 0))

    # Update Droplet
    for drop in droplets:
        drop.update(timer, gameDisplay)

    # Update everything
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
