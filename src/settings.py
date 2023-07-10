import os
import platform


SYSTEM_OS = platform.system()

APP_NAME = "alternative_ledger"
TAILS_BINARIES = {
    "Windows": {
        "url": "",
        "path": ""},
    "Darwin": {
         "url": "https://download.tails.net/tails/stable/tails-amd64-5.14/tails-amd64-5.14.img",
         "path": ""},
    "Linux":  {
        "url": "",
        "path": ""}
}

BACKENDS_BINARIES = {
    "Windows": {
        "url":  "",
        "path": ""},
    "Darwin": {
         "url":  "https://sourceforge.net/projects/libusb/files/libusb-1.0/libusb-1.0.26/libusb-1.0.26.tar.bz2/download",
         "filename": "libusb-1.0.26.tar.bz2"},
    "Linux":  {
         "url":  "https://sourceforge.net/projects/libusb/files/libusb-1.0/libusb-1.0.26/libusb-1.0.26.tar.bz2/download",
         "filename": "llibusb-1.0.26.tar.bz2",
    }
}

if SYSTEM_OS not in TAILS_BINARIES:
    raise ValueError(f'Unsupported operating system: {SYSTEM_OS}')

TAILS_BINARIES_URL = TAILS_BINARIES[SYSTEM_OS]["url"]
BACKENDS_BINARIES_URL = BACKENDS_BINARIES[SYSTEM_OS]["url"]
BACKENDS_BINARIES_FILE = BACKENDS_BINARIES[SYSTEM_OS]["filename"]
