from pyray import *
from .Scene import Scene
from config import *
from components import draw_button, singleton, GameState

class CreditsScene(Scene):
    BANNER_SCALE = 0.8
    BUTTON_WIDTH = 250
    BUTTON_HEIGHT = 80
    BUTTON_MARGIN = 30

    background_image: Image 
    background: Texture2D
    banner_image: Image
    banner: Texture2D
    exit_button: Rectangle

    def load(self):
        self.background_image = load_image("assets/background.png")
        self.background = load_texture_from_image(self.background_image)
        self.banner_image = load_image("assets/banner.png")
        self.banner = load_texture_from_image(self.banner_image)
        self.exit_button = Rectangle(SCREEN_WIDTH / 2 - self.BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + self.BUTTON_HEIGHT * 2 + self.BUTTON_MARGIN * 2, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)

        unload_image(self.background_image)
        unload_image(self.banner_image)

    def render(self):
        begin_drawing()
        clear_background(WHITE)
        draw_texture_ex(self.background, [0, 0], 0, 1, WHITE)
        draw_texture_ex(self.banner, [SCREEN_WIDTH / 2 - self.banner.width * self.BANNER_SCALE / 2, 0], 0, self.BANNER_SCALE, WHITE)
        end_drawing()
