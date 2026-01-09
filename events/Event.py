import threading
from entities import slime

def on_threaded_event(function) -> threading.Thread:
    def wrapper(*args, **kwargs) -> threading.Thread:
        thread = threading.Thread(target = function, args = args, kwargs = kwargs) 
        thread.start()
        return thread
    return wrapper

class Event:

    @on_threaded_event
    def on_trigger(self) -> threading.Thread:
        pass 

class OnCoinIncreaseEvent(Event):
    coin_amount: int

    def __init__(self, coin_amount):
        self.coin_amount = coin_amount
        super().__init__() 

    @on_threaded_event
    def on_trigger(self) -> threading.Thread:
        slime.coins += self.coin_amount 

def on_event(event: Event):
    event.on_trigger().join()