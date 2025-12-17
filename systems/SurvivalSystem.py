from .System import System
from components import *
from scenes import *
from entities import slime
import time

class SurvivalSystem(System):
    _scene: Scene

    last_sync_time: float = time.time()
    hunger_decrease: int = 0 

    def load(self):
        pass 

    def update(self):
        print("health: ", slime.healthpoints)
        print("hunger: ", slime.hunger)
        print("hunger dec:", self.hunger_decrease)

        if(slime.hunger > 0):
            if(singleton.state == GameState.PARK or
               singleton.state == GameState.TOWN):
                self.last_sync_time = time.time()
                if(slime.hunger <= self.hunger_decrease):
                    slime.hunger = 0
                elif(self.hunger_decrease > 0):
                    slime.hunger -= self.hunger_decrease
                    self.hunger_decrease = 0


            if(singleton.state == GameState.SHOP or 
                singleton.state == GameState.PLAYGROUND):
                self.hunger_decrease = int((time.time() - self.last_sync_time) // 1); 
                        
        if(slime.hunger == 0):
           if(time.time() > self.last_sync_time):
               slime.healthpoints -= 1;
               self.last_sync_time = time.time()
           if(slime.healthpoints == 0): 
               slime.healthpoints = 0 

    def unload(self):
        pass
    