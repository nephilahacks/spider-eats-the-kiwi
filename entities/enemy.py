from .base import BaseEntity

class Enemy(BaseEntity):
    velocity_x = 0
    velocity_y = 0

    def move(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

    def update(self):
        self.move()