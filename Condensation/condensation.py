
"""
This makes droplets that increase more slowly as they get larger.
"""

import pygame
from droplet import Droplet

# This gives the resource path - where all the images are store.
"""
current_dir = os.path.dirname(__file__).split('/')
current_dir.pop(-1)
current_dir = ("/".join(current_dir))
resource_path = current_dir + '/resources'
bg_image_path = resource_path + '/background.png'
"""

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

a = [Droplet(width, height, 1, gameDisplay, light_blue, 20)
            for i in range(drop_number)]

#a = Droplet(width, height, 5, gameDisplay, light_blue)

while not gameExit:
    timer = pygame.time.get_ticks()  # Trandrange(0.1, vel)his will give time in milliseconds
    secondTicker = int(timer / 1000)  # Will return whole seconds only
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # handle the quit case
            gameExit = True

    gameDisplay.fill(dark_blue)

    # Draw all the things
    for thingy in a:
        thingy.update()
    # show time stamp
    label = font.render("Time: {}".format(secondTicker), 1, (255, 255, 0))
    gameDisplay.blit(label, (0, 0))


    # Update everything
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
