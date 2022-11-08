from pico2d import *
import game_framework
import Project2D

image = None

def enter():
    global image
    image = load_image('./res/title.png')
    pass

def exit():
    global image
    del image

    pass





def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(Project2D)
def draw():
    clear_canvas()
    image.draw(400, 300)
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
