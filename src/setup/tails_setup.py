import urllib.request
import os
from src.logger import logger
from src.setup.setup import AbstractSetup
from src.settings import TAILS_BINARIES_URL

class TailsSetup(AbstractSetup):

    def setup(self):
        pass

    def install(self):

        def reporthook(block_number, block_size, total_size, previous_percent=[-1]):
            percent = int(block_number * block_size * 100 / total_size)
            if percent != previous_percent[0]:
                msg = f"Downloaded {percent}%"
                print(msg, end="\r")
                print(msg)
                previous_percent[0] = percent


        logger.info("Start to download tails OS")
        file_output = os.path.join(os.getcwd(), "tails.img")
        r = urllib.request.urlretrieve(TAILS_BINARIES_URL, reporthook=reporthook, filename=file_output)





a = TailsSetup()
a.install()








