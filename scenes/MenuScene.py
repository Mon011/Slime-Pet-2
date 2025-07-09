from pyray import *
from .Scene import Scene

class MenuScene(Scene):

    def render(self):
        begin_drawing()
        draw_text("This is main scene", 190, 200, 20, VIOLET)
        end_drawing()