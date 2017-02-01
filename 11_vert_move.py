"""
    Tutorial list
    7 - moving rectangles around
    8 - more on moving objects around
    9 - how to keep the game from going crazy (frames per second)
    10 - getting more input from the user. Check for hold down
    11 - adding the vertical motions
"""
import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

frame_x = 800  # I added this for simply referencing later
frame_y = 600


lead_x = 300  # These are 'front' of snake. Or 'lead'
lead_y = 300  # location
# This is set by input later on
lead_x_change = 0   # block changes this much each time
lead_y_change = 0

clock = pygame.time.Clock()  # Limiting the FPS here

gameDisplay = pygame.display.set_mode((frame_x, frame_y))  # Sets size
pygame.display.set_caption('Slither')  # Title of window

gameExit = False

while not gameExit:
    # Main game loop
    for event in pygame.event.get():
        # Event handling loop
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:  # key pressed - motion
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                # Use elif because only one option at a time
                lead_x_change = 10
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0

        if event.type == pygame.KEYUP:
            # Stop on release
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0

    # Want fill in its own loop, not in the event finder loop
    lead_x += lead_x_change  # Every loop add change to positions
    lead_y += lead_y_change
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])  # drew rect

    # Draw everything in background, THEN update - easier for computer
    pygame.display.update()

    clock.tick(15)  # This will change the speed of the snake
# Don't make the FPS what controls the difficulty.
# Higher frames per second makes the computer work much hards

pygame.quit()
quit()
