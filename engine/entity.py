import math

class Entity:

    def __init__(self, x=0, y=0, velocity=0, direction=0):
        self._x = x
        self._y = y
        self._velocity = velocity
        self._direction = direction

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = value

    def move(self):
        self.x = self.x + self.velocity * math.cos(self.direction)
        self.y = self.y + self.velocity * math.sin(self.direction)
