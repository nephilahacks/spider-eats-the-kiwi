from .base import BaseEntity

class Bullet(BaseEntity):
    velocity_x = 0
    velocity_y = 0

    def update(self):
        self.move()