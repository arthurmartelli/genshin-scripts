
import time
from typing import Callable, Any
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
    Holds down the given key until the event returns true

    Args:
        key (str): key to hold down
        event (Callable): event to wait for
        *args: arguments to pass to the event
    """
    pygui.keyDown(key)
    event(*args)
    pygui.keyUp(key)
