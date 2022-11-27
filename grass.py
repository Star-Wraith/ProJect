from pico2d import *

import item
from Project2D import *
import Project2D
import enemy
import death
import time
import flagpos

# def TTime():
#     time_second = time.time() + 10
#     while True:
#         if time.time() > time_second:
#             break
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

        self.break_Sound = load_music('./SE/brockbreak.mp3')

        self.cash = False


    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):
        if self.cash:

            game_world.remove_object(self)


        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)



        pass
    def handle_collision2(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        pass
#2 ? 블럭
class Block_QM:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/blockqm.PNG')
        self.image2 = load_image('./res/blockbrown.png')
        self.x = x + 20
        self.y = y + 20

        self.block_type = False

        # 충돌 넘버
        self.crash_number = 2

        self.brock_Sound = load_music('./SE/brockcoin.mp3')
        self.break_Sound = load_music('./SE/brockbreak.mp3')

        self.cash = False

    def draw(self):
        if not self.block_type:
            self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        if self.block_type:
            self.image2.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):

        if self.cash:

            game_world.remove_object(self)
        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        if other.y + 20 < self.y and other.x - 20 < self.x - Project2D.camera < other.x + 20:
            if not self.block_type:
                self.block_type += 1
                Project2D.item.append(item.Coin(self.x, self.y))
                game_world.add_objects(Project2D.item, 1)
                self.brock_Sound.set_volume(60)
                self.brock_Sound.play()



        pass
    def handle_collision2(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)


        pass

#3 투명 블럭
class Block_Shadow:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/blockbrown.PNG')
        self.x = x + 20
        self.y = y + 20

        self.block_type = False

        # 충돌 넘버
        self.crash_number = 3

        self.cash = False

        self.brock_Sound = load_music('./SE/brockcoin.mp3')
        self.break_Sound = load_music('./SE/brockbreak.mp3')



    def draw(self):
        if self.block_type:
            self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)

        draw_rectangle(*self.get_bb())


    def update(self):

        if Project2D.cat.y + 35 < self.y < Project2D.cat.y + 55 and Project2D.cat.x - 20 < self.x - Project2D.camera < Project2D.cat.x + 20:
            if not self.block_type:
                self.block_type += 1
                Project2D.item.append(item.Coin(self.x, self.y))
                game_world.add_objects(Project2D.item, 1)
                self.brock_Sound.set_volume(60)
                self.brock_Sound.play()


        if self.cash:

            game_world.remove_object(self)


        pass

    def get_bb(self):
        if not self.block_type:
            return 0, 0, 0, 0
        elif self.block_type:

            return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        if other.y + 20 < self.y and other.x - 20 < self.x - Project2D.camera < other.x + 20:
            if not self.block_type:
                self.block_type += 1
                Project2D.item.append(item.Coin(self.x, self.y))
                game_world.add_objects(Project2D.item, 1)
                self.brock_Sound.set_volume(60)
                self.brock_Sound.play()

        pass

    def handle_collision2(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)


        pass
#4 산
class Mountain:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.PNG')
        self.x = x + 20
        self.y = y + 91

        self.cash = False

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

        self.cash = False

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

        self.cash = False

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

