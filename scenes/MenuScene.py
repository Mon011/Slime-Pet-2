from pyray import *
from .Scene import Scene

class MenuScene(Scene):
    background_image: Image 
    background: Texture2D

    def __init__(self):
        self.background_image = load_image("assets/background.png")
        self.background = load_texture_from_image(self.background_image)
        unload_image(self.background_image)

    def render(self):
        begin_drawing()
        clear_background(WHITE)

        draw_texture_ex(self.background, [0, 0], 0, 1, WHITE)
        end_drawing()

        unload_texture(self.background)