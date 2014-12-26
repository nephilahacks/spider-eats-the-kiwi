from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.graphics import Ellipse
from random import randint
from kivy.config import Config

Config.set('graphics', 'resizable', 0)

Window.clearcolor = (0, 0, 0, 1.)


class BaseEntity(Widget):
    def __init__(self, imageStr, **kwargs):
        super(BaseEntity, self).__init__(**kwargs)
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


class Bullet(BaseEntity):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    def move(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

    def update(self):
        self.move()


class Enemy(BaseEntity):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    def move(self):
        self.x = self.x + self.velocity_x
        self.y = self.y + self.velocity_y

    def update(self):
        self.move()


class Ship(BaseEntity):

    impulse = 3

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

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


class Engine(Widget):
    enemiesList = []
    bulletsList = []
    minProb = 1700

    def __init__(self, **kwargs):
        super(Engine, self).__init__(**kwargs)
        self.ship = Ship(imageStr='./ship.jpg')
        self.ship.x = Window.width / 4
        self.ship.y = Window.height / 2
        self.add_widget(self.ship)
        Clock.schedule_interval(self.fire, 5.0/60.0)

    def fire(self, dt):
        imageStr = './bullet.png'
        fired_bullet = Bullet(imageStr)
        fired_bullet.velocity_x = 5
        fired_bullet.x = self.ship.x + 40
        fired_bullet.y = self.ship.y
        self.bulletsList.append(fired_bullet)
        self.add_widget(fired_bullet)

    def addEnemy(self):
        imageStr = './enemy.png'
        tmpEnemy = Enemy(imageStr)
        tmpEnemy.x = Window.width * 0.99
        ypos = randint(1, 16)
        ypos = ypos * Window.height * .0625
        tmpEnemy.y = ypos
        tmpEnemy.velocity_y = 0
        vel = 30
        tmpEnemy.velocity_x = -0.1 * vel
        self.enemiesList.append(tmpEnemy)
        self.add_widget(tmpEnemy)

    def on_touch_down(self, touch):
        touch.ud["initial_pos"] = (touch.x, touch.y)

    def on_touch_move(self, touch):
        diff_x = touch.x -touch.ud["initial_pos"][0]
        diff_y = touch.y -touch.ud["initial_pos"][1]
        self.ship.center_x = self.ship.center_x + diff_x
        self.ship.center_y = self.ship.center_y + diff_y
        touch.ud["initial_pos"] = (touch.x, touch.y)

    def gameOver(self):
        Clock.unschedule(self.update)
        Clock.unschedule(self.fire)
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self, dt):
        self.ship.update()
        tmpCount = randint(1, 1800)
        if tmpCount > self.minProb:
            self.addEnemy()
            if self.minProb < 1300:
                self.minProb = 1300
            self.minProb = self.minProb - 1

        for bullet in self.bulletsList:
            bullet.update()
        for enemy in self.enemiesList:
            if enemy.collide_widget(self.ship):
                print 'You lose'
                self.gameOver()
                Clock.unschedule(self.update)
            enemy.update()
        self.ship.velocity_x = 0
        self.ship.velocity_y = 0


class MainApp(App):
    def build(self):
        self.title = 'Nephila Space Adventures'
        parent = Widget()
        app = Engine()
        Clock.schedule_interval(app.update, 1.0/60.0)
        parent.add_widget(app)
        return parent


if __name__ == '__main__':
    MainApp().run()
