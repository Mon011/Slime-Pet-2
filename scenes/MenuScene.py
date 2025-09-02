from pyray import *
from .Scene import Scene
from config import *
from components import draw_button, singleton, GameState
from pathlib import Path

class MenuScene(Scene):
    BANNER_SCALE = 0.8
    BUTTON_MARGIN = 30

    background_image: Image 
    background: Texture2D
    banner_image: Image
    banner: Texture2D

    play_button_state: int
    credits_button_state: int
    exit_button_state: int 

    play_button_image: Texture2D
    play_button_on_hover_image: Texture2D
    play_button_pressed_image: Texture2D
    credits_button_image: Texture2D
    credits_button_on_hover_image: Texture2D
    credits_button_pressed_image: Texture2D
    exit_button_image: Texture2D
    exit_button_on_hover_image: Texture2D
    exit_button_pressed_image: Texture2D

    play_button: Texture2D
    play_button_on_hover: Texture2D
    play_button_pressed: Texture2D
    credits_button: Texture2D
    credits_button_on_hover: Texture2D
    credits_button_pressed: Texture2D
    exit_button: Texture2D
    exit_button_on_hover: Texture2D
    exit_button_pressed: Texture2D

    def load(self):
        self.background_image = load_image(str(Path("assets/background.png")))
        self.background = load_texture_from_image(self.background_image)
        self.banner_image = load_image(str(Path("assets/banner.png")))
        self.banner = load_texture_from_image(self.banner_image)

        self.play_button_state = 0
        self.credits_button_state = 0
        self.exit_button_state = 0

        self.play_button_image = load_image(str(Path("assets/buttons/play/standard.png")))
        self.play_button_on_hover_image = load_image(str(Path("assets/buttons/play/on-hover.png")))
        self.play_button_pressed_image = load_image(str(Path("assets/buttons/play/pressed.png")))

        self.credits_button_image = load_image(str(Path("assets/buttons/credits/standard.png")))
        self.credits_button_on_hover_image = load_image(str(Path("assets/buttons/credits/on-hover.png")))
        self.credits_button_pressed_image = load_image(str(Path("assets/buttons/credits/pressed.png")))

        self.exit_button_image = load_image(str(Path("assets/buttons/exit/standard.png")))
        self.exit_button_on_hover_image = load_image(str(Path("assets/buttons/exit/on-hover.png")))
        self.exit_button_pressed_image = load_image(str(Path("assets/buttons/exit/pressed.png")))
        
        self.play_button = load_texture_from_image(self.play_button_image)
        self.play_button_on_hover = load_texture_from_image(self.play_button_on_hover_image)
        self.play_button_pressed = load_texture_from_image(self.play_button_pressed_image)

        self.credits_button = load_texture_from_image(self.credits_button_image)
        self.credits_button_on_hover = load_texture_from_image(self.credits_button_on_hover_image)
        self.credits_button_pressed = load_texture_from_image(self.credits_button_pressed_image)
        
        self.exit_button = load_texture_from_image(self.exit_button_image)
        self.exit_button_on_hover = load_texture_from_image(self.exit_button_on_hover_image)
        self.exit_button_pressed = load_texture_from_image(self.exit_button_pressed_image)

        self.play_button_bounds = Rectangle(int(SCREEN_WIDTH / 2 - self.play_button_image.width / 2), int(SCREEN_HEIGHT / 2), self.play_button_image.width, self.play_button_image.height)
        self.credits_button_bounds = Rectangle(int(SCREEN_WIDTH / 2 - self.credits_button_image.width / 2), int(SCREEN_HEIGHT / 2 + self.credits_button_image.height + self.BUTTON_MARGIN), self.credits_button_image.width, self.credits_button_image.height)
        self.exit_button_bounds = Rectangle(int(SCREEN_WIDTH / 2 - self.exit_button_image.width / 2), int(SCREEN_HEIGHT / 2 + self.exit_button_image.height * 2 + self.BUTTON_MARGIN * 2), self.exit_button_image.width, self.exit_button_image.height)

        unload_image(self.background_image)
        unload_image(self.banner_image)

    def render(self):
        begin_drawing()
        clear_background(WHITE)

        draw_texture_ex(self.background, [0, 0], 0, 1, WHITE)
        draw_rectangle_rec(self.play_button_bounds, BLANK)
        draw_rectangle_rec(self.credits_button_bounds, BLANK)
        draw_rectangle_rec(self.exit_button_bounds, BLANK)

        if(self.play_button_state == 0):
            draw_button(self.play_button, int(self.play_button_bounds.x), int(self.play_button_bounds.y))
        if(self.play_button_state == 1):
            draw_button(self.play_button_on_hover, int(self.play_button_bounds.x), int(self.play_button_bounds.y))
        if(self.play_button_state == 2):
            draw_button(self.play_button_pressed, int(self.play_button_bounds.x), int(self.play_button_bounds.y))
        
        if(self.credits_button_state == 0):
            draw_button(self.credits_button, int(self.credits_button_bounds.x), int(self.credits_button_bounds.y))
        if(self.credits_button_state == 1):
            draw_button(self.credits_button_on_hover, int(self.credits_button_bounds.x), int(self.credits_button_bounds.y))
        if(self.credits_button_state == 2):
            draw_button(self.credits_button_pressed, int(self.credits_button_bounds.x), int(self.credits_button_bounds.y))

        if(self.exit_button_state == 0):
            draw_button(self.exit_button, int(self.exit_button_bounds.x), int(self.exit_button_bounds.y))
        if(self.exit_button_state == 1):
            draw_button(self.exit_button_on_hover, int(self.exit_button_bounds.x), int(self.exit_button_bounds.y))
        if(self.exit_button_state == 2):
            draw_button(self.exit_button_pressed, int(self.exit_button_bounds.x), int(self.exit_button_bounds.y))

        draw_texture_ex(self.banner, [SCREEN_WIDTH / 2 - self.banner.width * self.BANNER_SCALE / 2, 0], 0, self.BANNER_SCALE, WHITE)
        mouse_pos = get_mouse_position()

        if check_collision_point_rec(mouse_pos, self.play_button_bounds):
            if(is_mouse_button_released(0)):
                singleton.state = GameState.INTRODUCTION
                pass
            elif(is_mouse_button_down(0)):
                self.play_button_state = 2
            else:
                self.play_button_state = 1
        else:
            self.play_button_state = 0  

        if check_collision_point_rec(mouse_pos, self.credits_button_bounds):
            if(is_mouse_button_released(0)):
                singleton.state = GameState.CREDITS 
            elif(is_mouse_button_down(0)):
                self.credits_button_state = 2
            else:
                self.credits_button_state = 1
        else:
            self.credits_button_state = 0

        if check_collision_point_rec(mouse_pos, self.exit_button_bounds): 
            if(is_mouse_button_released(0)):
                close_window()
                exit()
            elif(is_mouse_button_down(0)):
                self.exit_button_state = 2
            else:
                self.exit_button_state = 1
        else:
            self.exit_button_state = 0
          
        end_drawing()
