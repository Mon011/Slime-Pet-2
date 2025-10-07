from pyray import *
from pathlib import Path
from config import Scale 

progress_bar_image = load_image(str(Path("assets/bar/progress_bar.png")))

def progress_bar(bar_texture: Texture2D, logo_texture: Texture2D, x: int, y: int, current_progress: int, max_progress: int, color: Color):
    if current_progress > max_progress:
        current_progress = max_progress

    max_width = bar_texture.width * Scale.TRIPLED - (2 * Scale.TRIPLED) 
    render_progress = int(max_width * (current_progress / max_progress))

    draw_rectangle_rec(Rectangle(x + logo_texture.width, y + logo_texture.height // 2, render_progress, bar_texture.height * Scale.TRIPLED), color)
    draw_texture_ex(bar_texture, [x + logo_texture.width, y + logo_texture.height // 2], 0, Scale.TRIPLED, WHITE) 
    draw_texture_ex(logo_texture, [x, y], 0, Scale.TRIPLED, WHITE)