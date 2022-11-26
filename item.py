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
        self.y = y + 60

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
