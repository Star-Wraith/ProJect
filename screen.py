from pico2d import *

class Screen:
    def __init__(self):
        self.image = load_image('batang.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass