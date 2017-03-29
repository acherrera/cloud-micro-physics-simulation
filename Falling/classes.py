from numpy import pi
from random import randrange
import pygame


# TODO look into the velocity and movement a little more. Make velocity from 0-100 maybe.

class FallDrop(object):

    # WARNING! Variable soup below. Proceed with caution. or rewrite. Actually, just rewrite it all.
    #TODO rewrite this class

    def __init__(self, x_lim, y_lim, radius, vel_init, vel_lim, color, accel = 0):
        """
        Class for falling drops
        :param x_lim: x position
        :param y_lim: y position
        :param radius: radius
        :param vel_init: initial velocity for object
        :param vel_lim: max velocity allowed
        :param color: color of object
        :param accel: Acceleration for falling object
        """
        if vel_lim < vel_init:
            vel_lim = vel_init
            print("Warning: velocity limit should be larger than initial velocity.")

        self.x = randrange(0, x_lim)
        self.y = randrange(0, y_lim)
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.radius = randrange(2, radius)
        self.volume = (3/4)*pi*(radius**3)
        self.velocity = vel_init
        self.velocity_init = vel_init
        self.color = color
        self.acceleration = accel

        # Used to reset droplet properties later
        self.max_radius = radius
        self.reference_vel = vel_lim
        self.act_vel = self.velocity
        self.max_velocity = (self.reference_vel*self.radius) / self.max_radius



    def update(self, time, display):

        # TODO: find a way to make this less jumpy. Acceleration hopes from low (or none) to faster and faster
        # Add acceleration of less than max, keep acceleration at maximum if already there.
        if self.velocity <= self.max_velocity:
            self.act_vel += self.acceleration * (time/1000)
            self.velocity += int (self.act_vel)
        # Careful: if velocity > max_velocity there is no correction to bring it back, even if max changes on reset
        self.y += int(self.velocity)

        # TODO set this to reset even if velocity is negative - top boundary exceeded
        # Reset the droplet if it is off the screen
        if self.y > self.y_lim:
            self.y = 0
            self.x = randrange(0, self.x_lim)
            # Reset droplet properties when starting from the top
            self.radius = randrange(2, self.max_radius)
            self.max_velocity = (self.reference_vel*self.radius) / self.max_radius
            self.velocity = 0

        # Redraw
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)
