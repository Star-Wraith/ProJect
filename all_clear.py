from pico2d import *
import game_framework
import Project2D
import game_world
import title
import death
S = None
A = None
B = None
C = None
D = None

F = None


font = None
sound = None

def enter():
    global font, sound, S, A, B, C, D, F
    S = load_image('./res/S.png')
    A = load_image('./res/A.png')
    B = load_image('./res/B.png')
    C = load_image('./res/C.png')
    D = load_image('./res/D.png')
    F = load_image('./res/F.png')

    sound = load_music('./SE/allclear.mp3')
    sound.set_volume(60)
    sound.play()

    font = load_font('./res/ENCR10B.TTF', 120)


    pass

def exit():
    global S, A, B, C, D, F
    del S, A, B, C, D, F
    game_world.clear()

    pass





def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def draw():
    clear_canvas()
    if death.DEATH_COUNT == 0:
        S.draw(400, 300)
    elif 0 < death.DEATH_COUNT <= 20:
        A.draw(400, 300)
        font.draw(220, 450, f'{death.DEATH_COUNT}', (0, 0, 0))
    elif 20 < death.DEATH_COUNT <= 50:
        B.draw(400, 300)
        font.draw(220, 445, f'{death.DEATH_COUNT}', (0, 0, 0))
    elif 50 < death.DEATH_COUNT <= 100:
        C.draw(400, 300)
        font.draw(160, 445, f'{death.DEATH_COUNT}', (0, 0, 0))
    elif 100 < death.DEATH_COUNT <= 150:
        D.draw(400, 300)
        font.draw(120, 445, f'{death.DEATH_COUNT}', (0, 0, 0))
    elif 150 < death.DEATH_COUNT:
        F.draw(400, 300)
        font.draw(260, 505, f'{death.DEATH_COUNT}', (0, 0, 0))



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