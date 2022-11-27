
from pico2d import *
import game_framework
import death
import game_world
import Project2D
import flagpos
import all_clear

RD, LD, RU, LU, JUMP = range(5)
event_name = ['RD', 'LD', 'RU', 'LU', 'JUMP']

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RD,
    (SDL_KEYDOWN, SDLK_a): LD,
    (SDL_KEYUP, SDLK_d): RU,
    (SDL_KEYUP, SDLK_a): LU,
    (SDL_KEYDOWN, SDLK_j): JUMP,
    (SDL_KEYDOWN, SDLK_w): JUMP
}

#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000
        if event == JUMP and self.jump_state == False:
            # self.jump_flag = 1
            # self.jump = self.y

            self.jump_Sound.set_volume(60)
            self.jump_Sound.play()

            self.jump_state = True
            self.jump_s = 100
            self.gravity = RUN_SPEED_PPS * game_framework.frame_time


    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
        self.gravity = RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def do(self):
        # self.frame = (self.frame + 1) % 2
        # self.timer -= 1
        # if self.timer == 0:
        #     self.add_event(TIMER)
        if self.jump_state == True:
            Cat.JUMP(self)
        # if self.jump_flag == 1:
        #     if self.y < self.jump + 400:
        #         self.y += 1
        #     else:
        #         self.jump_flag = 2
        # if self.jump_flag == 2:
        #     if self.y > self.jump:
        #         self.y -= 1
        #     else:
        #         self.jump_flag = 0

        self.y -= self.gravity

        if self.death_cat:
            Cat.death(self)

        pass



    @staticmethod
    def draw(self):
        # if self.face_dir == 1:
        #     if self.jump_flag == 1 or self.jump_flag == 2:
        #         self.image.clip_draw(2 * 49, 1, 46, 70, self.x, self.y)
        #     else:
        #         self.image.clip_draw(49, 1, 46, 70, self.x, self.y)
        #
        # else:
        #     if self.jump_flag == 1 or self.jump_flag == 2:
        #         self.image2.clip_draw(186 - 46 * 2, 1, 46, 70, self.x, self.y)
        #     else:
        #         self.image2.clip_draw(186 - 46, 1, 46, 70, self.x, self.y)

        if self.death_cat:
            self.image.clip_draw(3 * 48, 1, 46, 70, self.x, self.y)
        elif self.power_up:
            self.image_power.clip_draw(0, 0, 128, 220, self.x, self.y)
        elif self.face_dir == 1:
            if self.jump_state == True:
                self.image.clip_draw(2 * 49, 1, 46, 70, self.x, self.y)
            else:
                self.image.clip_draw(49, 1, 46, 70, self.x, self.y)
        else:
            if self.jump_state == True:
                self.image2.clip_draw(186 - 46 * 2, 1, 46, 70, self.x, self.y)
            else:
                self.image2.clip_draw(186 - 46, 1, 46, 70, self.x, self.y)


        pass

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        elif event == JUMP and self.jump_state == False:

                self.jump_Sound.set_volume(60)
                self.jump_Sound.play()
                #
                #
                # self.jump_flag = 1
                # self.jump = self.y
                self.jump_s = 100
                self.jump_state = True




    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir
        self.gravity = RUN_SPEED_PPS * game_framework.frame_time




        # self.move_time = 3
        # self.move_delay = 1



    def do(self):

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        # self.move_delay += 1
        # if self.move_delay % 10 == 0 and self.move_time > 1:
        #     self.move_time -= 1


        # self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time/self.move_time
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 400 and self.camera_x <= 8800:
            Cat.camera_move(self)
            # self.camera_x += RUN_SPEED_PPS * game_framework.frame_time
            # game_framework.camera = self.camera_x
            self.x = 400
        if self.x < 10:
            self.x = 10

        if self.jump_state == True:
            Cat.JUMP(self)

        if self.death_cat:
            print("여기!!")
            Cat.death(self)

        if self.dir != 0:
            self.face_dir_run = self.dir







        #
        # if self.jump_flag == 1:
        #     if self.y < self.jump + 200:
        #         self.y += 1
        #     else:
        #         self.jump_flag = 2
        # if self.jump_flag == 2:
        #     if self.y > self.jump:
        #         self.y -= 1
        #     else:
        #         self.jump_flag = 0

        self.y -= self.gravity

        if self.jump_state == False:
            self.gravity = RUN_SPEED_PPS * game_framework.frame_time


        # self.x += self.dir
        # self.x = clamp(0, self.x, 800)
        # if self.gravity == 0 and self.jump_flag == 0:
        #     self.gravity = 2 * RUN_SPEED_PPS * game_framework.frame_time
        pass

    def draw(self):
    #     if self.dir == 1:
    #         if self.jump_flag == 1 or self.jump_flag == 2:
    #             self.image.clip_draw(2 * 49, 1, 46, 70, self.x, self.y)
    #         else:
    #             self.image.clip_draw(int(self.frame) * 49, 1, 46, 70, self.x, self.y)
    #
    #     elif self.dir == -1:
    #         if self.jump_flag == 1 or self.jump_flag == 2:
    #             self.image2.clip_draw(186 - 46 * 2, 1, 46, 70, self.x, self.y)
    #         else:
    #             self.image2.clip_draw(186 - 46 * int(self.frame), 1, 46, 70, self.x, self.y)




        if self.death_cat:
            self.image.clip_draw(3 * 48, 1, 46, 70, self.x, self.y)
        elif self.power_up:
            self.image_power.clip_draw(0, 0, 128, 220, self.x, self.y)
        elif self.face_dir_run == 1:
            if self.jump_state == True or self.gravity != 0:
                self.image.clip_draw(2 * 49, 1, 46, 70, self.x, self.y)
            else:
                self.image.clip_draw(int(self.frame) * 49, 1, 46, 70, self.x, self.y)
        elif self.face_dir_run:
            if  self.jump_state == True or self.gravity != 0:
                self.image2.clip_draw(186 - 46 * 2, 1, 46, 70, self.x, self.y)
            else:
                self.image2.clip_draw(186 - 46 * int(self.frame), 1, 46, 70, self.x, self.y)


        pass




