import pico2d
from pico2d import *
import game_framework
import title
import PAUSE

class Screen:
    def __init__(self):
        self.image = load_image('batang.png')

    def draw(self):
        self.image.draw(400, 300)

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




class Cat:
    def __init__(self):
        self.image = load_image('players.PNG')
        self.image2 = load_image('players2.png')
        self.x = 50
        self.y = 117
        self.frame = 0
        self.pos = 1
        self.dir = 0
        # self.dir2 = 0


    def update(self):  # 소년의 행위 구현
        # global running
        # events = get_events()
        # for event in events:
        #     if event.type == SDL_QUIT:
        #         game_framework.quit()
        #     elif event.type == SDL_KEYDOWN:
        #         if event.key == SDLK_a:
        #             self.dir = -1
        #
        #
        #         elif event.key == SDLK_d:
        #             self.dir = 1
        #
        #
        #         # elif event.key == SDLK_w:
        #         #     self.dir2 += 1
        #         elif event.key == SDLK_p:
        #             game_framework.push_state(pause)
        #
        #
        #         elif event.key == SDLK_ESCAPE:
        #             game_framework.quit()
        #     elif event.type == SDL_KEYUP:
        #         if event.key == SDLK_a:
        #             self.dir = 0
        #
        #             self.pos = 0
        #
        #
        #         elif event.key == SDLK_d:
        #             self.dir = 0
        #
        #             self.pos = 1


        # self.x += dir * 5
        self.x += self.dir * 1
        # self.y += self.dir2 * 5
        self.frame = self.frame % 2

    def draw(self):
        if self.dir == 1 or self.pos == 1 and self.dir == 0:
            self.image.clip_draw(self.frame * 49, 1, 46, 70, self.x, self.y)
        elif self.dir == -1 or self.pos == 0 and self.dir == 0:
            self.image2.clip_draw(186 - 46 * self.frame, 1, 46, 70, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 46, 1, 46, 70, self.x, self.y)



class Enemy_roket:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('enemy.png')
        self.image2 = load_image('enemyRe.png')
        self.x = x
        self.y = y
        self.y_first = self.y
        self.dir = 1
        self.count = 0

    def update(self):
        # while self.y > 0:
        #     self.count += 1
        #     if count % 10 == 0:
        #         self.y -= 1
        self.y += self.dir * 1
        if self.y > 600:
            self.dir = -1
            self.y = 600
        elif self.y < 120:
            self.dir = 1
            self.y = 120
    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(229, 0, 55, 76, self.x, self.y)

        else:
            self.image.clip_draw(169, 0, 55, 76, self.x, self.y)

class Enemy_normal:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('enemy.png')
        self.image2 = load_image('enemyRe.png')
        self.x = x
        self.y = y
        self.dir = 1
        self.x_max = self.x + 100

    def update(self):
        # while self.y > 0:
        #     self.count += 1
        #     if count % 10 == 0:
        #         self.y -= 1
        self.x += self.dir * 1/3
        if self.x > self.x_max:
            self.dir = -1
            self.x = self.x_max
        elif self.x < self.x_max - 200:
            self.dir = 1
            self.x = self.x_max - 200
    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(397, 27, 55, 49, self.x, self.y)
        else:
            self.image.clip_draw(0, 27, 55, 49, self.x, self.y)

class Enemy_turtle:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('enemy.png')
        self.image2 = load_image('enemyRe.png')
        self.x = x
        self.y = y
        self.dir = 1
        self.x_max = self.x + 100

    def update(self):
        # while self.y > 0:
        #     self.count += 1
        #     if count % 10 == 0:
        #         self.y -= 1
        self.x += self.dir * 1/3
        if self.x > self.x_max:
            self.dir = -1
            self.x = self.x_max
        elif self.x < self.x_max - 200:
            self.dir = 1
            self.x = self.x_max - 200
    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(340, 8, 55, 76, self.x, self.y)
        else:
            self.image.clip_draw(55, 8, 55, 76, self.x, self.y)


class Enemy_air:
    def __init__(self, x, y):  # 생성자
        self.image = load_image('enemy.png')
        self.image2 = load_image('enemyRe.png')
        self.x = x
        self.y = y
        self.dir = 1


    def update(self):
        # while self.y > 0:
        #     self.count += 1
        #     if count % 10 == 0:
        #         self.y -= 1
        self.x += self.dir * 1/3
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0

    def draw(self):
        if self.dir == 1:
            self.image2.clip_draw(54, 20, 60, 56, self.x, self.y)
        else:
            self.image.clip_draw(340, 20, 58, 56, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                cat.dir = -1


            elif event.key == SDLK_d:
                cat.dir = 1


            # elif event.key == SDLK_w:
            #     cat.dir2 += 1

            elif event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_p:
                game_framework.push_state(PAUSE)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                cat.dir = 0

                cat.pos = 0


            elif event.key == SDLK_d:
                cat.dir = 0
                cat.pos = 1




# initialization code
# open_canvas()
# screen = Screen()
# # dir = 0
# grass = Grass()  # 잔디 객체를 생성
# cat = Cat()
# count = 0
# # List Compreshension

# open_canvas()
screen = None
# dir = 0
grass = None  # 잔디 객체를 생성
cat = None
count = 0
running = True
rocket = None
enemy = None
enemy_turtle = None
enemy_air = None
def enter():
    global cat, grass, running, screen, rocket, enemy, enemy_turtle, enemy_air
    cat = Cat()
    rocket = Enemy_roket(300, 400)
    enemy = Enemy_normal(500, 104)
    enemy_turtle = Enemy_turtle(300, 118)
    enemy_air = Enemy_air(750, 300)
    grass = Grass()
    screen = Screen()
    running = True

def exit():
    global cat, grass, screen, rocket, enemy, enemy_turtle, enemy_air
    del cat
    del rocket
    del enemy
    del enemy_turtle
    del enemy_air
    del grass
    del screen

def update():
    cat.update()
    rocket.update()
    enemy.update()
    enemy_turtle.update()
    enemy_air.update()

def draw_world():
    screen.draw()
    grass.draw()
    cat.draw()
    rocket.draw()
    enemy.draw()
    enemy_turtle.draw()
    enemy_air.draw()

def draw():
    # 게임 월드 렌더링
    global count
    clear_canvas()
    draw_world()
    screen.draw()
    grass.draw()
    cat.draw()
    rocket.draw()
    enemy.draw()
    enemy_turtle.draw()
    enemy_air.draw()
    if cat.dir != 0:
        count += 1
        if count % 100 == 0:
            cat.frame += 1
    update_canvas()

def pause():
    pass


def resume():

    pass

# game main loop code
# while running:
#     handle_events()  # 키 입력 받아들이는 처리..'
#     # Game logic
#     # grass 에 대한 상호작용.
#     # boy.update()
#     # boy.update() # 소년의 상호작용.
#
#     # Game drawing
#     clear_canvas()
#     screen.draw()
#     grass.draw()
#     cat.update()
#
#     cat.draw()
#     if cat.dir != 0:
#         count += 1
#         if count % 10 == 0:
#             cat.frame += 1
#
#     update_canvas()
#
#     get_events()
#     # boy.draw()
#
#
#     delay(0.01)

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()



if __name__ == '__main__': # 만약 단독 실행 상태이면,
    test_self()
