from .System import System
from components import *
from scenes import *
from pyray import *
from pathlib import Path
from config import *
from entities import slime

import typing

class SlimeRenderSystem(System):

    _scene: Scene
    main_sprite_texture: Texture2D

    def load(self):
        pass 

    def update(self):
        pass


