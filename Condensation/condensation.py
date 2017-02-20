
"""
This makes droplets that increase more slowly as they get larger.
"""

import pygame
import os
from Condensation.droplet import Droplet

# This gives the resource path - where all the images are store.
"""
current_dir = os.path.dirname(__file__).split('/')
current_dir.pop(-1)
current_dir = ("/".join(current_dir))
resource_path = current_dir + '/resources'
bg_image_path = resource_path + '/background.png'
"""

current_dir = os.path.dirname(__file__).split('/')
current_dir.pop(-1)
current_dir = ("/".join(current_dir))
resource_path = current_dir + '/resources'
bg_image_path = resource_path + '/background.png'

bg = pygame.image.load(bg_image_path) # used as background later

pygame.init()

name = 'Condensation Simulation'


height = 600
width = 800

white = (255, 255, 255)
black = (0, 0, 0)
dark_blue = (50, 100, 125)
light_blue = (50, 200, 250)

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption(name)

font = pygame.font.SysFont(None, 25)  # setting font for later

FPS = 160
clock = pygame.time.Clock()  # Limiting the FPS here

gameExit = False

drop_number = 10

 #droplets = [FallDrop(x_lim=width, y_lim=height, radius=10, vel_init=0, vel_lim = 5, color=light_blue, accel=0.01) for i in range(drop_number)]

a = Droplet(x_lim=width,
            y_lim=height,
            radius_init=3,
            display=gameDisplay,
            color=light_blue,
            factor=4)

while not gameExit:
    timer = pygame.time.get_ticks()  # Trandrange(0.1, vel)his will give time in milliseconds
    secondTicker = int(timer / 1000)  # Will return whole seconds only
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # handle the quit case
            gameExit = True

    gameDisplay.blit(bg, (0, 0))

    # Draw all the things
    a.update()
    # show time stamp
    label = font.render("Time: {}".format(secondTicker), 1, (255, 255, 0))
    gameDisplay.blit(label, (0, 0))


    # Update everything
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
