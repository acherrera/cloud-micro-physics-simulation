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

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

frame_x = 800
frame_y = 600
gameDisplay = pygame.display.set_mode((frame_x, frame_y))  # Sets size
pygame.display.set_caption('Slither')  # Title of window


gameExit = False

lead_x = 300  # These are 'front' of snake. Or 'lead'
lead_y = 300  # location
# This is set by input later on
lead_x_change = 0   # block changes this much each time

while not gameExit:
    for event in pygame.event.get():  # Event handler
        # Holding a key is not an event in itself.
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10

    # Want fill in its own loop, not in the event finder loop
    lead_x += lead_x_change
    # This was added in by me for funsies. Keeps square on screen
    if (lead_x > frame_x):
        lead_x = 0
    elif (lead_x < 0):
        lead_x = frame_x
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])  # drew rect

    # Draw everything in background, THEN update - easier for computer
    pygame.display.update()

pygame.quit()
quit()
