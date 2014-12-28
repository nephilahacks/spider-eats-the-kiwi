from .base import BaseEntity

class Enemy(BaseEntity):
    def __init__(self, imageStr, **kwargs):
        super(Enemy, self).__init__(imageStr, **kwargs)
        self.points = 50