from pico2d import *
import game_framework



PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
# Rocket
SPEED_ROKET_KMPH = 50.0 # Km / Hour
SPEED_ROKET_MPM = (SPEED_ROKET_KMPH  * 1000.0 / 60.0)
SPEED_ROKET_MPS = (SPEED_ROKET_MPM / 60.0)
SPEED_ROKET_PPS = (SPEED_ROKET_MPS * PIXEL_PER_METER)
# normal
SPEED_NORMAL_KMPH = 15.0 # Km / Hour
SPEED_NORMAL_MPM = (SPEED_NORMAL_KMPH  * 1000.0 / 60.0)
SPEED_NORMAL_MPS = (SPEED_NORMAL_MPM / 60.0)
SPEED_NORMAL_PPS = (SPEED_NORMAL_MPS * PIXEL_PER_METER)

# turtle
SPEED_TURTLE_KMPH = 15.0 # Km / Hour
SPEED_TURTLE_MPM = (SPEED_TURTLE_KMPH  * 1000.0 / 60.0)
SPEED_TURTLE_MPS = (SPEED_TURTLE_MPM  / 60.0)
SPEED_TURTLE_PPS = (SPEED_TURTLE_MPS * PIXEL_PER_METER)

# air
SPEED_AIR_KMPH = 15.0 # Km / Hour
SPEED_AIR_MPM = (SPEED_AIR_KMPH  * 1000.0 / 60.0)
SPEED_AIR_MPS = (SPEED_AIR_MPM  / 60.0)
SPEED_AIR_PPS = (SPEED_AIR_MPS * PIXEL_PER_METER)

class Enemy_roket:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/enemy.png')
        self.image2 = load_image('./res/enemyRe.png')
        self.x = x
        self.y = y
        self.y_first = self.y
        self.dir = 1
        self.count = 0

    def update(self):
        # while self.y > 0:
        #     self.count += 1
        #     if count % 10 == 0:
        #         self.y -= 1
        # self.y += self.dir * 1
        self.y += self.dir * SPEED_ROKET_PPS * game_framework.frame_time
        if self.y > 600:
            self.dir = -1
            self.y = 600
        elif self.y < 120:
            self.dir = 1
            self.y = 120
    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(229, 0, 55, 76, self.x, self.y)

        else:
            self.image.clip_draw(169, 0, 55, 76, self.x, self.y)

class Enemy_normal:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/enemy.png')
        self.image2 = load_image('./res/enemyRe.png')
        self.x = x
        self.y = y
        self.dir = 1
        self.x_max = self.x + 100

    def update(self):
        # while self.y > 0:
        #     self.count += 1
        #     if count % 10 == 0:
        #         self.y -= 1
        # self.x += self.dir * 1/3
        self.x += self.dir * SPEED_NORMAL_PPS * game_framework.frame_time
        if self.x > self.x_max:
            self.dir = -1
            self.x = self.x_max
        elif self.x < self.x_max - 200:
            self.dir = 1
            self.x = self.x_max - 200
    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(397, 27, 55, 49, self.x, self.y)
        else:
            self.image.clip_draw(0, 27, 55, 49, self.x, self.y)

class Enemy_turtle:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/enemy.png')
        self.image2 = load_image('./res/enemyRe.png')
        self.x = x
        self.y = y
        self.dir = 1
        self.x_max = self.x + 100

    def update(self):
        # while self.y > 0:
        #     self.count += 1
        #     if count % 10 == 0:
        #         self.y -= 1
        # self.x += self.dir * 1/3
        self.x += self.dir * SPEED_TURTLE_PPS * game_framework.frame_time

        if self.x > self.x_max:
            self.dir = -1
            self.x = self.x_max
        elif self.x < self.x_max - 200:
            self.dir = 1
            self.x = self.x_max - 200
    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(340, 8, 55, 76, self.x, self.y)
        else:
            self.image.clip_draw(55, 8, 55, 76, self.x, self.y)


class Enemy_air:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/enemy.png')
        self.image2 = load_image('./res/enemyRe.png')
        self.x = x
        self.y = y
        self.dir = 1


    def update(self):
        # while self.y > 0:
        #     self.count += 1
        #     if count % 10 == 0:
        #         self.y -= 1
        self.x += self.dir * 1/3
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(54, 20, 60, 56, self.x, self.y)
        else:
            self.image.clip_draw(340, 20, 58, 56, self.x, self.y)