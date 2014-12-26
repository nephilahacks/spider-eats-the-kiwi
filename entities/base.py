from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Ellipse
from engine.entity import Entity

class BaseEntity(Widget, Entity):
    def __init__(self, imageStr, **kwargs):
        Widget.__init__(self, **kwargs)
        Entity.__init__(self)
        with self.canvas:
            self.size = (Window.width*.002*25, Window.width*.002*25)
            self.rect_bg = Ellipse(source=imageStr, pos=self.pos, size=self.size)
            self.bind(pos=self.update_graphics_pos)
            self.x = self.center_x
            self.y = self.center_y
            self.pos = (self.x, self.y)
            self.rect_bg.pos = self.pos

    def update_graphics_pos(self, instance, value):
        self.rect_bg.pos = value

        def setSize(self, width, height):
            self.size = (width, height)

        def setPos(xpos, ypos):
            self.x = xpos
            self.y = ypos