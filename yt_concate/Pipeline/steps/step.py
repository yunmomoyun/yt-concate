from abc import ABC, abstractmethod
from abc import abstractclassmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs):
        pass


class StepException(Exception):
    pass
