from pico2d import *

class Grass:
    def __init__(self):  # 생성자
        self.image = load_image('brocknormal.PNG')
        self.x = 20
        self.y = 60


    def draw(self):
        while self.y > 0:
            self.x = 20
            while self.x < 800:
                self.image.clip_draw(0, 0, 40, 40, self.x, self.y)

                self.x += 40
            self.y -= 40
        self.x = 20
        self.y = 60

    def update(self):
        pass
