from pyray import *
from .Scene import Scene
from config import *
from pathlib import Path
import ui_components.buttons as button
from components import singleton, GameState

class MapScene(Scene):
    background: Texture2D
    back_button: Texture2D 
    shop_button: Texture2D 
    playground_button: Texture2D 
    BUTTON_WIDTH = 150
    BUTTON_HEIGHT = 60

    def load(self):
        self.background = load_texture(str(Path("assets/backgrounds/map-scene.png")))
        self.back_button = load_texture(str(Path("assets/buttons/back-button.png")))
        self.shop_button = load_texture(str(Path("assets/buttons/shop-map-button.png")))
        self.playground_button = load_texture(str(Path("assets/buttons/playland-map-button.png")))

    def render(self):
        clear_background(WHITE)
        draw_texture_ex(self.background, [0, 0], 0, Scale.QUADRUPLED, WHITE)
        button.multiple_state_button(self.back_button, SCREEN_WIDTH // 16 - self.back_button.width // 4, SCREEN_HEIGHT // 15, Scale.TRIPLED, navigate_to_town)
        button.multiple_state_button(self.shop_button, SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.2, Scale.TRIPLED, navigate_to_shop)
        button.multiple_state_button(self.playground_button, SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.75, Scale.QUADRUPLED, navigate_to_playground)

    def unload(self):
        unload_texture(self.background)
        unload_texture(self.back_button)
        unload_texture(self.shop_button)
        unload_texture(self.playground_button)

def navigate_to_town():
    singleton.state = GameState.TOWN

def navigate_to_shop():
    singleton.state = GameState.SHOP

def navigate_to_playground():
    singleton.state = GameState.PLAYGROUND
