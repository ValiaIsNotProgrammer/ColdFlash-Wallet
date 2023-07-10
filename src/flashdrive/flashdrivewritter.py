from abc import ABC, abstractmethod


class AbstractFlashDriveWritter(ABC):

    @abstractmethod
    def write_data(self, file_path: str):
        pass