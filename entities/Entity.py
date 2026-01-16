import typing
import uuid
from components import Component

class Entity:
    id: int
    components: list

    def __init__(self, components):
        self.id = uuid.uuid1() 
        self.components = components

    def get_component(self, type: type) -> Component:
        for component in self.components:
            if type == type(component):
                return component 

    def has_component(self, types: list):
        for type in types:
            if type not in self.components:
                return False
    