
from random import randrange
import pygame
import numpy as np

class Droplet(object):

    def __init__(self, x_lim, y_lim, radius_init, display, color):
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.x = randrange(0,x_lim)
        self.y = randrange(0, y_lim)
        self.radius = radius_init
        self.display = display
        self.color = color
        self.size = float(radius_init)


    def update(self):

        # TODO Make this grow on a log type scale.
        # Oh, this is fantastic
        self.size += (1/self.radius)
        self.radius = int(self.size)

        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.radius)
