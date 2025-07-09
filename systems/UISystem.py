from .System import System
from components import *
from scenes import *
import typing

class UISystem(System):
    _scene: Scene
    
    def load(self):
        pass

    def update(self):
        
        if(singleton.state == GameState.MENU): 
            self._scene = MenuScene()
        self._scene.render()