#66 적 구름
class Cloud_enemy:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.PNG')
        self.x = x + 20
        self.y = y + 20

        self.cash = False

        # 충돌 넘버
        self.crash_number = 66

        self.block_type = False

    def draw(self):
        if self.block_type:
            self.image.clip_draw(303, 272, 138, 80, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 69 - Project2D.camera, self.y - 40, self.x + 69 - Project2D.camera, self.y + 40

    def handle_collision(self, other, group):
        self.block_type = True

        pass

    def handle_collision2(self, other, group):
        self.block_type = True

        pass



#7 저장 플래그
class Flag:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.PNG')
        self.x = x + 20
        self.y = y + 62

        self.cash = False


        # 충돌 넘버
        self.crash_number = 7

    def draw(self):
        self.image.clip_draw(0, 6, 67, 124, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        if flagpos.flag_live:
            game_world.remove_object(self)

        pass

    def get_bb(self):
        return self.x - 34 - Project2D.camera, self.y - 62, self.x + 34 - Project2D.camera, self.y + 62

    def handle_collision(self, other, group):
        flagpos.flag_live = True
        game_world.remove_object(self)
        pass

    def handle_collision2(self, other, group):
        game_world.remove_object(self)

        pass
#8 점프대
class JUMP_Bar:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/item.PNG')
        self.x = x + 20
        self.y = y + 24

        self.cash = False


        # 충돌 넘버
        self.crash_number = 8

    def draw(self):
        self.image.clip_draw(357, 8, 47, 49, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):

        if self.cash:

            game_world.remove_object(self)

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

        self.cash = False

        # 충돌 넘버
        self.crash_number = 9

        self.break_Sound = load_music('./SE/brockbreak.mp3')

    def draw(self):
        self.image.clip_draw(0, 0, 40, 80, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.speed
        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 40, self.x + 20 - Project2D.camera, self.y + 40

    def handle_collision(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        pass

    def handle_collision2(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        self.speed = 2 * RUN_SPEED_PPS * game_framework.frame_time

        pass

#21 빨간버섯 ? 블럭
class Block_RM:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/blockqm.PNG')
        self.image2 = load_image('./res/blockbrown.png')
        self.x = x + 20
        self.y = y + 20

        self.block_type = False
        self.cash = False

        self.brock_Sound = load_music('./SE/dokan.mp3')
        self.break_Sound = load_music('./SE/brockbreak.mp3')
        # 충돌 넘버
        self.crash_number = 21

    def draw(self):
        if not self.block_type:
            self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        if self.block_type:
            self.image2.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)

    def update(self):
        pass


    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)


        if other.y + 20 < self.y and other.x - 20 < self.x - Project2D.camera < other.x + 20:
            if not self.block_type:
                self.block_type += 1
                Project2D.item.append(item.Red_mushroom(self.x, self.y))
                game_world.add_objects(Project2D.item, 1)
                game_world.add_collision_group(Project2D.cat, Project2D.item, 'cat:item')
                self.brock_Sound.set_volume(60)
                self.brock_Sound.play()
        pass

    def handle_collision2(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)


        pass

#42 독버섯 ? 블럭
class Block_PM:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/blockqm.PNG')
        self.image2 = load_image('./res/blockbrown.png')
        self.x = x + 20
        self.y = y + 20

        self.cash = False


        self.block_type = False

        self.brock_Sound = load_music('./SE/dokan.mp3')
        self.break_Sound = load_music('./SE/brockbreak.mp3')

        # 충돌 넘버
        self.crash_number = 44

    def draw(self):
        if not self.block_type:
            self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        if self.block_type:
            self.image2.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)

        draw_rectangle(*self.get_bb())

    def update(self):
        pass


    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):
        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        if other.y + 20 < self.y and other.x - 20 < self.x - Project2D.camera < other.x + 20:
            if not self.block_type:
                self.block_type += 1
                Project2D.item.append(item.Poison_mushroom(self.x, self.y))
                game_world.add_objects(Project2D.item, 1)
                game_world.add_collision_group(Project2D.cat, Project2D.item, 'cat:item')
                self.brock_Sound.set_volume(60)
                self.brock_Sound.play()


        pass

    def handle_collision2(self, other, group):
        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        pass

#77 스타 ? 블럭
class Block_STAR:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/blockqm.PNG')
        self.image2 = load_image('./res/blockbrown.png')
        self.x = x + 20
        self.y = y + 20

        self.cash = False


        self.block_type = False

        self.brock_Sound = load_music('./SE/dokan.mp3')
        self.break_Sound = load_music('./SE/brockbreak.mp3')

        # 충돌 넘버
        self.crash_number = 77

    def draw(self):
        if not self.block_type:
            self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        if self.block_type:
            self.image2.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)

        draw_rectangle(*self.get_bb())

    def update(self):
        pass


    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):
        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        if other.y + 20 < self.y and other.x - 20 < self.x - Project2D.camera < other.x + 20:
            if not self.block_type:
                self.block_type += 1
                Project2D.item.append(item.Star(self.x, self.y))
                game_world.add_objects(Project2D.item, 1)
                game_world.add_collision_group(Project2D.cat, Project2D.item, 'cat:item')
                self.brock_Sound.set_volume(60)
                self.brock_Sound.play()


        pass

    def handle_collision2(self, other, group):
        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        pass


#12 스위치 있는 ? 블럭 # 수정 필요
class Block_Switch:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/blockqm.PNG')
        self.image2 = load_image('./res/blockbrown.png')
        self.x = x + 20
        self.y = y + 20

        self.cash = False


        self.block_type = False

        self.brock_Sound = load_music('./SE/dokan.mp3')
        self.break_Sound = load_music('./SE/brockbreak.mp3')

        # 충돌 넘버
        self.crash_number = 12

    def draw(self):
        if not self.block_type:
            self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        if self.block_type:
            self.image2.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)

        draw_rectangle(*self.get_bb())

    def update(self):

        if self.cash:

            game_world.remove_object(self)

        pass


    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):
        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        if other.y + 20 < self.y and other.x - 20 < self.x - Project2D.camera < other.x + 20:
            if not self.block_type:
                self.block_type += 1
                Project2D.item.append(item.Switch_small(self.x, self.y))
                game_world.add_objects(Project2D.item, 1)
                game_world.add_collision_group(Project2D.cat, Project2D.item, 'cat:item')
                self.brock_Sound.set_volume(60)
                self.brock_Sound.play()


        pass

    def handle_collision2(self, other, group):
        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        pass

#88 나무
class TREE:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.PNG')
        self.x = x + 20
        self.y = y + 58

        self.cash = False

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

        self.cash = False

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
            game_world.add_objects(Project2D.BOMB, 1)
            game_world.add_collision_group(Project2D.cat, Project2D.BOMB, 'cat:BOMB')

            self.COUNT += 1


        pass
    def handle_collision2(self, other, group):
        if self.COUNT == 0:
            game_world.remove_object(self)

            Project2D.Bye_bgm.set_volume(60)
            Project2D.Bye_bgm.repeat_play()

            Project2D.BOMB.append(enemy.Enemy_BOMB(6800, 800))
            game_world.add_objects(Project2D.BOMB, 1)
            game_world.add_collision_group(Project2D.cat, Project2D.BOMB, 'cat:BOMB')


            self.COUNT += 1
        pass

