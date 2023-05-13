from .interface import LoggerInterface

import github_action_utils as gha


class GithubActionLogger(LoggerInterface):
    def info(self, message, **kwargs):
        gha.echo(message, **kwargs)

    def warning(self, message, **kwargs):
        gha.warning(message, **kwargs)

    def error(self, message, **kwargs):
        gha.error(message, **kwargs)

    def debug(self, message, **kwargs):
        gha.debug(message, **kwargs)
