from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Ellipse
from random import randint
from kivy.config import Config
from entities.bullet import Bullet
from entities.ship import Ship
from entities.enemy import Enemy
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import math

Config.set('graphics', 'resizable', 0)

Window.clearcolor = (0, 0, 0, 1.)

class Engine(Widget):
    enemiesList = []
    bulletsList = []
    minProb = 1700

    def __init__(self, **kwargs):
        super(Engine, self).__init__(**kwargs)
        self.score = Label(text='Score: 0')
        self.score.x = 10
        self.score.y = Window.height * 0.90
        self.add_widget(self.score)
        self.ship = Ship(imageStr='./assets/images/ship.jpg')
        self.ship.x = Window.width / 4
        self.ship.y = Window.height / 2
        self.add_widget(self.ship)
        Clock.schedule_interval(self.fire, 5.0/60.0)

    def fire(self, dt):
        imageStr = './assets/images//bullet.png'
        fired_bullet = Bullet(imageStr)
        fired_bullet.velocity = 12
        fired_bullet.x = self.ship.x
        fired_bullet.y = self.ship.y
        self.bulletsList.append(fired_bullet)
        self.add_widget(fired_bullet)

    def addEnemy(self):
        imageStr = './assets/images/enemy.png'
        tmpEnemy = Enemy(imageStr)
        tmpEnemy.x = Window.width * 0.99
        ypos = randint(1, 16)
        ypos = ypos * Window.height * .0625
        tmpEnemy.y = ypos
        tmpEnemy.velocity = 5
        tmpEnemy.direction = math.pi
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
        self.velocity = 0

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
        for enemy in self.enemiesList[:]:
            removed = False
            for bullet in self.bulletsList[:]:
                if enemy.collide_widget(bullet):
                    self.bulletsList.remove(bullet)
                    self.remove_widget(bullet)
                    self.enemiesList.remove(enemy)
                    self.remove_widget(enemy)
                    removed = True
                    self.score.text = ': '.join(("Score", str(int(self.score.text.split(":")[1]) + enemy.points)))
                    break
            if removed:
                continue
            if enemy.collide_widget(self.ship):
                print 'You lose'
                self.gameOver()
                Clock.unschedule(self.update)
            enemy.update()
        self.ship.velocity = 0


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
