import asyncio
from functools import wraps


def retry(
    retries: int = 3,
    backoff: float = 1.0,
):

    def decorator(func):

        @wraps(func)
        async def wrapper(
            *args,
            **kwargs,
        ):

            for attempt in range(
                retries
            ):

                try:
                    return await func(
                        *args,
                        **kwargs,
                    )

                except Exception:

                    if (
                        attempt
                        == retries - 1
                    ):
                        raise

                    await asyncio.sleep(
                        backoff
                        * (2 ** attempt)
                    )

        return wrapper

    return decorator