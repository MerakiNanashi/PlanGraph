from core.utils.base import asyncio, wraps
from core.utils.logging import get_logger

logger = get_logger(__name__)

def retry(
    retries: int = 3,
    backoff: float = 1.0,
    exceptions: tuple[type[Exception], ...] = (
        Exception,
    ),
):
    def decorator(func):

        @wraps(func)
        async def wrapper(
            *args,
            **kwargs,
        ):

            for attempt in range(retries):

                try:
                    return await func(
                        *args,
                        **kwargs,
                    )

                except exceptions as exc:

                    is_last_attempt = (
                        attempt == retries - 1
                    )

                    if is_last_attempt:

                        logger.exception(
                            (
                                "Retries exhausted | "
                                "function=%s | "
                                "attempts=%s"
                            ),
                            func.__name__,
                            retries,
                        )

                        raise

                    delay = (
                        backoff
                        * (2 ** attempt)
                    )

                    logger.warning(
                        (
                            "Retrying | "
                            "function=%s | "
                            "attempt=%s/%s | "
                            "delay=%.2fs | "
                            "error=%s"
                        ),
                        func.__name__,
                        attempt + 1,
                        retries,
                        delay,
                        str(exc),
                    )

                    await asyncio.sleep(
                        delay
                    )

        return wrapper

    return decorator