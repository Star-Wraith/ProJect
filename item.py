from pico2d import *
from Project2D import *
import Project2D
import enemy
import death
import time

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 30 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Coin:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/item.PNG')
        self.x = x
        self.y = y + 40

        # 충돌 넘버
        self.crash_number = 0

        self.live = 0


    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)

    def update(self):
        self.live += game_framework.frame_time
        if self.live > 0.5:
            game_world.remove_object(self)
        pass

    def get_bb(self):
        return 0, 0, 0, 0

    def handle_collision(self, other, group):

        pass

    def handle_collision2(self, other, group):
        pass


class Red_mushroom:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/item.PNG')
        self.x = x
        self.y = y + 20


        # 충돌 넘버
        self.crash_number = 20

        self.up = 0




    def draw(self):
        self.image.clip_draw(40, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.up < 10 * game_framework.frame_time :

            self.up += game_framework.frame_time
            self.y += 2

        if self.x - Project2D.camera < 0:
            game_world.remove_object(self)

        # if self.y < - 80:
        #     game_world.remove_object(self)

        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):
        if group == 'cat:item':
            game_world.remove_object(self)

        pass

    def handle_collision2(self, other, group):
        if group == 'cat:item':
            game_world.remove_object(self)

        pass

class Poison_mushroom:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/item.PNG')
        self.x = x
        self.y = y + 20


        # 충돌 넘버
        self.crash_number = 43

        self.up = 0




    def draw(self):
        self.image.clip_draw(80, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.up < 10 * game_framework.frame_time :

            self.up += game_framework.frame_time
            self.y += 2

        if self.x - Project2D.camera < 0:
            game_world.remove_object(self)

        # if self.y < - 80:
        #     game_world.remove_object(self)

        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):
        if group == 'cat:item':
            game_world.remove_object(self)

        pass

    def handle_collision2(self, other, group):
        if group == 'cat:item':
            game_world.remove_object(self)

        pass