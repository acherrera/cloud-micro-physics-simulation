"""
    Tutorial list
    2 - making a basic framework - crappy framework
    3 - showing what events look like
    4 - adding quit function to program - good framework
    5 - going over colors and fill
    6 - drawing rectangles and more colors
"""
import pygame

pygame.init()

# Defining colors here - use RGB values (Red, Gree, Blue, Alpha)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))  # Sets size
pygame.display.set_caption('Slither')  # Title of window


gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # This will exit out
            gameExit = True

    # Want fill in its own loop, not in the event finder loop
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [400, 300, 10, 10])  # drew rect
    gameDisplay.fill(red, rect=[200, 200, 50, 50])  # Can be accerlated
    # Draw everything in background, THEN update - easier for computer
    pygame.display.update()

pygame.quit()
quit()
