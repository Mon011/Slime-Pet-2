from pyray import *
from .Scene import Scene
from config import *
from components import draw_button, draw_button_rect, singleton, GameState

class ParkScene(Scene):

    def load(self):
        pass

    def render(self):
        begin_drawing()
        clear_background(GREEN)

        draw_text("PARK SCENE", int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), 64, BLACK)
        end_drawing()