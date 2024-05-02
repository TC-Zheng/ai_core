import functools
import logging
import time
from typing import Any, Callable, TypeVar, cast

T = TypeVar("T", bound=Callable[..., Any])  # A type variable that can be any function


def debug_log(func: T) -> T:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logger = logging.getLogger(func.__module__)
        start_time = time.time()  # Capture the start time
        logger.debug(f"Entering {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.debug(
            f"Exited {func.__name__} with result={result} (execution time: {time.time() - start_time:.4f} seconds)"
        )
        return result

    return cast(T, wrapper)
