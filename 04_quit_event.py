"""
Learning how to handle events - Inputs
Making a 'snake' game copy
2 - making a basic framework - crappy framework
3 - showing what events look like
4 - adding quit function to program - good framework
"""
import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))  # Sets size
pygame.display.set_caption('Slither')  # Title of window

pygame.display.update()

gameExit = False

# Basic game loop goes here. Keep the window around
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # This will exit out
            gameExit = True

pygame.quit()
quit()
