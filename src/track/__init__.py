"""This project demonstrates a proof of concept for tracking machine learning experiments using a Python decorator named `track`. The `track` decorator automatically logs the parameters and results of each experiment to an SQLite database."""

import inspect
import sqlite3
from collections import defaultdict
from functools import wraps
from types import NoneType
from typing import Any, Callable

__all__ = ["track"]

_PY2SQLITE = defaultdict(
    lambda: "TEXT",
    {
        str: "TEXT",
        int: "INTEGER",
        float: "REAL",
        bool: "INTEGER",
        bytes: "BLOB",
        NoneType: "NULL",
    },
)


def _connect() -> sqlite3.Connection:
    return sqlite3.connect("track.db")


def _create_table_from_callable(
    con: sqlite3.Connection, obj: Callable[..., Any]
) -> inspect.Signature:
    signature = inspect.signature(obj)
    columns = ", ".join(
        [
            f"{param.name} {_PY2SQLITE[param.annotation]}"
            for param in signature.parameters.values()
        ]
    )
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {obj.__name__} ({columns})")
    cur.close()
    return signature


def track[**P, R](
    connect: Callable[[], sqlite3.Connection] | None = None,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    if connect is None:
        connect = _connect

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        signature = _create_table_from_callable(connect(), func)

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            bound = signature.bind_partial(*args, **kwargs)
            arguments = [*bound.arguments.values()]
            values = ", ".join("?" * len(arguments))

            with connect() as con:
                cur = con.cursor()
                cur.execute(f"INSERT INTO {func.__name__} VALUES ({values})", arguments)
                cur.close()

            return func(*args, **kwargs)

        return wrapper

    return decorator
