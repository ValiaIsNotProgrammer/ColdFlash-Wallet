from abc import ABC, abstractmethod


class AbstractFlashDriveBackup(ABC):

    @abstractmethod
    def __init__(self, flashdrive_name: str = None):
        pass

    @abstractmethod
    def read_data(self, file_path: str):
        pass

    @abstractmethod
    def write_data(self, file_path: str):
        pass


