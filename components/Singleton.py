import typing
from .GameState import GameState

class Singleton:

    state: GameState

    def __init__(self):
        self.state = GameState.MENU

singleton = Singleton()