from pyray import *
from .Scene import Scene
from config import *
from components import singleton, GameState
import ui_components.buttons as button
import ui_components.bars as bar
from pathlib import Path

class ParkScene(Scene):
    background: Texture2D
    town_button: Texture2D
    health_bar: Texture2D
    hunger_bar: Texture2D

    def load(self):
        self.background = load_texture(str(Path("assets/backgrounds/park-scene.png")))
        self.town_button = load_texture(str(Path("assets/buttons/town-button.png")))
        self.health_bar = load_texture(str(Path("assets/bar/health_bar_sprite.png")))
        self.hunger_bar = load_texture(str(Path("assets/bar/hunger_bar_sprite.png")))
        self.main_sprite_texture = load_texture(str(Path("assets/entities/slime/static/sprite-main.png")))

    def render(self):
        draw_texture_ex(self.background, [0, 0], 0, 1, WHITE)
        button.multiple_state_button(self.town_button, int(SCREEN_WIDTH * 0.85), int(SCREEN_HEIGHT * 0.75), 2, navigate_to_town)
        bar_x = int(SCREEN_WIDTH * 0.65)
        bar.progress_bar(self.health_bar, bar_x, int(SCREEN_HEIGHT * 0.05), Vector2(bar_x + 50, int(SCREEN_HEIGHT * 0.05) + 30), 80, 100, RED)
        draw_texture_ex(self.hunger_bar, [int(SCREEN_WIDTH * 0.65), int(SCREEN_HEIGHT * 0.13)], 0, 3, WHITE) 
        draw_texture_ex(self.main_sprite_texture, [SCREEN_WIDTH / 2 - self.main_sprite_texture.width * TEXTURE_SCALE / 2, int(SCREEN_HEIGHT * 0.75)], 0, TEXTURE_SCALE, WHITE)

    def unload(self):
        unload_texture(self.background)
        unload_texture(self.town_button)
        unload_texture(self.health_bar)
        unload_texture(self.hunger_bar)
        unload_texture(self.main_sprite_texture)

def navigate_to_town():
    singleton.state = GameState.TOWN
