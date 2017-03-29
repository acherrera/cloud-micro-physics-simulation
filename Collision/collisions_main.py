"""
Note - this must be one level down from the main directory in order to run correctly. See the current_dir
variable for the reasoning

Collision detection example:
** looks like mask detection (?) is the way to go here **
https://www.pygame.org/docs/tut/SpriteIntro.html  ==> May want/have to make circles into sprites and do this instead
http://stackoverflow.com/questions/22135712/pygame-collision-detection-with-two-circles
https://www.reddit.com/r/pygame/comments/2pxiha/rectanglar_circle_hit_detection/
http://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_mask
"""

# TODO: With no acceleration, the velocity scaling does not work. Assumes initial velocity

import pygame
from Collision.collision_classes import FallDrop
from random import randrange
import os

# This gives the resource path - where all the images are store.
current_dir = os.path.dirname(__file__).split('/')
current_dir.pop(-1)
current_dir = ("/".join(current_dir))
resource_path = current_dir + '/resources'
bg_image_path = resource_path + '/background.png'

pygame.init()

name = 'Falling Simulation'


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

radius = 20


# This is setting the droplet parameters
a = FallDrop(x_lim=width/2,
             y_lim=height,
             radius_lim=10,
             vel_init= 2,
             vel_lim = 2,
             color=light_blue,
             accel=0,
             y_init=0
             )

b = FallDrop(x_lim=((width/2)+ (radius/2)),
             y_lim=height,
             radius_lim=10,
             vel_init= 1,
             vel_lim = 1,
             color=light_blue,
             accel=0,
             y_init=40
             )

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
    a.update(display=gameDisplay, time=timer)
    b.update(display=gameDisplay, time=timer)

    # Update everything
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
