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
