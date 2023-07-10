import re
import os
import sys
import subprocess

import usb.core
import usb.util

from abc import ABC, abstractmethod
from src.logger import log_method, logger
from src.setup.flashdrive_setup import DarwinFlashDriveSetup


class AbstractUSBFlashDrive(ABC):

    @log_method
    @abstractmethod
    def prepare_io(self):
        pass

    @log_method
    @abstractmethod
    def get_flashdrive_path(self):
        pass

    @log_method
    @abstractmethod
    def get_flashdrive_name(self):
        pass

    @log_method
    @abstractmethod
    def read_data(self, file_path: str):
        pass

    @log_method
    @abstractmethod
    def write_data(self, file_path: str, data: str):
        pass

    @log_method
    @abstractmethod
    def backup_data(self, file_path: str, backup_path: str):
        pass

    @log_method
    @abstractmethod
    def check(self):
        pass


class DarwinUSBFlashDrive(AbstractUSBFlashDrive):

    def __init__(self):
        # logger.info(usb.core.show_devices())
        # self.setup_flashdrive()
        # self.device = self.get_flashdrive()
        # self.prepare_io()
        # self.dev_info = self.parse_lsusb_output(str(usb.core.find()))
        pass

    def setup_flashdrive(self):
        DarwinFlashDriveSetup().setup()

    def get_flashdrive(self) -> usb.core.Device:
        devices = [dev for dev in usb.core.find(find_all=True)]
        if devices:
            return devices[0]
        else:
            logger.warning("Usb isn't found.\nВаше usb устройсто не найдено." \
                   " Пожалуйста, убедитесь что usb устройство подключено к компьютеру и работает исправно." \
                   "Для большей информации о запуске приложения ознакомтиесь в README. " \
                   "Если проблема не решается, то отправте вашу проблему в обсуждения github.com")
            sys.exit()

    def path_usb_dir(self):
        flashdrive_path = '/Volumes/USB_DISK'

        if not os.path.exists(flashdrive_path):
            try:
                os.makedirs(flashdrive_path)
            except Exception as e:
                print(f"Не удалось создать директорию на флешке: {e}")
                return None
        return flashdrive_path

    def write_data(self, file_name: str, data: str):
        file_name = os.path.join(self.path_usb_dir(), file_name)
        print(file_name)
        echo_process = subprocess.Popen(f'echo "{data}" > {file_name}', shell=True)
        echo_process.wait()

        with open(file_name, 'r') as f:
            print(f.read())
            content = f.read()
            if content == data:
                print(f"Данные успешно записаны в файл {file_name}")
            else:
                print(f"Не удалось записать данные в файл {file_name}")

    def read_data(self, file_path: str, ep_in):
        try:
            data_read = ep_in.read(13, timeout=1000)
            print(data_read)
        except usb.core.USBTimeoutError as ex:
            print(ex)
            usb.util.dispose_resources(self.device)

    def get_interface(self):
        cfg = self.device.get_active_configuration()
        interface_number = cfg[(0, 0)].bInterfaceNumber
        return usb.util.find_descriptor(cfg, bInterfaceNumber=interface_number)

    def prepare_io(self) -> None:
        try:
            self.device.set_configuration()
        except Exception as ex:
            logger.error(f"couldn't get the configuration: {ex}")
        try:
            if self.device.is_kernel_driver_active(0):
                self.device.detach_kernel_driver(0)
        except Exception as ex:
            logger.error("It is impossible to write and read data from the flashdrive, "
                         f"since the interface core cannot be turned off: {ex}")
        usb.util.claim_interface(self.device, 0)

    def get_flashdrive_path(self):
        pass

    def get_flashdrive_name(self):
        config = self.device.get_active_configuration()
        interface = config[(0, 0)]

        endpoint = interface[0]
        disk_name = usb.util.get_string(self.device, endpoint)
        return disk_name

    def backup_data(self, file_path: str, backup_path: str):
        pass

    def check(self):
        pass

    def parse_lsusb_output(self, output):
        device_info = {}

        for line in output.split("\n"):
            match = re.match(r"^\s*(\S[^:]*):\s*(.*)$", line)
            if match:
                key = match.group(1)
                value = match.group(2)

                if key in ["bLength", "bMaxPacketSize0", "wTotalLength", "bMaxPower"]:
                    value = int(value, 16)
                elif key in ["idVendor", "idProduct"]:
                    value = value.lower()
                elif key.startswith("i"):
                    value = value.strip()
                elif re.match(r"^\s*[0-9a-f]+\s*$", value, re.IGNORECASE):
                    value = int(value.strip(), 16)

                if key == "DEVICE":
                    device_info = {}
                    current_key = None
                elif key == "CONFIGURATION":
                    device_info["CONFIGURATION"] = {}
                    current_key = "CONFIGURATION"
                elif key == "INTERFACE":
                    device_info["CONFIGURATION"]["INTERFACE"] = {}
                    current_key = "INTERFACE"
                elif key == "ENDPOINT":
                    device_info["CONFIGURATION"]["INTERFACE"]["ENDPOINT"] = {}
                    current_key = "ENDPOINT"
                else:
                    current_key = key

                if current_key is not None:
                    device_info[current_key.strip()] = value

        return device_info


class WindowsUSBFlashDrive(AbstractUSBFlashDrive):

    def __init__(self):
        pass

    def write_data(self, file_path: str, data: str):
        pass

    def prepare_io(self):
        pass

    def get_flashdrive_name(self):
        pass

    def get_flashdrive_path(self):
        pass

    def backup_data(self, file_path: str, backup_path: str):
        pass

    def read_data(self, file_path: str):
        pass

    def check(self):
        pass


class LinuxUSBFlashDrive(AbstractUSBFlashDrive):

    def __init__(self):
        pass

    def write_data(self, file_path: str, data: str):
        pass

    def prepare_io(self):
        pass

    def get_flashdrive_name(self):
        pass

    def get_flashdrive_path(self):
        pass

    def backup_data(self, file_path: str, backup_path: str):
        pass

    def read_data(self, file_path: str):
        pass

    def check(self):
        pass




