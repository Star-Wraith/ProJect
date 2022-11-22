import pico2d
from pico2d import *
import game_framework
import game_world
import read_map
import title
import PAUSE
# 배경
from grass import Grass
from screen import Screen
# 플레이어(냥이)
from cat import Cat
# 적들
from enemy import Enemy_roket
from enemy import Enemy_normal
from enemy import Enemy_turtle
from enemy import Enemy_air

from enemy import Enemy_BOMB



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            cat.handle_event(event)




# initialization code
# open_canvas()
# screen = Screen()
# # dir = 0
# grass = Grass()  # 잔디 객체를 생성
# cat = Cat()
# count = 0
# # List Compreshension

# open_canvas()ddddddd
screen = None
# dir = 0
grass = list()  # 잔디 객체를 생성
cat = None
count = 0
running = True
rocket = list()
enemy = list()
enemy_turtle = list()
enemy_air = list()
stage_bgm = None
camera = None
BOMB = list()
Bye_bgm = None
tok_se = None
DEATH_SE = None
def enter():
    global cat, grass, running, screen, rocket, enemy, enemy_turtle, enemy_air, stage_bgm, BOMB, Bye_bgm, tok_se, DEATH_SE


    # clear
    enemy.clear()
    rocket.clear()
    enemy_turtle.clear()
    enemy_air.clear()
    grass.clear()
    BOMB.clear()
    Bye_bgm = load_music('./SE/Song.mp3')
    tok_se = load_music('./SE/koura.mp3')
    DEATH_SE = load_music('./SE/death.mp3')


    stage_bgm = load_music('./BGM/field.mp3')
    stage_bgm.set_volume(60)
    stage_bgm.repeat_play()
    # ------------ 시작 브금 ------------------
    cat = Cat()

    # enemy_air = Enemy_air(750, 300)
    read_map.map_read()
    grass = read_map.map_mapping

    # # clear
    # enemy.clear()
    # rocket.clear()
    # enemy_turtle.clear()
    # enemy_air.clear()


    # enemy
    # enemy = Enemy_normal(500, 104)
    enemy.append(Enemy_normal(500, 104))
    enemy.append(Enemy_normal(1300, 104))
    enemy.append(Enemy_normal(7980, 700, 7400))
    enemy.append(Enemy_normal(8100, 104))

    # rocket
    rocket.append(Enemy_roket(1960, 900, 1440))
    rocket.append(Enemy_roket(4000, 900, 3480))
    rocket.append(Enemy_roket(5040, 900, 4520))
    rocket.append(Enemy_roket(5120, 900, 4600))
    rocket.append(Enemy_roket(9200, 900, 8680))
    rocket.append(Enemy_roket(9300, 900, 8800))
    rocket.append(Enemy_roket(9360, 900, 8800))
    rocket.append(Enemy_roket(9420, 900, 8800))
    rocket.append(Enemy_roket(9480, 900, 8800))
    rocket.append(Enemy_roket(9540, 900, 8800))

    # Enemy_turtle
    enemy_turtle.append(Enemy_turtle(4840, 118))
    enemy_turtle.append(Enemy_turtle(4960, 118))
    enemy_turtle.append(Enemy_turtle(8140, 118))

    # Enemy_air
    enemy_air.append(Enemy_air(7300, 300, 6500))

    screen = Screen()
    # 2는 플레이어
    game_world.add_object(cat, 2)

    # 적이랑 블럭은 1

    game_world.add_objects(grass, 1)
    game_world.add_objects(enemy_air, 1)
    game_world.add_objects(rocket, 1)
    game_world.add_objects(enemy, 1)
    game_world.add_objects(enemy_turtle, 1)
    game_world.add_objects(BOMB, 1)
    # 배경
    game_world.add_object(screen, 0)

    game_world.add_collision_group(cat, enemy, 'cat:enemy')
    game_world.add_collision_group(cat, rocket, 'cat:rocket')
    game_world.add_collision_group(cat, enemy_turtle, 'cat:turtle')
    game_world.add_collision_group(cat, enemy_air, 'cat:air')
    game_world.add_collision_group(cat, grass, 'cat:grass')
    game_world.add_collision_group(cat, BOMB, 'cat:BOMB')
    game_world.add_collision_group(enemy, grass, 'enemy:grass')





