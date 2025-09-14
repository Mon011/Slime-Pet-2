from pyray import *
from .Scene import Scene
from config import *

class TownScene(Scene):
    def load(self):
        pass

    def render(self):
        clear_background(PURPLE)
        draw_text("TOWN SCENE - TODO", 200, 200, 24, BLACK)          