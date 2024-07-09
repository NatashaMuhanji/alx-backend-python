#!/usr/bin/env python3
""" a python module to loop 10 times """
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """a simple asynchronous generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        random_value = random.uniform(0, 10)
        yield random_value
