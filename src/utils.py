import asyncio
from collections.abc import Callable
from datetime import datetime
from functools import lru_cache, partial, wraps
from typing import Any

from orjson import loads


def run_in_executor(_func: Callable) -> Callable:
    @wraps(_func)
    def wrapped(*args, **kwargs) -> Any:
        loop = asyncio.get_event_loop()
        func = partial(_func, *args, **kwargs)
        return loop.run_in_executor(executor=None, func=func)

    return wrapped


@run_in_executor
@lru_cache(maxsize=1024)
def async_file_loader(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


async def load_essays_data():
    essays = loads(await async_file_loader("static/pages/essays.json"))
    return list(
        sorted(
            (essay for essay in essays if essay.get("published")),
            key=lambda essay: datetime.strptime(essay.get("created_at"), "%Y-%m-%d"),
            reverse=True,
        )
    )
