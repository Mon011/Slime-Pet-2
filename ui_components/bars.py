from pyray import *

def progress_bar(texture: Texture2D, x: int, y: int, start_progress_position: Vector2, current_progress: int, max_progress: int, color: Color):
    # TODO: Fix health bar progress
    max_width = int(texture.width - (start_progress_position.x - x))
    render_progress = int(max_width * (max_progress / current_progress))
    draw_rectangle(int(start_progress_position.x), int(start_progress_position.y), render_progress, texture.height // 2, color)
    draw_texture_ex(texture, [x, y], 0, 3, WHITE) 
    