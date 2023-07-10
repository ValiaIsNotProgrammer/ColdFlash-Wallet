import logging
import functools


# class Logger:
#     """ Represents a Logger object handles logging functionalities executed as a singleton"""
#     _instance = None
#
#     def __init__(self, name, level=logging.DEBUG):
#         self.logger = logging.getLogger(name)
#         self.logger.setLevel(level)
#         self.logger.setLevel(level)
#
#         # Создаем обработчик (handler) для записи логов в файл
#         stream_handler = logging.StreamHandler()
#         stream_handler.setLevel(logging.DEBUG)
#
#         # Создаем формат сообщений
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         stream_handler.setFormatter(formatter)
#
#         # Добавляем обработчик к логгеру
#         self.logger.addHandler(stream_handler)
#
#     @classmethod
#     def get_logger(cls):
#         """ Singleton method to get the Logger instance """
#         if not cls._instance:
#             cls._instance = cls(name=__name__, level=logging.DEBUG)
#         return cls._instance.logger

# Создаем объект логгера и задаем уровень логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)


logger.addHandler(console_handler)


def log_method(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        logger.debug(f"Calling {method.uy__name__} with args: {args} and kwargs: {kwargs}")
        return method(*args, **kwargs)
    return wrapper