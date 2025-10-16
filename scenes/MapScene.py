from pyray import *
from .Scene import Scene
from config import *
from pathlib import Path
import ui_components.buttons as button
from components import singleton, GameState

class MapScene(Scene):
    background: Texture2D
    back_button: Rectangle
    shop_button: Rectangle
    playground_button: Rectangle
    BUTTON_WIDTH = 150
    BUTTON_HEIGHT = 60

    def load(self):
        self.background = load_texture(str(Path("assets/backgrounds/map-scene.png")))
        self.back_button = Rectangle(SCREEN_WIDTH // 15 - self.BUTTON_WIDTH // 15, SCREEN_HEIGHT // 15, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.shop_button = Rectangle(SCREEN_WIDTH * 0.55 - self.BUTTON_WIDTH * 0.55, SCREEN_HEIGHT * 0.50, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.playground_button = Rectangle(SCREEN_WIDTH * 0.75 - self.BUTTON_WIDTH * 0.75, SCREEN_HEIGHT // 6, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)

    def render(self):
        clear_background(WHITE)
        draw_texture_ex(self.background, [0, 0], 0, Scale.QUADRUPLED, WHITE)
        button.standard_button(self.back_button, 4, GRAY, BLACK, "Back", get_font_default(), navigate_to_town)
        button.standard_button(self.shop_button, 4, GRAY, BLACK, "Shop", get_font_default(), navigate_to_shop)
        button.standard_button(self.playground_button, 4, GRAY, BLACK, "Playground", get_font_default(), navigate_to_playground)

    def unload(self):
        unload_texture(self.background)

def navigate_to_town():
    singleton.state = GameState.TOWN

def navigate_to_shop():
    singleton.state = GameState.SHOP

def navigate_to_playground():
    singleton.state = GameState.PLAYGROUND
