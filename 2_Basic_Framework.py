"""
This program will just open and close the window.
This is the most basic ever
"""
import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))  # Sets size

# pygame.display.flip() # See below
# .flip() updates the entire screen, not just changed parts

pygame.display.update()

pygame.quit()
quit()
