import functools
import logging
import time


def debug_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        start_time = time.time()  # Capture the start time
        logger.debug(f"Entering {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logger.debug(
            f"Exited {func.__name__} with result={result} (execution time: {time.time() - start_time:.4f} seconds)"
        )
        return result

    return wrapper
