import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.flashdrive.flashdrive import DarwinUSBFlashDrive


if __name__ == "__main__":
    flashdrive = DarwinUSBFlashDrive()
    flashdrive.write_data("hello_world.txt", "Hello World\n")




