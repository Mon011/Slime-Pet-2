from .System import System
from components import *
from scenes import *
import typing

class UISystem(System):
    _scene: Scene
    
    def load(self):
        if(singleton.state == GameState.MENU):
            self._scene = MenuScene()
        if(singleton.state == GameState.CREDITS):
            self._scene = CreditsScene()
        self._scene.load()

    def update(self):
        self._scene.render()