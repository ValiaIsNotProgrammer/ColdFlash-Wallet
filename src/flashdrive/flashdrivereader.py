from abc import ABC, abstractmethod


class AbstractFlashDriveReader(ABC):

    @abstractmethod
    def __init__(self, flashdrive_name: str = None):
        pass

    @abstractmethod
    def read_data(self, file_path: str):
        pass
