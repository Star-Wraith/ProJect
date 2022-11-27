from pico2d import *
import game_framework
import game_world
from cat import Cat
import Project2D
import death

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
# Rocket
SPEED_ROKET_KMPH = 100.0 # Km / Hour
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
    def __init__(self, x, y, xPos):  # 생성자
        self.image = load_image('./res/enemy.png')
        self.image2 = load_image('./res/enemyRe.png')
        self.x = x
        self.y = y
        self.y_first = self.y
        self.dir = -1
        self.count = 0
        self.xPos = xPos
        self.Sound = load_music('./SE/kirra.mp3')
        self.Sound.set_volume(60)
        self.One = True

        # 충돌 넘버
        self.crash_number = 0



    def update(self):
        # while self.y > 0:
        #     self.count += 1
        #     if count % 10 == 0:
        #         self.y -= 1
        # self.y += self.dir * 1
        # self.y += self.dir * SPEED_ROKET_PPS * game_framework.frame_time
        if self.xPos <= Project2D.camera:
            # self.dir = -1
            if self.One == True:
                self.Sound.play()
                self.One = False
            self.y += self.dir * SPEED_ROKET_PPS * game_framework.frame_time
        # 화면 벗어나면 지우기
        if self.x - Project2D.camera < -20 or self.y < -20:
            game_world.remove_object(self)
            print('지우기 성공')
    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(229, 0, 55, 76, self.x - Project2D.camera, self.y)
        else:
            self.image.clip_draw(169, 0, 55, 76, self.x - Project2D.camera, self.y)

    def get_bb(self):
        return self.x - 27 - Project2D.camera, self.y - 38, self.x + 27 - Project2D.camera, self.y + 38

    def handle_collision(self, other, group):
        print('닿음')
        # if group == 'cat:rocket':
        #     game_world.game_world_clear()
        pass

    def handle_collision2(self, other, group):
        pass

class Enemy_BOMB:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/BOMB.png')
        self.x = x
        self.y = y
        self.y_first = self.y
        self.dir = -1
        self.TIME = 0
        self.One = True

        # 충돌 넘버
        self.crash_number = 0

    def update(self):


        self.y += 2 * self.dir * SPEED_ROKET_PPS * game_framework.frame_time



    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(0, 0, 800, 400, self.x - Project2D.camera, self.y)

    def get_bb(self):
        return self.x - 400 - Project2D.camera, self.y - 200, self.x + 400 - Project2D.camera, self.y + 200

    def handle_collision(self, other, group):
        # if group == 'cat:BOMB':
        #     game_world.game_world_clear()
        pass

    def handle_collision2(self, other, group):
        # if group == 'cat:BOMB':
        #     game_world.game_world_clear()
        pass


