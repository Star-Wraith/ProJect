

from pico2d import *

class Screen:
    def __init__(self):
        self.image = load_image('batang.png')

    def draw(self):
        self.image.draw(400, 300)

class Grass:
    def __init__(self):  # 생성자
        self.image = load_image('brocknormal.PNG')
        self.x = 15
        self.y = 75


    def draw(self):
        while self.y > 0:
            self.x = 15
            while self.x < 800:
                self.image.clip_draw(0, 0, 30, 30, self.x, self.y)
                self.x += 30
            self.y -= 30
        self.x = 15
        self.y = 75




class Cat:
    def __init__(self):
        self.image = load_image('players.PNG')
        self.image2 = load_image('players2.png')
        self.x = 50
        self.y = 117
        self.frame = 0
        self.pos = 1
        self.dir = 0
        self.dir2 = 0


    def update(self):  # 소년의 행위 구현
        global running
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_a:
                    self.dir = -1


                elif event.key == SDLK_d:
                    self.dir = 1


                # elif event.key == SDLK_w:
                #     self.dir2 += 1


                elif event.key == SDLK_ESCAPE:
                    running = False
            elif event.type == SDL_KEYUP:
                if event.key == SDLK_a:
                    self.dir = 0

                    self.pos = 0


                elif event.key == SDLK_d:
                    self.dir = 0

                    self.pos = 1


        # self.x += dir * 5
        self.x += self.dir * 5
        # self.y += self.dir2 * 5
        self.frame = self.frame % 2

    def draw(self):
        if self.dir == 1 or  self.pos == 1 and self.dir == 0:
            self.image.clip_draw(self.frame * 33, 1, 31, 53, self.x, self.y)
        elif self.dir == -1 or self.pos == 0 and self.dir == 0:
            self.image2.clip_draw(124 - 31 * self.frame, 1, 31, 53, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 33, 1, 31, 53, self.x, self.y)








# def handle_events():
#     global running
#     global dir
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_KEYDOWN:
#             if event.key == SDLK_a:
#                 dir -= 1
#             elif event.key == SDLK_d:
#                 dir += 1
#             elif event.key == SDLK_ESCAPE:
#                 running = False
#         elif event.type == SDL_KEYUP:
#             if event.key == SDLK_a:
#                 dir += 1
#             elif event.key == SDLK_d:
#                 dir -= 1




# initialization code
open_canvas()
screen = Screen()
# dir = 0
grass = Grass()  # 잔디 객체를 생성
boy = Cat()
count = 0
# List Compreshension


running = True

# game main loop code
while running:
    # handle_events()  # 키 입력 받아들이는 처리..'
    # Game logic
    # grass 에 대한 상호작용.
    # boy.update()
    # boy.update() # 소년의 상호작용.

    # Game drawing
    clear_canvas()
    screen.draw()
    grass.draw()
    boy.update()

    boy.draw()
    if dir != 0:
        count += 1
        if count % 10 == 0:
            boy.frame += 1

    update_canvas()

    get_events()
    # boy.draw()


    delay(0.01)
