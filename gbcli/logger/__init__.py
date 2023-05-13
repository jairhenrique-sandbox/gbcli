from .interface import LoggerInterface

from .github import GithubActionLogger
from .dummy import DummyLogger

__all__ = ("LoggerFactory",)


class LoggerFactory:
    @staticmethod
    def create(name: str) -> LoggerInterface:
        name = str(name).lower()

        if name == "github":
            return GithubActionLogger()

        return DummyLogger()
