from pyray import *
from .Scene import Scene
from config import *
from components import draw_button_rect, singleton, GameState
from entities import slime

class IntroductionScene(Scene):
    slime_sprite_image: Image
    slime_sprite: Texture2D

    next_button_bounds: Rectangle

    def load(self):
        self.slime_sprite_image = load_image("assets/entities/slime/sprite-main.png")
        self.slime_sprite = load_texture_from_image(self.slime_sprite_image)
        self.next_button_bounds = Rectangle(int(SCREEN_WIDTH * 0.75), int(SCREEN_WIDTH / 2) - self.slime_sprite.width, 150,60)
        unload_image(self.slime_sprite_image)

    def render(self):
        begin_drawing()
        clear_background(BLUE)

        draw_text("This is your new Slime!", int(SCREEN_WIDTH / 2) - 150, int(SCREEN_HEIGHT / 8), 27, BLACK)
        draw_texture_ex(self.slime_sprite, [int(SCREEN_WIDTH / 2) - self.slime_sprite.width, int(SCREEN_HEIGHT / 2)], 0, 2, WHITE)
        draw_text("Your slime pet's name: " + slime.name, int(SCREEN_WIDTH / 2) - self.slime_sprite.width - 150, int(SCREEN_HEIGHT * 0.80), 36, WHITE)
        draw_button_rect(Rectangle(int(SCREEN_WIDTH * 0.75), int(SCREEN_WIDTH / 2) - self.slime_sprite.width, 150,60), 2, GRAY, BLACK, "NEXT", get_font_default())

        if check_collision_point_rec(get_mouse_position(), self.next_button_bounds):
            if(is_mouse_button_released(0)):
                singleton.state = GameState.PARK

        end_drawing()