def exit():
    global stage_bgm
    del stage_bgm
    game_world.clear()

def update():
    global camera, cat, grass
    camera = cat.camera_move()
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b) == 1:
            print('COLLISION by ', group)
            b.handle_collision(a, group)
            a.handle_collision(b, group)
        if collide(a, b) == 2:
            b.handle_collision2(a, group)
            a.handle_collision2(b, group)
def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass


def resume():

    pass

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    # 일반 적
    # if b == enemy[0] or b == enemy[1] or b == enemy[2]:
    #     print('됐어!')
    #     return True
    for i in range(len(enemy)):
        if b == enemy[i] and ba <= tb + 2 and ba > tb - 10:
            return 2
        elif b == enemy[i]:
            print('됐어!')
            return True
        # if b == enemy[i]:
        #     print('됐어!')
        #     return True

    # 로켓 적
    for i in range(len(rocket)):
        if b == rocket[i]:
            print('됐어!')
            return True

    # 터틀 적
    for i in range(len(enemy_turtle)):
        if b == enemy_turtle[i] and ba <= tb + 2 and ba > tb - 10:
            return 2
        elif b == enemy_turtle[i]:
            print('됐어!')
            return True
    # air 적
    for i in range(len(enemy_air)):
        if b == enemy_air[i]:
            print('됐어!')
            return True
    # 1 벽돌 블럭 충돌 처리
    if b.crash_number == 1 and a.crash_number == 9999:
        if a.y < b.y:
            return True
        elif a.y - 35 > b.y + 20:
            return 2
    # 2 ?블럭 충돌 처리
    if b.crash_number == 2 and a.crash_number == 9999:
        if a.y < b.y:
            return True
        elif a.y - 35 > b.y + 20:
            return 2
    # 3 투명 블럭 충돌 처리
    if b.crash_number == 3 and a.crash_number == 9999:
        if a.y < b.y:
            return True
        elif a.y - 35 > b.y + 20:
            return 2
    # 7 플래그 충돌 처리
    # if b.crash_number == 7 and a.crash_number == 9999:
    #     if a.y < b.y:
    #         return True
    #     elif a.y - 35 > b.y + 2:
    #         return 2
    # 8 점프대 충돌 처리
    if b.crash_number == 8 and a.crash_number == 9999:
        if a.y < b.y:
            return True
        elif a.y - 35 > b.y + 20:
            return 2
    # 9 떨어지는 블럭 충돌 처리
    if b.crash_number == 9 and a.crash_number == 9999:
        if a.y < b.y:
            return True
        elif a.y - 35 > b.y + 40:
            return 2

    # 21 빨간 버섯 ?블럭 충돌 처리
    if b.crash_number == 21 and a.crash_number == 9999:
        if a.y < b.y:
            return True
        elif a.y - 35 > b.y + 20:
            return 2
    # 42 독 버섯 ?블럭 충돌 처리
    if b.crash_number == 42 and a.crash_number == 9999:
        if a.y < b.y:
            return True
        elif a.y - 35 > b.y + 20:
            return 2
    # 11 굴뚝 충돌 처리
    if b.crash_number == 11 and a.crash_number == 9999:
        if a.y < b.y:
            return True
        elif a.y - 35 > b.y + 80:
            return 2

    # # 55 결승 봉 충돌 처리
    # if b.crash_number == 11 and a.crash_number == 9999:
    #     if a.y < b.y:
    #         return True
    #     elif a.y - 35 > b.y + 220:
    #         return 2

    # 99 올라가는 블럭 충돌 처리
    if b.crash_number == 99 and a.crash_number == 9999:
        if a.y < b.y:
            return True
        elif a.y - 35 > b.y + 20:
            return 2



    if a.crash_number == 0 and b.crash_number == 1:
        if a.y < b.y:
            return True
        elif a.y - 38 > b.y:
            return 2


    return True






def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()



if __name__ == '__main__': # 만약 단독 실행 상태이면,
    test_self()
