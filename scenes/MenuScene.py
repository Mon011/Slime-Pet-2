from pyray import *
from .Scene import Scene
from config import *
from components import draw_button, singleton, GameState

class MenuScene(Scene):
    BANNER_SCALE = 0.8
    BUTTON_WIDTH = 250
    BUTTON_HEIGHT = 80
    BUTTON_MARGIN = 30

    background_image: Image 
    background: Texture2D
    banner_image: Image
    banner: Texture2D
    play_button: Rectangle
    credits_button: Rectangle
    exit_button: Rectangle
    

    def load(self):
        self.background_image = load_image("assets/background.png")
        self.background = load_texture_from_image(self.background_image)
        self.banner_image = load_image("assets/banner.png")
        self.banner = load_texture_from_image(self.banner_image)
        self.play_button = Rectangle(SCREEN_WIDTH / 2 - self.BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.credits_button = Rectangle(SCREEN_WIDTH / 2 - self.BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + self.BUTTON_HEIGHT + self.BUTTON_MARGIN, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.exit_button = Rectangle(SCREEN_WIDTH / 2 - self.BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + self.BUTTON_HEIGHT * 2 + self.BUTTON_MARGIN * 2, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        unload_image(self.background_image)
        unload_image(self.banner_image)

    def render(self):
        begin_drawing()
        clear_background(WHITE)
        draw_texture_ex(self.background, [0, 0], 0, 1, WHITE)
        draw_button(self.play_button, 4, GRAY, BLACK, "Start", get_font_default())
        draw_button(self.credits_button, 4, GRAY, BLACK, "Credits", get_font_default())
        draw_button(self.exit_button, 4, GRAY, BLACK, "Exit", get_font_default())
        draw_texture_ex(self.banner, [SCREEN_WIDTH / 2 - self.banner.width * self.BANNER_SCALE / 2, 0], 0, self.BANNER_SCALE, WHITE)
        mouse_pos = get_mouse_position()
        if check_collision_point_rec(mouse_pos, self.play_button) and is_mouse_button_pressed(0):
            pass
        elif check_collision_point_rec(mouse_pos, self.credits_button) and is_mouse_button_pressed(0):
            singleton.state = GameState.CREDITS 
        elif check_collision_point_rec(mouse_pos, self.exit_button) and is_mouse_button_pressed(0):
            close_window()
            exit()
        end_drawing()
