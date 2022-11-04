from pico2d import *

class Enemy_roket:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('enemy.png')
        self.image2 = load_image('enemyRe.png')
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
        self.y += self.dir * 1
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
        self.image = load_image('enemy.png')
        self.image2 = load_image('enemyRe.png')
        self.x = x
        self.y = y
        self.dir = 1
        self.x_max = self.x + 100

    def update(self):
        # while self.y > 0:
        #     self.count += 1
        #     if count % 10 == 0:
        #         self.y -= 1
        self.x += self.dir * 1/3
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
        self.image = load_image('enemy.png')
        self.image2 = load_image('enemyRe.png')
        self.x = x
        self.y = y
        self.dir = 1
        self.x_max = self.x + 100

    def update(self):
        # while self.y > 0:
        #     self.count += 1
        #     if count % 10 == 0:
        #         self.y -= 1
        self.x += self.dir * 1/3
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
        self.image = load_image('enemy.png')
        self.image2 = load_image('enemyRe.png')
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