import typing
from .Mood import Mood
import random
class Slime:
    name: str
    healthpoints: int
    mood: Mood
    def __init__(self):
        self.healthpoints = 100
        self.mood = Mood(random.randint(1, 3))
        self.name = "TODO"

slime = Slime()