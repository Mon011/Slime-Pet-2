from pyray import *
from systems import * 
from components import *
from config import *
from entities import slime
import string_resources as res

def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, res.TITLE)
    set_target_fps(TARGET_FPS)
    ui_system = UISystem()
    systems = [ui_system]

    for system in systems:
        system.load()

    while not window_should_close():
        previous_state = singleton.state
        begin_drawing()
        for system in systems:
            system.update()
        
        if previous_state != singleton.state:
            ui_system.load()
        
        end_drawing()


    close_window()

if __name__ == "__main__":
    main()