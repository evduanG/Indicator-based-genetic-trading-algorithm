from abc import ABC, abstractmethod

class INode(ABC):
    @abstractmethod
    def mutation(self):
        pass

    @abstractmethod
    def get_crossover(self):
        pass

    @abstractmethod
    def crossover(self, tree_a, tree_b):
        pass

    @abstractmethod
    def calc(self, data, is_to_str):
        pass

    @abstractmethod
    def to_string(self):
        pass

