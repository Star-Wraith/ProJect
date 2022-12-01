from pico2d import *
import game_framework
import Project2D
import game_world
import title
image = None
font = None
DEATH = 3 # 목숨
DEATH_COUNT = 0 # 죽은 횟수
def enter():
    global image, DEATH, font, SE, DEATH_COUNT, wait_time
    wait_time = 0
    DEATH -= 1
    DEATH_COUNT += 1
    if DEATH < -99:
        DEATH = -99
    image = load_image('./res/death.png')
    font = load_font('./res/ENCR10B.TTF', 40)


    pass

def exit():
    global image
    del image
    game_world.clear()

    pass





def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(Project2D)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def draw():
    clear_canvas()
    image.draw(400, 300)
    font.draw(450, 300, f'{DEATH}', (255, 255, 255)) # 죽은 횟수 표시
    # font.draw(220, 100, 'press space bar', (255, 255, 0))
    update_canvas()
    pass
def update():

    pass


def pause():
    pass

def resume():

    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()



if __name__ == '__main__': # 만약 단독 실행 상태이면,
    test_self()