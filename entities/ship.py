from .base import BaseEntity
from kivy.core.window import Window

class Ship(BaseEntity):

    impulse = 3

    velocity_x = 0
    velocity_y = 0

    def move(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

        if self.y < Window.height * 0.95:
            self.impulse = -3

    def determineVelocity(self):
        self.impulse = 0.95 * self.impulse

    def update(self):
        self.determineVelocity()
        self.move()