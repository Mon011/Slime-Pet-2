import typing
from .Mood import Mood
from components import Position
from pyray import *
# from pathlib import Path
import random
class Slime:
    name: str
    healthpoints: int
    hunger: int
    mood: Mood

    def __init__(self):
        self.healthpoints = 100
        self.hunger = 100
        self.mood = Mood(random.randint(1, 3))
        self.name = "TODO"

slime = Slime()