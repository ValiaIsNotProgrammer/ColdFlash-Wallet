import urllib.request
import tarfile
import subprocess
import os
import getpass
from abc import abstractmethod

import usb.backend.libusb1

from src.logger import logger
from src.setup.setup import AbstractSetup
from src.settings import BACKENDS_BINARIES_URL, BACKENDS_BINARIES_FILE


class AbstractFlashDriveSetup(AbstractSetup):

    @classmethod
    @abstractmethod
    def setup(cls):
        pass

    @classmethod
    @abstractmethod
    def install(cls):
        pass

    @classmethod
    @abstractmethod
    def is_valid_backend(cls):
        pass


class DarwinFlashDriveSetup(AbstractFlashDriveSetup):
    backend = None

    @classmethod
    def setup(cls):
        cls.backend = usb.backend.libusb1.get_backend()
        if cls.is_valid_backend():
            logger.info("Success, backend found: {}".format(cls.backend))
            return
        logger.warning("The backend was not found. The download for the backend is about to take place")
        cls.install()

    @classmethod
    def install(cls):
        logger.info("Checking the server")
        urllib.request.urlretrieve(BACKENDS_BINARIES_URL, BACKENDS_BINARIES_FILE)
        logger.info("Downloading the backend")
        tar = tarfile.open(BACKENDS_BINARIES_FILE, "r:bz2")
        logger.info("Unzipping an image")
        tar.extractall()
        logger.info("Getting all binaries")
        tar.close()
        logger.info("Сlosing the archive and getting the libusb-1.0.26 dir")
        os.chdir("libusb-1.0.26")
        logger.info("Preparing configurations")
        subprocess.call("./configure")
        logger.info("Compiling the source code")
        subprocess.call("make")
        logger.info("Installing the backend")
        password = getpass.getpass("Enter your password: ")
        subprocess.call("echo {} | sudo -S make install".format(password), shell=True)
        logger.info("Success!")
        cls.setup()

    @classmethod
    def is_valid_backend(cls):
        if cls.backend:
            return True
        return False


class WindowsFlashDriveSetup(AbstractFlashDriveSetup):
    backend = None


    def setup(cls):
        pass

    def _install(cls):
        pass

    def is_valid_backend(cls):
        pass


class LinuxFlashDriveSetup(AbstractFlashDriveSetup):
    backend = None

    def setup(cls):
        pass

    def _install(cls):
        pass

    def is_valid_backend(cls):
        pass
