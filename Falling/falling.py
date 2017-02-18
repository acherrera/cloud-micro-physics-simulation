
import pygame
from Falling.classes import FallDrop
from random import randrange

print (randrange(0,10))



pygame.init()

name = 'template'

height = 800
width = 600

white = (255,255,255)
black = (0, 0, 0)
dark_blue = (50, 100, 125)
light_blue = (50, 200, 250)

gameDisplay = pygame.display.set_mode((height, width))
pygame.display.set_caption(name)

font = pygame.font.SysFont(None, 25) # setting font for later

FPS = 60
clock = pygame.time.Clock()  # Limiting the FPS here


gameExit = False

a = FallDrop(height, width, 20, 0, light_blue, accel= 0.000002)
# for later: objects = [MyClass(property=foo, property2=prop) for prop in props]
# TODO implement multiple objects above
# TODO add a fall acceleration or velocity parameter to FallDrp class

while not gameExit:
    timer = pygame.time.get_ticks()
    secondTicker = timer/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # handle the quit case
            gameExit = True


    gameDisplay.fill(dark_blue)
    # show time stamp
    label = font.render("Time: {}".format(int(secondTicker)), 1, (255,255,0))
    gameDisplay.blit(label, (0,0))

    # Update Droplet
    a.update(timer, gameDisplay)

    # Update everything
    pygame.display.update()
    clock.tick()

pygame.quit()
quit()