class Enemy_normal:
    def __init__(self, x, y, xPos=False):  # 생성자
        self.image = load_image('./res/enemy.png')
        self.image2 = load_image('./res/enemyRe.png')
        self.x = x
        self.y = y
        self.dir = 1
        self.x_max = self.x + 100
        self.gravity = 0
        self.xPos = xPos

        # 충돌 넘버
        self.crash_number = 0

    def update(self):
        if self.xPos == False:
            # self.x += self.dir * SPEED_NORMAL_PPS * game_framework.frame_time
            if self.gravity == 0:
                self.x += self.dir * SPEED_NORMAL_PPS * game_framework.frame_time
                if self.x - Project2D.camera > self.x_max - Project2D.camera:
                    self.dir = -1
                    # self.x = self.x_max
                elif self.x - Project2D.camera < self.x_max - 200 - Project2D.camera:
                    self.dir = 1
                    # self.x = self.x_max - 200
            if self.x - Project2D.camera < -20 or self.y < -20:
                game_world.remove_object(self)
                print('지우기 성공')
            self.y -= self.gravity
            if self.gravity == 0:
                self.gravity = 6 * SPEED_NORMAL_PPS * game_framework.frame_time
        else:
            if self.xPos <= Project2D.camera:

                if self.gravity == 0:
                    self.x += self.dir * SPEED_NORMAL_PPS * game_framework.frame_time
                    if self.x - Project2D.camera > self.x_max - Project2D.camera:
                        self.dir = -1
                        # self.x = self.x_max
                    elif self.x - Project2D.camera < self.x_max - 200 - Project2D.camera:
                        self.dir = 1
                        # self.x = self.x_max - 200
                if self.x - Project2D.camera < -20 or self.y < -20:
                    game_world.remove_object(self)
                    print('지우기 성공')
                self.y -= self.gravity
                if self.gravity == 0:
                    self.gravity = 6 * SPEED_NORMAL_PPS * game_framework.frame_time


        #
        # self.y -= self.gravity
        # if self.gravity == 0:
        #     self.gravity = SPEED_NORMAL_PPS * game_framework.frame_time
    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(397, 27, 55, 49, self.x - Project2D.camera, self.y)
        else:
            self.image.clip_draw(0, 27, 55, 49, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 30 - Project2D.camera, self.y - 30, self.x + 30 - Project2D.camera, self.y + 30

    def handle_collision(self, other, group):
        print('닿음')
        if group == 'enemy:grass':
                if self.dir == 1:
                    self.dir = -1
                else:
                    self.dir = 1

        pass

    def handle_collision2(self, other, group):
        if group == 'cat:enemy':
            game_world.remove_object(self)
        if group == 'enemy:grass':
            self.gravity = 0
        pass

class Enemy_turtle:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/enemy.png')
        self.image2 = load_image('./res/enemyRe.png')
        self.x = x
        self.y = y
        self.dir = 1
        self.x_max = self.x + 100

        # 충돌 넘버
        self.crash_number = 0

    def update(self):
        self.x += self.dir * SPEED_TURTLE_PPS * game_framework.frame_time

        if self.x - Project2D.camera > self.x_max - Project2D.camera and self.dir != 3:
            self.dir = -1
        elif self.x - Project2D.camera < self.x_max - Project2D.camera - 200 and self.dir != 3:
            self.dir = 1

        if self.x - Project2D.camera < -30 or self.y < -40:
            game_world.remove_object(self)
            print('지우기 성공')
    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(340, 8, 55, 76, self.x - Project2D.camera, self.y)
        elif self.dir == -1:
            self.image.clip_draw(55, 8, 55, 76, self.x - Project2D.camera, self.y)
        elif self.dir == 0 or self.dir == 3:
            self.image.clip_draw(115, 51, 53, 58, self.x - Project2D.camera, self.y)


    def get_bb(self):
        return self.x - 27 - Project2D.camera, self.y - 38, self.x + 27 - Project2D.camera, self.y + 38

    def handle_collision(self, other, group):
        print('닿음')
        # if group == 'cat:turtle':
        #     game_world.game_world_clear()
        if group == 'turtle:grass':
            if self.dir == 1:
                self.dir = -1
            else:
                self.dir = 1
        pass

    def handle_collision2(self, other, group):
        if group == 'cat:turtle' and self.dir == 0:
            self.dir = 3
        if group == 'cat:turtle' and self.dir != 3:
            self.y -= 9
            self.dir = 0
            pass


class Enemy_air:
    def __init__(self, x, y, xPos):  # 생성자
        self.image = load_image('./res/enemy.png')
        self.image2 = load_image('./res/enemyRe.png')
        self.x = x
        self.y = y
        self.dir = -1
        self.xPos = xPos

        # 충돌 넘버
        self.crash_number = 0

    def update(self):

        if self.xPos <= Project2D.camera:
            self.x += self.dir * SPEED_AIR_PPS * game_framework.frame_time

        if self.x - Project2D.camera < -30 or self.y < -30:
            game_world.remove_object(self)
            print('지우기 성공')


    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(54, 20, 60, 56, self.x - Project2D.camera, self.y)
        else:
            self.image.clip_draw(340, 20, 58, 56, self.x - Project2D.camera, self.y)

    def get_bb(self):
        return self.x - 29 - Project2D.camera, self.y - 28, self.x + 29 - Project2D.camera, self.y + 28

    def handle_collision(self, other, group):
        print('닿음')
        # if group == 'cat:air':
        #     game_world.game_world_clear()
        pass


class Enemy_fireball:
    def __init__(self, x, y, xPos):  # 생성자
        self.image = load_image('./res/fireball.png')
        self.x = x
        self.y = y
        self.xPos = xPos

        # 충돌 넘버
        self.crash_number = 0

    def update(self):
        if self.xPos <= Project2D.camera:
            self.x -= 2 * SPEED_AIR_PPS * game_framework.frame_time

        if self.x - Project2D.camera < -30 or self.y < -30:
            game_world.remove_object(self)
            print('지우기 성공')


    def draw(self):
        self.image.clip_draw(0, 0, 57, 46, self.x - Project2D.camera, self.y)

    def get_bb(self):
        return self.x - 28 - Project2D.camera, self.y - 23, self.x + 28 - Project2D.camera, self.y + 23

    def handle_collision(self, other, group):
        print('닿음')
        # if group == 'cat:air':
        #     game_world.game_world_clear()
        pass



class Enemy_cloakman:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/cloakman.png')
        self.x = x
        self.y = y
        self.dir = 1
        self.gravity = 0

        # 충돌 넘버
        self.crash_number = 0

    def update(self):
            # self.x += self.dir * SPEED_NORMAL_PPS * game_framework.frame_time
        if not self.gravity:
            self.y += self.dir * 1 * SPEED_NORMAL_PPS * game_framework.frame_time
            if self.y > 400:
                self.dir = -1
            elif self.y < 200:
                self.dir = 1
        if self.x - Project2D.camera < -100 or self.y < -100:
            game_world.remove_object(self)
            print('지우기 성공')
        self.y -= self.gravity

    def draw(self):
        if not self.gravity:
            self.image.clip_draw(0, 0, 83, 134, self.x - Project2D.camera, self.y)
        elif self.gravity:
            self.image.clip_draw(83, 0, 83, 134, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 41 - Project2D.camera, self.y - 67, self.x + 41 - Project2D.camera, self.y + 67

    def handle_collision(self, other, group):

        pass

    def handle_collision2(self, other, group):
        print('tkdatdawtaaawwatgwawa')
        if group == 'cat:cloakman':
            self.gravity = 3 * SPEED_NORMAL_PPS * game_framework.frame_time
        pass

# class Enemy_turtle_down:
#     def __init__(self, x, y, pos=False):  # 생성자
#         self.image = load_image('./res/enemy.png')
#         self.image2 = load_image('./res/enemyRe.png')
#         self.x = x
#         self.y = y
#         self.dir = -1
#         self.xPos = pos
#         self.gravity = 0
#
#         # 충돌 넘버
#         self.crash_number = 25
#
#     def update(self):
#
#         if self.x - Project2D.camera < -30 or self.y < -40:
#             game_world.remove_object(self)
#             print('지우기 성공')
#         if self.xPos <= Project2D.camera:
#             if self.gravity == 0:
#                 self.x += self.dir * SPEED_TURTLE_PPS * game_framework.frame_time
#
#             if self.x - Project2D.camera < -20 or self.y < -20:
#                 game_world.remove_object(self)
#                 print('지우기 성공')
#             self.y -= self.gravity
#             if self.gravity == 0:
#                 self.gravity = 2 * SPEED_TURTLE_PPS * game_framework.frame_time
#
#     def draw(self):
#
#         if self.dir == -1:
#             self.image.clip_draw(55, 8, 55, 76, self.x - Project2D.camera, self.y)
#         elif self.dir == 0 or self.dir == 3:
#             self.image.clip_draw(115, 51, 53, 58, self.x - Project2D.camera, self.y)
#
#
#     def get_bb(self):
#         return self.x - 27 - Project2D.camera, self.y - 38, self.x + 27 - Project2D.camera, self.y + 38
#
#     def handle_collision(self, other, group):
#         print('닿음')
#
#         pass
#
#     def handle_collision2(self, other, group):
#         if group == 'cat:turtle_down' and self.dir == 0:
#             self.dir = 3
#         if group == 'cat:turtle_down' and self.dir != 3:
#             self.y -= 9
#             self.dir = 0
#         if group == 'turtle_down:grass':
#             self.gravity = 0
#         pass