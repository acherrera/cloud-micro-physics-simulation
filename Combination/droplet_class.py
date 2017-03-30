


# Class creation for the combined droplet. 

from random import randrange
import pygame
import numpy as np

class Droplet(object):

    def __init__(self, x_lim, y_lim, radius_init, display, color,
            growth_factor, vel_init, vel_lim, radius_max, accel=0):
        self.x_lim = x_lim                  #
        self.y_lim = y_lim                  #
        self.x = randrange(0,x_lim)         #
        self.y = randrange(0, y_lim)        #

        # use = randrand(2, radius) to create random starting randius
        # current have uniform starting
        self.radius = radius_init
        self.display = display
        self.color = color
        self.size = float(radius_init)
        self.growth_factor = growth_factor
        self.velocity = vel_init
        self.velocity_init = vel_init
        self.acceleration = accel

        # Used to reset droplet properties later
        self.max_radius = radius
        self.reference_vel = vel_lim
        self.act_vel = self.velocity
        self.max_velocity = (self.reference_vel*self.radius) / self.max_radius




    def update(self, time, display):

        # =========== This is the condensation part ==========

        # Growth slows as droplet gets larger
        self.size += (1/(self.growth_factor*self.radius))
        self.radius = int(self.size)



        # ========== This is the falling portion ============= 

        if self.velocity <= self.max_velocity:
            self.act_vel += self.acceleration * (time/1000)
            self.velocity += int (self.act_vel)
        # Careful: if velocity > max_velocity there is no correction to bring it back, even if max changes on reset
        self.y += int(self.velocity)

        # Change max velocity base on size
        self.max_velocity = (self.reference_vel*self.radius) / self.max_radius

        # TODO set this to reset even if velocity is negative - top boundary exceeded
        # TODO make velocity work as a function of radius
        # Reset the droplet if it is off the screen
        if self.y > self.y_lim:
            self.y = 0
            self.x = randrange(0, self.x_lim)

            # Reset droplet properties when starting from the top
            self.radius = randrange(2, self.max_radius)
            self.velocity = 0

        # This HAS to be the last thing that is done
        pygame.draw.circle(self.display, self.color, (self.x, self.y), self.radius)
