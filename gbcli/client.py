from typing import Any

import httpx

client = httpx.Client()


def get_data(url: str) -> dict[Any, Any]:
    response = client.get(url)

    return response.json()
