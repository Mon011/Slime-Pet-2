from abc import ABC, abstractmethod

class Scene(ABC):

    @abstractmethod
    def render(self):
        pass
