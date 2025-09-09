from pyray import *
from .Scene import Scene
from config import *
from components import draw_multiple_state_button, singleton, GameState
from pathlib import Path

class ParkScene(Scene):
    background: Texture2D
    town_button: Texture2D
    health_bar: Texture2D
    hunger_bar: Texture2D

    def load(self):
        self.background_image = load_image(str(Path("assets/backgrounds/park-scene.png")))
        self.background = load_texture_from_image(self.background_image)
        self.town_button = load_texture(str(Path("assets/buttons/town-button.png")))
        self.health_bar = load_texture(str(Path("assets/bar/health_bar_sprite.png")))
        self.hunger_bar = load_texture(str(Path("assets/bar/hunger_bar_sprite.png")))
        unload_image(self.background_image)

    def render(self):
        begin_drawing()
        clear_background(WHITE)
        draw_texture_ex(self.background, [0, 0], 0, 1, WHITE)
        draw_multiple_state_button(self.town_button, int(SCREEN_WIDTH * 0.85), int(SCREEN_HEIGHT * 0.75), 2, navigate_to_town)
        draw_texture_ex(self.health_bar, [int(SCREEN_WIDTH * 0.65), int(SCREEN_HEIGHT * 0.05)], 0, 3, WHITE) 
        draw_texture_ex(self.hunger_bar, [int(SCREEN_WIDTH * 0.65), int(SCREEN_HEIGHT * 0.13)], 0, 3, WHITE) 
        end_drawing()

def navigate_to_town():
    singleton.state = GameState.TOWN
