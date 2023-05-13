from .interface import LoggerInterface


class DummyLogger(LoggerInterface):
    def info(self, message, **kwargs):
        pass

    def warning(self, message, **kwargs):
        pass

    def error(self, message, **kwargs):
        pass

    def debug(self, message, **kwargs):
        pass
