from .Component import Component
from pyray import *

class Render(Component):
    texture: Texture
    hitbox: Rectangle
    is_animated: bool
    rotation: int

    def __init__(self, texture, is_animated, rotation):
        self.texture = texture
        self.is_animated = is_animated
        self.rotation = rotation
