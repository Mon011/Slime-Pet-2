from pyray import *
from .Scene import Scene
from config import *
from pathlib import Path
from components import singleton, GameState
import ui_components.buttons as button
import ui_components.bars as bar

class PlaygroundScene(Scene):
    map_button: Texture2D

    def load(self):
        self.map_button = load_texture(str(Path("assets/buttons/map-button.png")))

    def render(self):
        clear_background(DARKGRAY)
        button.multiple_state_button(self.map_button, int(SCREEN_WIDTH * 0.80), int(SCREEN_HEIGHT * 0.75), Scale.DOUBLED, navigate_to_map)

    def unload(self):
        unload_texture(self.map_button)

    def map_view():
        pass

def navigate_to_map():
    singleton.state = GameState.MAP