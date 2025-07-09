from abc import ABC, abstractmethod
import typing
class System(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def update(self):
        pass    