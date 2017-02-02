"""
    Tutorial list
    13 - making the code a little better. changing hard numbers to
    variables for easier changes later
    14 - adding text to the screen for the user
    15 - adding more function to game over
       - defining game loop in its own thing
       - moved changing varables to gameloop
    16 - added apple for the snake to eat
       - added length to apple
    17 - alining apple with the snake
       - allow snake to eat apple
"""
import pygame
import random

pygame.init()

# Simple colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Display Dimensions
displayWidth = 800
displayHeight = 600

blockSize = 10
FPS = 30

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


def gameLoop():
    # Main loop for the game

    # Game status - exit when True
    gameExit = False
    gameOver = False

    # 'Head' start position
    leadX = displayWidth/2
    leadY = displayHeight/2

    # Initial movement. IE change per frame
    leadXChange = 0
    leadYChange = 0

    # apple location - needs to be divisble by 10 to match head
    randAppleX = random.randrange(0,
                                  displayWidth-blockSize, 10)
    randApplyY = random.randrange(0,
                                  displayHeight-blockSize, 10)

    while not gameExit:
        # Game loop runs here
        while gameOver:
            # When game is over, show this screen
            gameDisplay.fill(white)
            messageToScreen("Game over, press C to play" +
                            " again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                # Check what input is
                if event.type == pygame.KEYDOWN:
                    print(event)
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        # run the game again
                        # TODO fix this - have to exit many times
                        gameLoop()

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
                    leadXChange = blockSize
                    leadYChange = 0
                elif event.key == pygame.K_UP:
                    leadYChange = -blockSize
                    leadXChange = 0
                elif event.key == pygame.K_DOWN:
                    leadYChange = blockSize
                    leadXChange = 0
            """ Uncomment to stop on release
            if event.type == pygame.KEYUP:
                # Stop on release
                if event.key == pygame.K_LEFT or\
                        event.key == pygame.K_RIGHT:
                    leadXChange = 0
                elif event.key == pygame.K_UP or\
                        event.key == pygame.K_DOWN:
                    leadYChange = 0
            """

        if leadX >= displayWidth or leadX <= 0 or\
           leadY >= displayHeight or leadY <= 0:
            # quit if the snake goes off the screen
            gameOver = True

        leadX += leadXChange
        leadY += leadYChange
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randApplyY, 
                                            blockSize, blockSize])
        pygame.draw.rect(gameDisplay, black, [leadX, leadY,
                                              blockSize, blockSize])

        if leadX == randAppleX and leadY == randApplyY:
            print("om nom nom")

        # Draw everything in background, THEN update - easier
        pygame.display.update()

        clock.tick(FPS)  # This will change the speed of the snake

gameLoop()


pygame.quit()
quit()
