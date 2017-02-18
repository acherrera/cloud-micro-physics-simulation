from numpy import pi
from random import randrange
import pygame

class FallDrop():
    def __init__(self, x_lim, y_lim, radius, vel, color, accel = 0):
        """
        Class for falling drops
        :param x_lim: x position
        :param y_lim: y position
        :param radius: radius
        :param vel: initial velocity for object
        :param accel: Acceleration for falling object
        """
        self.x = randrange(0, x_lim)
        self.y = randrange(0, y_lim)
        self.xLim = x_lim
        self.yLim = y_lim
        self.radius = radius
        self.volume = (3/4)*pi*(radius**3)
        self.velocity = vel
        self.color = color
        self.acceleration = accel

    def update(self, time, Dislplay):
        print(time)

        # TODO why does this not seem to respond until well into the run? ~11 seconds it start working
        self.velocity += self.acceleration * (time/1000)
        self.y += int(self.velocity * (time/1000))
        # TODO figure out why the randrand only makes one random number and doesn't change
        # self.x += randrange(-1,1) # This is to test the random function. DOES NOT work. Only make randome number once
        if (self.x > self.xLim) or (self.x < 0):
            self.x = randrange(0,self.xLim)

        if (self.y > self.yLim) or (self.y < 0):
            self.y = 0

        pygame.draw.circle(Dislplay, self.color, (self.x, self.y), self.radius)

