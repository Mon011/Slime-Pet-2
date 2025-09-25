import typing
import uuid
from abc import ABC, abstractmethod

class Entity(ABC):
    id: int
    components: list

    def __init__(self, components):
        self.id = uuid.uuid1() 
        self.components = components

    @abstractmethod
    def get_component(self):
        pass

    def has_types(self, types: list):
        for type in types:
            if type not in self.components:
                return False
    