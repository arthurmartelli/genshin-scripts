
import time
from typing import Callable
import pyautogui as pygui


def press_key_for_duration(key: str, duration: float) -> None:
    """
    Presses a key for a certain duration

    Args:
        key (str): key to press
        duration (float): duration (in seconds)
    """
    pygui.keyDown(key)
    time.sleep(duration)
    pygui.keyUp(key)


def press_key_until_event(
    key: str,
    event: Callable,
    *args,
) -> None:
    """
    Holds down the given key until the pixel at the given
    position matches the given color.

    Args:
        key (str): key to hold down
        position (tuple[int, int]): pixel position (x, y)
        color (tuple[int, int, int]): color to match at the pixel position
    """
    pygui.keyDown(key)
    event(*args)
    pygui.keyUp(key)