#17 코인 스위치
class SWITCH_COIN:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/switch.png')
        self.x = x + 20
        self.y = y + 40
        self.COUNT = 0

        self.cash = False

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
            game_world.add_objects(Project2D.BOMB, 1)
            game_world.add_collision_group(Project2D.cat, Project2D.BOMB, 'cat:BOMB')

            self.COUNT += 1


        pass
    def handle_collision2(self, other, group):
        if self.COUNT == 0:
            game_world.remove_object(self)

            Project2D.Bye_bgm.set_volume(60)
            Project2D.Bye_bgm.repeat_play()

            Project2D.BOMB.append(enemy.Enemy_BOMB(6800, 800))
            game_world.add_objects(Project2D.BOMB, 1)
            game_world.add_collision_group(Project2D.cat, Project2D.BOMB, 'cat:BOMB')


            self.COUNT += 1
        pass


#11 굴뚝
class Roof:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/roof.png')
        self.x = x + 20
        self.y = y + 80

        self.cash = False

        self.break_Sound = load_music('./SE/brockbreak.mp3')

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
        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)
        pass

    def handle_collision2(self, other, group):
        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        pass

#33 풀
class Leaf:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.png')
        self.x = x + 20
        self.y = y + 20

        self.cash = False

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

        self.cash = False

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

# 22: 적 결승봉
class Bong_Enemy:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/bong.png')
        self.image2 = load_image('./res/bongenemy.png')
        self.x = x + 20
        self.y = y + 220

        self.cash = False

        self.shadow = True

        # 충돌 넘버
        self.crash_number = 22
    def draw(self):
        if self.shadow:
            self.image.clip_draw(0, 0, 40, 440, self.x - Project2D.camera, self.y)
        else:
            self.image2.clip_draw(0, 0, 40, 440, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass


    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 220, self.x + 20 - Project2D.camera, self.y + 220

    def handle_collision(self, other, group):
        self.shadow = False
        pass
    def handle_collision2(self, other, group):

        pass

# 56: 결승문
class Clear_Door:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/haikei.png')
        self.x = x + 20
        self.y = y + 90

        self.cash = False

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

        self.cash = False

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

#51 네모 5개 블럭
class Grass_Ver2:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/block4.PNG')
        self.x = x + 20
        self.y = y + 20

        # 충돌 넘버
        self.crash_number = 1

        self.cash = False

        self.break_Sound = load_music('./SE/brockbreak.mp3')


    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):

        if self.cash:

            game_world.remove_object(self)

        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)



        pass
    def handle_collision2(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        pass


#19그냥 떨어지는 블럭
class Block_UP_DOWN:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/brocknormal.PNG')
        self.x = x + 20
        self.y = y + 20

        self.cash = False

        # 충돌 넘버
        self.crash_number = 19

        self.break_Sound = load_music('./SE/brockbreak.mp3')


    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())


    def update(self):
        if Project2D.camera >= 2800:
            self.y -= 2 * RUN_SPEED_PPS * game_framework.frame_time
        pass

    def get_bb(self):
        return self.x - 20 - Project2D.camera, self.y - 20, self.x + 20 - Project2D.camera, self.y + 20

    def handle_collision(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        pass

    def handle_collision2(self, other, group):

        if other.crash_number == 9999:
            if other.power_up:
                self.break_Sound.set_volume(60)
                self.break_Sound.play()
                game_world.remove_object(self)

        pass

#20 닭이닭
class Chicken_enemy:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/chicken.png')
        self.x = x + 20
        self.y = y + 110

        self.cash = False

        # 충돌 넘버
        self.crash_number = 20


    def draw(self):
        self.image.clip_draw(0, 0, 128, 220, self.x - Project2D.camera, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 64 - Project2D.camera, self.y - 110, self.x + 64 - Project2D.camera, self.y + 110

    def handle_collision(self, other, group):


        pass

    def handle_collision2(self, other, group):

        pass


#25 스위치
class SWITCH_Picachu:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('./res/switch.png')
        self.x = x + 20
        self.y = y + 40
        self.COUNT = 0

        self.cash = False

        # 충돌 넘버
        self.crash_number = 25

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
            Project2D.item.append(item.Pikachu(self.x, self.y))
            game_world.add_objects(Project2D.item, 1)
            game_world.add_collision_group(Project2D.cat, Project2D.item, 'cat:BOMB')

            self.COUNT += 1

        pass

    def handle_collision2(self, other, group):
        if self.COUNT == 0:
            game_world.remove_object(self)
            Project2D.item.append(item.Pikachu(self.x, self.y))
            game_world.add_objects(Project2D.item, 1)
            game_world.add_collision_group(Project2D.cat, Project2D.item, 'cat:BOMB')

            self.COUNT += 1
        pass