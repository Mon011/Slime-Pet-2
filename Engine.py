from systems import * 
from pyray import *
from config import *
from components import *
import string_resources as res

class Engine:
    entities: list
    systems: list

    def run(self):
        init_window(SCREEN_WIDTH, SCREEN_HEIGHT, res.TITLE)
        set_target_fps(TARGET_FPS)
        systems = [UISystem(), RenderSystem(), SurvivalSystem()] 

        for system in systems:
            system.load()

        while not window_should_close():
            begin_drawing()
            previous_state = singleton.state
            
            if previous_state != singleton.state:
                for system in systems:
                    system.unload()
            
            for system in systems:
                system.update()

            if previous_state != singleton.state:
                for system in systems:
                    system.load()
                
            end_drawing()

        close_window()

engine = Engine()
