"""
    Tutorial list
    10 - getting more input from the user. Check for hold down
    11 - adding the vertical motions
    12 - adding boundaries to the game
    13 - making the code a little better. changing hard numbers to
    variables for easier changes later
    14 - adding text to the screen for the user
"""
import pygame
import time

pygame.init()

# Simple colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Display Dimensions
displayWidth = 800
displayHeight = 600

# 'Head' start position
leadX = displayWidth/2
leadY = displayHeight/2

# Initial movement. IE change per frame
leadXChange = 0
leadYChange = 0

blockSize = 10
FPS = 30
gameExit = False

clock = pygame.time.Clock()  # Limiting the FPS here
gameDisplay = pygame.display.set_mode((displayWidth,
                                       displayHeight))
pygame.display.set_caption('Slither')  # Title of window

font = pygame.font.SysFont(None, 25)


def messageToScreen(msg, color):
    # Single function to display text
    screenText = font.render(msg, True, color)
    gameDisplay.blit(screenText,
                     [displayWidth/2, displayHeight/2])


while not gameExit:
    # Main game loop
    for event in pygame.event.get():
        # Event handling loop
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            # key pressed = motion
            if event.key == pygame.K_LEFT:
                leadXChange = -blockSize
                leadYChange = 0
            elif event.key == pygame.K_RIGHT:
                # Use elif because only one option at a time
                leadXChange = blockSize
                leadYChange = 0
            elif event.key == pygame.K_UP:
                leadYChange = -blockSize
                leadXChange = 0
            elif event.key == pygame.K_DOWN:
                leadYChange = blockSize
                leadXChange = 0

        if event.type == pygame.KEYUP:
            # Stop on release
            if event.key == pygame.K_LEFT or\
                    event.key == pygame.K_RIGHT:
                leadXChange = 0
            elif event.key == pygame.K_UP or\
                    event.key == pygame.K_DOWN:
                leadYChange = 0

    if leadX >= displayWidth or leadX <= 0 or\
       leadY >= displayHeight or leadY <= 0:
        # quit if the snake goes off the screen
        gameExit = True

    # Want fill in its own loop, not in the event finder loop
    leadX += leadXChange  # Every loop add change to positions
    leadY += leadYChange
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [leadX, leadY,
                                          blockSize, blockSize])

    # Draw everything in background, THEN update - easier
    pygame.display.update()

    clock.tick(FPS)  # This will change the speed of the snake

messageToScreen("You Lose", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
