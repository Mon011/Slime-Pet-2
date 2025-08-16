from pyray import *

def calculate_font_size(font: Font, text: str, rectangle: Rectangle, spacing: float, text_scale: int = 2):
    font_size = rectangle.height
    text_size = measure_text_ex(font, text, font_size, spacing)

    scale_x = rectangle.width / text_size.x / text_scale 
    scale_y = rectangle.height / text_size.y / text_scale
    font_size *= min(scale_x, scale_y)
    return font_size

def draw_button(rectangle: Rectangle, line_thick: int, rect_fill_color: Color, rect_border_color: Color, text: str, font: Font, text_spacing: float = 0.0):
    draw_rectangle_rec(rectangle, rect_fill_color)
    draw_rectangle_lines_ex(rectangle, line_thick, rect_border_color)
    font_size = calculate_font_size(font, text, rectangle, text_spacing)
    text_size = measure_text_ex(font, text, font_size, text_spacing)

    text_pos_x = int(rectangle.x + (rectangle.width - text_size.x) / 2 - line_thick)
    text_pos_y = int(rectangle.y + (rectangle.height - text_size.y ) / 2)
    draw_text(text, text_pos_x, text_pos_y, int(font_size), BLACK)

def draw_button(texture: Texture, posX: int, posY: int):
    draw_texture(texture, posX, posY, WHITE)