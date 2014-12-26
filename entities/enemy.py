from .base import BaseEntity

class Enemy(BaseEntity):
    velocity_x = 0
    velocity_y = 0

    def update(self):
        self.move()