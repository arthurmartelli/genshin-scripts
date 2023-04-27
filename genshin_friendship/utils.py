"""
Utility module for automating GUI tasks using PyAutoGUI and PyGetWindow.

This module provides several functions for interacting with GUI applications,
such as switching to a specific window, waiting for a certain pixel color to appear,
pressing a key for a specified duration or until a certain pixel color is reached.

Functions:
- switch_to_window(title: str) -> None
- wait_for_color(position: tuple[int, int], color: tuple[int, int, int]) -> None
- press_key_for_duration(key: str, duration: float) -> None
- press_key_until_color(key: str, position: tuple[int, int], color: tuple[int, int, int]) -> None
"""

import time
import pyautogui as pygui
import pygetwindow as gw


def switch_to_window(title: str) -> None:
    """
    Switches to the window with the given title.

    Args:
        title (str): title of the window to switch to.
    Returns:
        None.
    Examples:
        switch_to_window("My Window")
    """
    try:
        window = gw.getWindowsWithTitle(title)[0]
        window.activate()
    except IndexError:
        print(f"No window found with title: {title}")


def wait_for_color(position: tuple[int, int], color: tuple[int, int, int]) -> None:
    """
    Waits until the pixel at the given (x, y) position matches the given color.

    Args:
        position (tuple[int, int]): pixel position (x, y)
        color (tuple[int, int, int]): color to match in (r, g, b)
    """
    while not pygui.pixelMatchesColor(position[0], position[1], color):
        time.sleep(0.1)
    time.sleep(1)


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


def press_key_until_color(
    key: str,
    position: tuple[int, int],
    color: tuple[int, int, int],
) -> None:
    """
    Holds down the given key until the pixel at the given
    position matches the given color.

    Args:
        key (str): key to hold down
        position (tuple[int, int]): pixel position (x, y)
        color (tuple[int, int, int]): color to match at the pixel position
    """
    while not pygui.pixelMatchesColor(position[0], position[1], color):
        pygui.keyDown(key)
    pygui.keyUp(key)
