
from pico2d import *
import game_framework
import death
import game_world
import Project2D

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

        if self.face_dir == 1:
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

        if self.dir == 1:
            if self.jump_state == True or self.gravity != 0:
                self.image.clip_draw(2 * 49, 1, 46, 70, self.x, self.y)
            else:
                self.image.clip_draw(int(self.frame) * 49, 1, 46, 70, self.x, self.y)

        elif self.dir == -1:
            if  self.jump_state == True or self.gravity != 0:
                self.image2.clip_draw(186 - 46 * 2, 1, 46, 70, self.x, self.y)
            else:
                self.image2.clip_draw(186 - 46 * int(self.frame), 1, 46, 70, self.x, self.y)


        pass




#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN, JUMP: RUN},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, JUMP: RUN}
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
    def __init__(self):
        self.image = load_image('./res/players.PNG')
        self.image2 = load_image('./res/players2.png')
        self.x = 50
        self.y = 117
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.camera_x = 0 # 카메라 구현 대기중
        self.speed = 1
        # self.move_time = 3
        # self.move_delay = 1

        # 충돌 넘버
        self.crash_number = 9999

        self.jump = 0
        self.jump_flag = 0

        self.jump_Sound = load_music('./SE/jump.mp3')

        self.jump_state = False
        self.gravity = 2 * RUN_SPEED_PPS * game_framework.frame_time
        self.jump_s = 100
        self.jump_count = 0



        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        # 죽음
        self.death_pos = 0



    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(self.cur_state.__name__, ' ', event_name[event])
            self.cur_state.enter(self, event)




        # self.x += self.dir * 1
        # self.frame = self.frame % 2

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def JUMP(self): # jump 이쪽으로 옮길 필요 있음
        if self.jump_s > 0:
            self.y += self.jump_s * self.speed * RUN_SPEED_PPS * game_framework.frame_time/100
            self.jump_s -= RUN_SPEED_PPS * game_framework.frame_time/5
            self.gravity = 0
        elif self.jump_s <= 0:
            if self.jump_count == 0:
                self.gravity = self.speed * RUN_SPEED_PPS * game_framework.frame_time
                self.jump_count += 1
            else:
                if self.gravity == 0:
                    self.jump_state = False
                    self.jump_count = 0




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

        pass





    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 20, self.y - 40, self.x + 20, self.y + 40

    # def death_motion(self):
    #     self.death_pos = self.y + 100
    #     self.image.clip_draw(3 * 49, 1, 46, 70, self.x, self.y)
    #     delay(0.5)
    #     # while self.y <= self.death_pos:
    #     #     self.y += RUN_SPEED_PPS * game_framework.frame_time
    #     # while self.y >= -50:
    #     #     self.y -= RUN_SPEED_PPS * game_framework.frame_time


    def handle_collision(self, other, group):
        # Cat.death_motion(self)
        print(group)
        if group == 'cat:enemy':
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            game_framework.change_state(death)
        elif group == 'cat:rocket':
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            game_framework.change_state(death)
        elif group == 'cat:turtle':
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            game_framework.change_state(death)
        elif group == 'cat:air':
            Project2D.DEATH_SE.set_volume(60)
            Project2D.DEATH_SE.play()
            game_framework.change_state(death)
        elif group == 'cat:BOMB':
            game_framework.change_state(death)
        elif group == 'cat:grass': # 고쳐야한다 각 grass마다 크기가 달라서
            # 대충 이런식으로 바꿔나갈듯 (하나 하나씩 바꿔나가면 될듯)
            # if other.crash_number == 99:
            #     other.y += 100
            if self.x + 20 < other.x - Project2D.camera:
                self.x -= 5
            elif self.x - 20 > other.x - Project2D.camera:
                self.x += 5
            elif self.y + 20 < other.y:
                self.jump_s = 0
                # self.y -= 2
            elif self.y - 20 > other.y:
                self.y += 3
            # if self.x + other.get_bb()[0] - other.x + Project2D.camera + 10 < other.x - Project2D.camera:
            #     self.x -= 2
            # elif self.x - other.get_bb()[2] - other.x + Project2D.camera - 10 > other.x - Project2D.camera:
            #     self.x += 2
            # if self.y + other.get_bb()[1] - other.y < other.y:
            #     self.y -= 2
            # elif self.y + other.get_bb()[3] - other.y > other.y:
            #     self.y += 2
        pass

    def handle_collision2(self, other, group):
        # Cat.death_motion(self)
        if group == 'cat:enemy':
            self.y += 50
            Project2D.tok_se.set_volume(60)
            Project2D.tok_se.play()

        if group == 'cat:turtle':
            self.y += 50
            Project2D.tok_se.set_volume(60)
            Project2D.tok_se.play()
        if group == 'cat:grass':
            self.gravity = 0


        if group == 'cat:rocket':
            game_framework.change_state(death)
        if group == 'cat:air':
            game_framework.change_state(death)

        if group == 'cat:BOMB':
            game_framework.change_state(death)

        pass


    def camera_move(self):
        if self.x > 400:
            if self.camera_x <= 8800:
                # self.camera_x += 20 * RUN_SPEED_PPS * game_framework.frame_time
                self.camera_x += 1 * RUN_SPEED_PPS * game_framework.frame_time
                # print(self.camera_x)
        return self.camera_x

# 해야 될 것
# 적들 위치 선정 (완)
# 점프 고치기 (실패)
# 각종 상호작용들 (아주 약간)