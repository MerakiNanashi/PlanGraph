import logging

from core.utils.base import *
from core.utils.latency import measure_latency

__all__ = [
    "measure_latency",
]

logging.getLogger(__name__).info("Core utils initialized")