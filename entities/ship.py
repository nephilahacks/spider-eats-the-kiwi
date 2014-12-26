from .base import BaseEntity
from kivy.core.window import Window

class Ship(BaseEntity):

    impulse = 3

    velocity_x = 0
    velocity_y = 0

    def update(self):
        self.move()