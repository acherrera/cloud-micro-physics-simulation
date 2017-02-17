
from numpy import pi

class Droplet(object):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.volume = (4/3)*pi*(radius**3)

    def show_attributes(self):
        print (self.x, self.y, self.radius, self.volume)