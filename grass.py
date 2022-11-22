from pico2d import *
from Project2D import *
import Project2D
import enemy
import death
import time

def TTime():
    time_second = time.time() + 10
    while True:
        if time.time() > time_second:
            break
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 30 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


#1 일반 블럭
class Grass:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/brocknormal.PNG')
        self.x = x + 20
        self.y = y + 20

        # 충돌 넘버
        self.crash_number = 1


    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):
        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):
        pass
#2 ? 블럭
class Block_QM:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/blockqm.PNG')
        self.x = x + 20
        self.y = y + 20

        # 충돌 넘버
        self.crash_number = 2
    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass

#3 투명 블럭
class Block_Shadow:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/blockqm.PNG')
        self.x = x + 20
        self.y = y + 20

        # 충돌 넘버
        self.crash_number = 3
    def draw(self):

        self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):
        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass
#4 산
class Mountain:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.PNG')
        self.x = x + 20
        self.y = y + 91

        # 충돌 넘버
        self.crash_number = 4
    def draw(self):
        self.image.clip_draw(0, 314, 298, 182, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return 0, 0, 0, 0
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass

#5 ' ' 구름
class Cloud:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.PNG')
        self.x = x + 20
        self.y = y + 20

        # 충돌 넘버
        self.crash_number = 5
    def draw(self):
        self.image.clip_draw(303, 354, 138, 80, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass


    def get_bb(self):
        return 0, 0, 0, 0
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass

#6 그냥 구름
class Cloudsmall:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.PNG')
        self.x = x + 20
        self.y = y + 20

        # 충돌 넘버
        self.crash_number = 6
    def draw(self):
        self.image.clip_draw(302, 212, 101, 58, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass
    def get_bb(self):
        return 0, 0, 0, 0
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass


#7 저장 플래그
class Flag:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.PNG')
        self.x = x + 20
        self.y = y + 62

        # 충돌 넘버
        self.crash_number = 7
    def draw(self):
        self.image.clip_draw(0, 6, 67, 124, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass
    def get_bb(self):
        return 0, 0, 0, 0
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass
#8 점프대
class JUMP_Bar:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/item.PNG')
        self.x = x + 20
        self.y = y + 24

        # 충돌 넘버
        self.crash_number = 8
    def draw(self):
        self.image.clip_draw(357, 8, 47, 49, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 23 - Project2D.camera, self.y - 23, self.x + 23 - Project2D.camera, self.y + 23
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):
        Project2D.cat.speed = 10


        pass

#9 떨어지는 블럭
class Block_Drop:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/dropblock.PNG')
        self.x = x + 20
        self.y = y + 40
        self.speed = 0

        # 충돌 넘버
        self.crash_number = 9
    def draw(self):
        self.image.clip_draw(0, 0, 40, 80, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.speed
        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 40, self.x + 20 - Project2D.camera, self.y + 40
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):
        self.speed = 2 * RUN_SPEED_PPS * game_framework.frame_time

        pass

#21 빨간버섯 ? 블럭
class Block_RM:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/blockqm.PNG')
        self.x = x + 20
        self.y = y + 20

        # 충돌 넘버
        self.crash_number = 21
    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass


    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass

#42 독버섯 ? 블럭
class Block_PM:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/blockqm.PNG')
        self.x = x + 20
        self.y = y + 20

        # 충돌 넘버
        self.crash_number = 42

    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass


    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass



#88 나무
class TREE:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.PNG')
        self.x = x + 20
        self.y = y + 58

        # 충돌 넘버
        self.crash_number = 88
    def draw(self):
        self.image.clip_draw(504, 373, 60, 121, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return 0, 0, 0, 0
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass

#10 스위치
class SWITCH:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/switch.png')
        self.x = x + 20
        self.y = y + 40
        self.COUNT = 0

        # 충돌 넘버
        self.crash_number = 10
    def draw(self):
        self.image.clip_draw(0, 0, 80, 80, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 40 - Project2D.camera, self.y - 40, self.x + 40 - Project2D.camera, self.y + 40
    def handle_collision(self, other, group):
        if self.COUNT == 0:
            game_world.remove_object(self)

            Project2D.Bye_bgm.set_volume(60)
            Project2D.Bye_bgm.repeat_play()

            Project2D.BOMB.append(enemy.Enemy_BOMB(6800, 800))
            game_world.add_objects(Project2D.BOMB, 2)

            Project2D.BOMB.append(enemy.Enemy_BOMB(6000, 800))
            game_world.add_objects(Project2D.BOMB, 2)
            self.COUNT += 1


        pass
    def handle_collision2(self, other, group):
        if self.COUNT == 0:
            game_world.remove_object(self)

            Project2D.Bye_bgm.set_volume(60)
            Project2D.Bye_bgm.repeat_play()

            Project2D.BOMB.append(enemy.Enemy_BOMB(6800, 800))
            game_world.add_objects(Project2D.BOMB, 2)

            Project2D.BOMB.append(enemy.Enemy_BOMB(6000, 800))
            game_world.add_objects(Project2D.BOMB, 2)
            self.COUNT += 1
        pass



#11 굴뚝
class Roof:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/roof.png')
        self.x = x + 20
        self.y = y + 80

        # 충돌 넘버
        self.crash_number = 11
    def draw(self):
        self.image.clip_draw(0, 0, 120, 160, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 60 - Project2D.camera, self.y - 80, self.x + 60 - Project2D.camera, self.y + 80
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass

#33 풀
class Leaf:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.png')
        self.x = x + 20
        self.y = y + 20

        # 충돌 넘버
        self.crash_number = 33
    def draw(self):
        self.image.clip_draw(302, 436, 116, 62, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return 0, 0, 0, 0
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass
# 55: 결승봉
class Bong:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/bong.png')
        self.x = x + 20
        self.y = y + 220

        # 충돌 넘버
        self.crash_number = 55
    def draw(self):
        self.image.clip_draw(0, 0, 40, 440, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass


    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 220, self.x + 20 - Project2D.camera, self.y + 220

    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass

# 56: 결승문
class Clear_Door:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.png')
        self.x = x + 20
        self.y = y + 90

        # 충돌 넘버
        self.crash_number = 56
    def draw(self):
        self.image.clip_draw(0, 133, 198, 180, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return 0, 0, 0, 0
    def handle_collision(self, other, group):
        pass
    def handle_collision2(self, other, group):

        pass

#99 올라가는 블럭
class Block_UP:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/blockqm.PNG')
        self.x = x + 20
        self.y = y + 20
        self.speed = 0

        # 충돌 넘버
        self.crash_number = 99
    def draw(self):

        self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):
        self.y += self.speed
        self.speed = 0
        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20
    def handle_collision(self, other, group):

        self.speed = 100

        pass
    def handle_collision2(self, other, group):

        pass