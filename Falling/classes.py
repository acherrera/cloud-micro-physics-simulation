from numpy import pi
from random import randrange
import pygame


# TODO look into the velocity and movement a little more. Make velocity from 0-100 maybe.

class FallDrop(object):

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
        self.radius = randrange(2,radius)
        self.volume = (3/4)*pi*(radius**3)
        self.velocity = (vel*self.radius)/radius
        self.color = color
        self.acceleration = accel
        # Used to reset droplet properties later
        self.maxRadius = radius
        self.maxVelocity = vel


    def update(self, time, Display):


        self.velocity += self.acceleration * (time/1000)
        self.y += int(self.velocity)

        # TODO set this to reset even if velocity is negative - top boundary exceeded
        if (self.y > self.yLim):
            self.y = 0
            self.x = randrange(0,self.xLim)
            # Reset droplet properties when starting from the top
            self.radius = randrange(2,self.maxRadius)
            self.velocity = (self.maxVelocity * self.radius) / self.maxRadius

        # Redraw
        pygame.draw.circle(Display, self.color, (self.x, self.y), self.radius)