#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE}
}

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 30 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



class Cat:
    def __init__(self, x=50, y=117, camera_pos=0):
        self.image = load_image('./res/players.PNG')
        self.image2 = load_image('./res/players2.png')
        self.image_power = load_image('./res/powerup.png')
        self.x = x
        self.y = y
        self.frame = 0
        self.face_dir = 1
        self.face_dir_run = self.face_dir
        self.dir = 0
        self.camera_x = camera_pos # 카메라 구현 대기중
        self.speed = 1
        # self.move_time = 3
        # self.move_delay = 1

        # 충돌 넘버
        self.crash_number = 9999

        self.jump = 0
        self.jump_flag = 0

        self.jump_Sound = load_music('./SE/jump.mp3')
        self.Star_Sound = load_music('./SE/powerup.mp3')
        self.clear_Sound = load_music('./SE/goal.mp3')
        self.brock_Sound = load_music('./SE/brockcoin.mp3')

        self.jump_state = False
        self.gravity = 2 * RUN_SPEED_PPS * game_framework.frame_time
        self.jump_s = 100
        self.jump_count = 0

        self.power_up = False   # 빨간 버섯 충돌
        self.death_cat = False




        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        # 죽음
        self.death_pos = 0
        self.yPlus = 0

        # 클리어 대기시간
        self.clear_pos = 0
        self.clear_time = 0



    def update(self):
        # self.cur_state.do(self)

        if self.death_cat:
            Cat.death(self)
        elif self.clear_pos:
            Cat.stage_clear(self)
        else:
            self.cur_state.do(self)
            if self.event_que:
                event = self.event_que.pop()
                self.cur_state.exit(self, event)
                try:
                    self.cur_state = next_state[self.cur_state][event]
                except KeyError:
                    print(self.cur_state.__name__, ' ', event_name[event])
                self.cur_state.enter(self, event)

        if self.y > 1200:

            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            self.death_cat = True
            # game_framework.change_state(death)
            # game_world.game_world_clear()
        elif self.y < -220 and self.death_cat == False:
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            self.death_cat = True


        # self.x += self.dir * 1
        # self.frame = self.frame % 2
    def death(self): # 여기 하는중
        if self.yPlus < 200:
            # self.power_up = False
            self.y += RUN_SPEED_PPS * game_framework.frame_time
            self.yPlus += RUN_SPEED_PPS * game_framework.frame_time
        elif self.y > - 400:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time
        else:
            game_framework.change_state(death)
            game_world.game_world_clear()

    def stage_clear(self):
        if self.y > 160:
            self.y -= RUN_SPEED_PPS * game_framework.frame_time/2
        elif self.clear_time < 1000 * game_framework.frame_time:
            self.clear_time += game_framework.frame_time
        else:
            flagpos.stage_number += 1
            flagpos.flag_camera_pos = None
            flagpos.flag_pos_x = None
            flagpos.flag_pos_y = None
            flagpos.flag_live = False
            game_world.game_world_clear()
            if flagpos.stage_number <= 2:
                game_framework.change_state(death) # 2 Stage로 변경
            else:
                game_framework.change_state(all_clear)




    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def JUMP(self):
        if self.jump_s > 0:
            self.y += self.jump_s * self.speed * RUN_SPEED_PPS * game_framework.frame_time/100
            self.jump_s -= RUN_SPEED_PPS * game_framework.frame_time/5
            self.gravity = 0
        elif self.jump_s <= 0:
            if not self.jump_count:
                self.gravity = self.speed * RUN_SPEED_PPS * game_framework.frame_time
                self.jump_count = True
            else:
                if self.gravity == 0:
                    self.jump_state = False
                    self.jump_count = False


        pass





    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


    def get_bb(self):
        if self.power_up:
            return self.x - 64, self.y - 110, self.x + 64, self.y + 110
        if self.death_cat:
            return 1000, 1000, 1000, 1000
        return self.x - 20, self.y - 40, self.x + 20, self.y + 40



    def handle_collision(self, other, group):
        # Cat.death_motion(self)
        print(group)
        if group == 'cat:enemy':
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            self.death_cat = True
        elif group == 'cat:rocket':
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            self.death_cat = True
        elif group == 'cat:turtle':
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            self.death_cat = True
        elif group == 'cat:air':
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            self.death_cat = True
        elif group == 'cat:fireball':
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            self.death_cat = True
        elif group == 'cat:BOMB':
            self.death_cat = True
        elif group == 'cat:cloakman':
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            self.death_cat = True

        elif group == 'cat:grass':
            if self.x + 20 < other.x - Project2D.camera:
                self.x -= 5
            elif self.x - 20 > other.x - Project2D.camera:
                self.x += 5
            elif self.y + 20 < other.y:
                self.jump_s = 0
                # self.y -= 2
            elif self.y - 20 > other.y:
                self.y += 3

            if other.crash_number == 7:
                flagpos.flag_pos_x, flagpos.flag_pos_y, flagpos.flag_camera_pos = self.x + Project2D.camera, self.y, self.camera_x

            elif other.crash_number == 55:
                self.clear_Sound.set_volume(60)
                self.clear_Sound.play()
                self.clear_pos = True
                pass
            elif other.crash_number == 66:
                Project2D.DEATH_SE.set_volume(60)
                Project2D.DEATH_SE.play()
                self.death_cat = True
                pass
            elif other.crash_number == 20:
                Project2D.DEATH_SE.set_volume(60)
                Project2D.DEATH_SE.play()
                self.death_cat = True
                pass
            elif other.crash_number == 19:
                Project2D.DEATH_SE.set_volume(60)
                Project2D.DEATH_SE.play()
                self.death_cat = True
            elif other.crash_number == 22:
                Project2D.Bye_bgm.set_volume(60)
                Project2D.Bye_bgm.repeat_play()
                self.death_cat = True
                pass
        elif group == 'cat:item':
            if other.crash_number == 20:
                self.power_up = True
                self.Star_Sound.set_volume(60)
                self.Star_Sound.play()
            if other.crash_number == 43:
                Project2D.DEATH_SE.set_volume(60)
                Project2D.DEATH_SE.play()
                self.death_cat = True
            if other.crash_number == 76:
                self.Star_Sound.set_volume(60)
                self.Star_Sound.play()
                self.death_cat = True
            if other.crash_number == 13:
                for i in range(len(Project2D.grass)):
                    Project2D.grass[i].cash = True

                self.brock_Sound.set_volume(60)
                self.brock_Sound.play()




        pass

    def handle_collision2(self, other, group):
        if group == 'cat:enemy':
            self.y += 50
            Project2D.tok_se.set_volume(60)
            Project2D.tok_se.play()

        if group == 'cat:turtle':
            self.y += 50
            Project2D.tok_se.set_volume(60)
            Project2D.tok_se.play()
        if group == 'cat:turtle_down':
            self.y += 50
            Project2D.tok_se.set_volume(60)
            Project2D.tok_se.play()
        if group == 'cat:cloakman':
            self.y += 200
            Project2D.tok_se.set_volume(60)
            Project2D.tok_se.play()

        if group == 'cat:grass':
            if not self.power_up:
                self.gravity = 0

        if other.crash_number == 66:
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            self.death_cat = True
            pass

        if group == 'cat:rocket':
            self.death_cat = True

        if group == 'cat:air':
            self.death_cat = True

        if group == 'cat:fireball':
            self.death_cat = True

        if group == 'cat:BOMB':
            self.death_cat = True

        pass


    def camera_move(self):
        if self.x > 400:
            if self.camera_x <= 8800:
                # self.camera_x += 20 * RUN_SPEED_PPS * game_framework.frame_time
                self.camera_x += 1 * RUN_SPEED_PPS * game_framework.frame_time
                # print(self.camera_x)
        return self.camera_x
