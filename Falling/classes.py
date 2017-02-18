from numpy import pi
from random import randrange
import pygame
import matplotlib.pyplot as plt

class FallDrop():
    def __init__(self, xLim, yLim, radius, vel, color, accel = 0):
        """
        Class for falling drops
        :param xLim: x position
        :param yLim: y position
        :param radius: radius
        :param vel: initial velocity for object
        :param accel: Acceleration for falling object
        """
        self.x = randrange(0, xLim)
        self.y = randrange(0, yLim)
        self.xLim = xLim
        self.yLim = yLim
        self.radius = radius
        self.volume = (3/4)*pi*(radius**3)
        self.velocity = vel
        self.color = color
        self.acceleration = accel


    def update(self, time, Dislplay):

        # TODO why does this not seem to respond until well into the run? ~11 seconds it start working
        self.velocity += self.acceleration * (time/1000)
        self.y += int(self.velocity)
        # TODO figure out why the randrand only makes one random number and doesn't change
        # TODO set this to reset even if velocity is negative - top boundary exceeded
        if (self.y > self.yLim) or (self.y < 0):
            self.y = 0
            self.x = randrange(0,self.xLim)


        pygame.draw.circle(Dislplay, self.color, (self.x, self.y), self.radius)
