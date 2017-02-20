from numpy import pi
from random import randrange
import pygame


# TODO look into the velocity and movement a little more. Make velocity from 0-100 maybe.

class FallDrop(object):

    # WARNING! Variable soup below. Proceed with caution. or rewrite. Actually, just rewrite it all.
    # TODO rewrite this class to better implement actual and int variables. Just convert at end
    # TODO take out all the stupid 'act' varables. Assume float and convert on output. Less confusing

    def __init__(self, x_lim, y_lim, radius_lim, vel_init, vel_lim, color, accel = 0):
        """
        Class for falling drops
        :param x_lim: x position
        :param y_lim: y position
        :param radius_lim: radius
        :param vel_init: initial velocity for object
        :param vel_lim: max velocity allowed
        :param color: color of object
        :param accel: Acceleration for falling object
        """
        if vel_lim < vel_init:
            vel_lim = vel_init
            print("Warning: velocity limit should be larger than initial velocity.")

        self.x = randrange(0, x_lim)
        self.y = randrange(0, y_lim)  # Set to 0 to start from top.
        self.radius = randrange(2, radius_lim)
        self.velocity = vel_init  # Actual velocity. Converted to INT later
        self.max_velocity = (vel_lim*self.radius) / radius_lim
        self.start_fall_time = 0

        # CONSTANTS
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.color = color
        self.acceleration = accel
        self.velocity_init = vel_init  # Starting velocity.
        self.max_radius = radius_lim   # constant
        self.reference_vel = vel_lim  # constant

    def update(self, time, display):

        # Add acceleration of less than max, keep acceleration at maximum if already there.
        if self.velocity < self.max_velocity:
            # need difference to account for reseting of drop each fall
            self.velocity += self.acceleration * (-((self.start_fall_time - time) / 1000))
        elif self.velocity > self.max_velocity:
            self.velocity = self.max_velocity

        self.y += self.velocity


        # TODO set this to reset even if velocity is negative - top boundary exceeded
        # Reset the droplet if it is off the screen
        if self.y > self.y_lim:
            self.y = 0  # Put drop to top
            self.x = randrange(0, self.x_lim)  # Randomly place on x direction.

            # Reset droplet properties when starting from the top
            self.radius = randrange(2, self.max_radius)  # Change radius
            self.max_velocity = (self.reference_vel*self.radius) / self.max_radius  # change max veloicty based on size
            self.velocity = self.velocity_init  # Set velocity to initial velocity
            self.start_fall_time = time  # Reset falling time

        # Redraw
        pygame.draw.circle(display, self.color, (int(self.x), int(self.y)), self.radius)
