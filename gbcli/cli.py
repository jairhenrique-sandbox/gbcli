import typer

from gbcli.client import get_data
from gbcli.logger import LoggerFactory

app = typer.Typer()


@app.command()
def hello(name: str, printer: str = "dummy"):
    logger = LoggerFactory.create(printer)

    logger.error(f"Chamando hello command com nome: {name}")

    print(f"Hello {name}")


@app.command()
def counter(number: int, printer: str = "dummy"):
    logger = LoggerFactory.create(printer)

    logger.warning(f"Contando até {number}")

    for value, _ in enumerate(range(number), 1):
        print(f"Contando {value}")


@app.command()
def get(url: str, printer: str = "dummy"):
    logger = LoggerFactory.create(printer)

    logger.info(f"Buscando dados na url {url}")

    data = get_data(url)

    logger.debug(f"Debug response: {data}")
