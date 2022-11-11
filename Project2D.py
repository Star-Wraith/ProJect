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
from enemy1 import Enemy_roket
from enemy1 import Enemy_normal
from enemy1 import Enemy_turtle
from enemy1 import Enemy_air





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
stage_bgm = None

camera = None
def enter():
    global cat, grass, running, screen, rocket, enemy, enemy_turtle, enemy_air, stage_bgm


    stage_bgm = load_music('./BGM/field.mp3')
    stage_bgm.set_volume(60)
    stage_bgm.repeat_play()
    # ------------ 시작 브금 ------------------
    cat = Cat()
    rocket = Enemy_roket(300, 400)
    enemy = Enemy_normal(500, 104)
    enemy_turtle = Enemy_turtle(300, 118)
    enemy_air = Enemy_air(750, 300)
    read_map.map_read()
    grass = read_map.map_mapping
    screen = Screen()
    # 2는 플레이어
    game_world.add_object(cat, 2)
    # 적이랑 블럭은 1
    game_world.add_object(rocket, 1)
    game_world.add_object(enemy, 1)
    game_world.add_object(enemy_turtle, 1)
    game_world.add_object(enemy_air, 1)
    game_world.add_objects(grass, 1)
    # 배경 0
    game_world.add_object(screen, 0)

    game_world.add_collision_group(cat, enemy, 'cat:enemy')
    game_world.add_collision_group(cat, grass, 'cat:grass')



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

    if b == enemy:
        return True
    if a.y > b.y:
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
