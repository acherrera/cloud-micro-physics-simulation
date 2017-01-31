"""
    Tutorial list
    4 - adding quit function to program - good framework
    5 - going over colors and fill
    6 - drawing rectangles and more colors
    7 - moving rectangles around
    8 - more on moving objects around
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

lead_x = 300  # These are 'front' of snake. Or 'lead'
lead_y = 300  # location

while not gameExit:
    for event in pygame.event.get():  # Event handler
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10  # Move one block left. One block is 10x10
            if event.key == pygame.K_RIGHT:
                lead_x += 10

    # Want fill in its own loop, not in the event finder loop

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])  # drew rect

    # Draw everything in background, THEN update - easier for computer
    pygame.display.update()

pygame.quit()
quit()
