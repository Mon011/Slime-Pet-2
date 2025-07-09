from pyray import *
from systems import * 
from components import *

def main():
    init_window(1280, 720, "Slime Pet 2")

    systems = [UISystem()]
    for system in systems:
        system.load()

    while not window_should_close():
        begin_drawing()
        clear_background(WHITE)

        for system in systems:
            system.update()

        end_drawing()

    close_window()

if __name__ == "__main__":
    main()