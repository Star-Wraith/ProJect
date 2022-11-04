import pico2d
from pico2d import *



RD, LD, RU, LU = range(4)
event_name = ['RD', 'LD', 'RU', 'LU']

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RD,
    (SDL_KEYDOWN, SDLK_a): LD,
    (SDL_KEYUP, SDLK_d): RU,
    (SDL_KEYUP, SDLK_a): LU
}

#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')


    @staticmethod
    def do(self):
        # self.frame = (self.frame + 1) % 2
        # self.timer -= 1
        # if self.timer == 0:
        #     self.add_event(TIMER)
        pass



    @staticmethod
    def draw(self):

        if self.face_dir == 1:
            self.image.clip_draw(49, 1, 46, 70, self.x, self.y)
        else:
            self.image2.clip_draw(186 - 46, 1, 46, 70, self.x, self.y)
        # else:
        #     self.image.clip_draw(self.frame * 46, 1, 46, 70, self.x, self.y)
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


    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir



    def do(self):
        self.move_delay += 1
        if self.move_delay % 50 == 0:
            self.frame = (self.frame + 1) % 2
        # self.frame = (self.frame + 1) % 2
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        pass

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 49, 1, 46, 70, self.x, self.y)
        elif self.dir == -1:
            self.image2.clip_draw(186 - 46 * self.frame, 1, 46, 70, self.x, self.y)
        pass




#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE}
}

class Cat:
    def __init__(self):
        self.image = load_image('players.PNG')
        self.image2 = load_image('players2.png')
        self.x = 50
        self.y = 117
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.move_delay = 0

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)



    def update(self):  # 소년의 행위 구현
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
        debug_print('PPPP')
        debug_print(f'Face Dir: {self.face_dir}, Dir: {self.dir}')

        # if self.dir == 1 or self.pos == 1 and self.dir == 0:
        #     self.image.clip_draw(self.frame * 49, 1, 46, 70, self.x, self.y)
        # elif self.dir == -1 or self.pos == 0 and self.dir == 0:
        #     self.image2.clip_draw(186 - 46 * self.frame, 1, 46, 70, self.x, self.y)
        # else:
        #     self.image.clip_draw(self.frame * 46, 1, 46, 70, self.x, self.y)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)