from raylibpy import *
from systems import * 
from components import *
from config import *

def main():
    init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Slime Pet 2")
    ui_system = UISystem()
    systems = [ui_system]
    for system in systems:
        system.load()

    while not window_should_close():
        previous_state = singleton.state

        for system in systems:
            system.update()
        
        if previous_state != singleton.state:
            ui_system.load()


    close_window()

if __name__ == "__main__":
    main()