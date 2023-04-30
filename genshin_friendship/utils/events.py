

import time
import pyautogui as pygui


def wait_for_color(position: tuple[int, int], color: tuple[int, int, int]) -> None:
    """
    Waits until the pixel at the given (x, y) position matches the given color.

    Args:
        position (tuple[int, int]): pixel position (x, y)
        color (tuple[int, int, int]): color to match in (r, g, b)
    """
    while not pygui.pixelMatchesColor(position[0], position[1], color):
        time.sleep(0.1)
