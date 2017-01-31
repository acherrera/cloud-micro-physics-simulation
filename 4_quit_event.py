"""
Learning how to handle events - Inputs
Making a 'snake' game copy
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
        print(event)
# TODO Put quit function here

pygame.quit()
quit()
