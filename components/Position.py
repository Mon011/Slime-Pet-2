from .Direction import Direction

class Position():
    x: float
    y: float
    speed: float
    direction: Direction

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.direction = Direction.NONE

    def __init__(self, x, y, speed, direction):
       self.x = x
       self.y = y
       self.speed = speed 
       self.direction = direction
        
