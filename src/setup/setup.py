from abc import ABC, abstractmethod
from src.logger import log_method


class AbstractSetup(ABC):

    @log_method
    @abstractmethod
    def setup(self):
        pass

    @log_method
    @abstractmethod
    def install(self):
        pass

