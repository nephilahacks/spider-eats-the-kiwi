from .base import BaseEntity
from kivy.core.window import Window

class Ship(BaseEntity):
    def __init__(self, *args, **kwargs):
        super(Ship, self).__init__(*args, **kwargs)
        self.active = True