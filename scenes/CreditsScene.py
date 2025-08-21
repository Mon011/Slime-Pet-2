from raylibpy import *
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
    back_button: Rectangle

    def load(self):
        self.background_image = load_image("assets/background.png")
        self.background = load_texture_from_image(self.background_image)
        self.banner_image = load_image("assets/banner.png")
        self.banner = load_texture_from_image(self.banner_image)
        self.exit_button = Rectangle(SCREEN_WIDTH / 2 - self.BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + self.BUTTON_HEIGHT * 2 + self.BUTTON_MARGIN * 2, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.back_button = Rectangle(SCREEN_WIDTH / 2 - self.BUTTON_WIDTH / 2, SCREEN_HEIGHT / 2 + self.BUTTON_HEIGHT * 2 + self.BUTTON_MARGIN * 2, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)

        unload_image(self.background_image)
        unload_image(self.banner_image)

    def render(self):
        begin_drawing()
        clear_background(WHITE)
        draw_texture_ex(self.background, [0, 0], 0, 1, WHITE)
        draw_texture_ex(self.banner, [SCREEN_WIDTH / 2 - self.banner.width * self.BANNER_SCALE / 2, 0], 0, self.BANNER_SCALE, WHITE)
        text = "PRODUCTION:\nMon011 PROGRAMMING\nJanDomanMI PROGRAMMING\nmxdevPL DESIGN\nKlecekman DESIGN"
        font_size = 35
        text_width = measure_text(text, font_size)
        x = (get_screen_width() - text_width ) // 2
        y = (get_screen_height() - font_size) // 2
        draw_text(text,x,y-50,font_size,BLACK)
        mouse_pos = get_mouse_position()
        draw_button(self.back_button, 4, GRAY, BLACK, "Back", get_font_default())
        if check_collision_point_rec(mouse_pos, self.back_button) and is_mouse_button_pressed(0):
            singleton.state = GameState.MENU
        
             
        end_drawing()
