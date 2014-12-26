class Entity:

    def __init__(self, x=0, y=0, xvelocity=0, yvelocity=0):
        self._x = x
        self._y = y
        self._xvelocity = xvelocity
        self._yvelocity = yvelocity

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
    def xvelocity(self):
        return self._xvelocity

    @xvelocity.setter
    def xvelocity(self, value):
        self._xvelocity = value

    @property
    def yvelocity(self):
        return self._yvelocity

    @yvelocity.setter
    def yvelocity(self, value):
        self._yvelocity = value

    def move(self):
        self.x = self.x + self.xvelocity
        self.y = self.y + self.yvelocity
