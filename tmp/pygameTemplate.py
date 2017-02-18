
import pygame

pygame.init()

name = 'template'

height = 800
width = 600

white = (255,255,255)
black = (0, 0, 0)
dark_blue = (50, 100, 125)

gameDisplay = pygame.display.set_mode((height, width))
pygame.display.set_caption(name)

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # handle the quit case
            gameExit = True

    gameDisplay.fill(dark_blu)
    pygame.display.update()

pygame.quit()
quit()