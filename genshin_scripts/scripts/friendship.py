"""
This module contains the main sequence to gain friendship with the bot

The main sequence consists of four steps:
    1. Login to the game
    2. Walk forward for 'duration' seconds
    3. Give food to the dog
    4. Wal back for 'duration' seconds
    5. Logout of the game

Functions:
    - walk_to_food: walks until food bowl is available
    - give_food: activate food interaction and give food to the dog
    - walk_to_flower: walks until the flower is available
    - logout: logs out of the game
    - login: logs in to the game
    - run: main sequence to gain friendship with the bot
"""


import time

import pyautogui as pygui
import utils


def walk_to_food() -> None:
    """
    Walks the character until the food bowl is available and positioned within reach.

    The function uses pyautogui and the utils module to move the character to a
    position near the food bowl. It first walks forward for three seconds to get
    away from the starting position (usually the flower), then it continues to
    walk forward until it reaches the position of the food bowl, indicated by a
    white color. Finally, it turns around for half a second to position the
    character in front of the food bowl.
    """
    white = (255, 255, 255)
    item_available_position = (1100, 560)
    utils.actions.press_key_for_duration("w", 3)
    utils.actions.press_key_until_event(
        "w",
        utils.events.wait_for_color,
        item_available_position,
        white
    )
    utils.actions.press_key_for_duration("s", 0.1)


def give_food() -> None:
    """
    Activates the food interaction and gives food to the dog.

    This function presses the 'f' key to activate the food interaction and then clicks
    on the position (1060, 740) to give the food item to the dog.
    """
    interaction_key = "f"
    position = (1060, 740)
    pygui.press(interaction_key)
    pygui.click(position[0], position[1], 1)


def walk_to_flower() -> None:
    """
    Walks backward until the flower is available for interaction.

    Uses the 'utils.press_key_until_color()' function to continuously move backward
    ('s' key) until the white color at the position of the flower is detected on the
    screen. Then, turns around ('w' key) for a short duration of time.
    """
    white = (255, 255, 255)
    item_available_position = (1100, 560)

    utils.actions.press_key_for_duration("s", 3)
    utils.actions.press_key_until_event(
        "s",
        utils.events.wait_for_color,
        item_available_position,
        white
    )
    utils.actions.press_key_for_duration("w", 0.1)


def logout() -> None:
    """
    Logs out of the game and returns to the main menu.

    Presses the 'Esc' key to open the menu, waits until the menu appears,
    clicks the 'Exit' button, clicks the confirmation button to return to
    the main menu, and logs out of the game.
    """
    esc = "esc"
    exit_click = (210, 950)
    wait_position = (310, 450)
    confirmation_click = (1060, 740)
    color = (236, 229, 216)

    pygui.press(esc)
    utils.events.wait_for_color(wait_position, color)
    time.sleep(1)
    pygui.click(exit_click[0], exit_click[1], 1)
    time.sleep(1)
    pygui.click(confirmation_click[0], confirmation_click[1], 1)


def login() -> None:
    """
    Logs into the game by clicking through the
    initial screens until the login is confirmed.
    """
    click_center = (950, 600)
    white_color = (255, 255, 255)
    dark_gray_color = (34, 34, 34)

    # white screen after logout -> wait until no longer white
    wait_first = (250, 200)
    utils.events.wait_for_color(wait_first, white_color)
    time.sleep(1)
    pygui.click(click_center[0], click_center[1], 1)

    # welcome screen -> wait until logout button appears (black)
    wait_second = (240, 910)  # logout button
    utils.events.wait_for_color(wait_second, dark_gray_color)
    time.sleep(1)
    pygui.click(click_center[0], click_center[1], 1)

    # click to enter screen (door appears) -> wait until text at the bottom appears
    wait_third = (1690, 780)
    utils.events.wait_for_color(wait_third, white_color)
    time.sleep(1)
    pygui.click(click_center[0], click_center[1], 1)

    # wait until login is confirmed (blue part of paimon's head by the minimap)
    paimon_pos = (200, 170)
    paimon_color = (71, 114, 167)
    utils.events.wait_for_color(paimon_pos, paimon_color)
    time.sleep(1)


def run(iterations: int = 10) -> None:
    """
    Runs the main sequence to gain friendship with the bot.

    The sequence involves resetting and activating the event, logging
    back in to the game, walking to the food bowl, giving the food item
    to the bot, and walking back to the flower.
    """
    iterations = 10
    game = "Genshin Impact"

    utils.window.switch_to_window(game)

    print("The script needs to be run as admin to interact with the game")

    for i in range(iterations):
        logout()  # reset and activate event
        login()  # log back
        walk_to_food()  # walk to food bowl
        give_food()  # give the food item
        walk_to_flower()  # walk back to flower
        print(f"Iteration {i + 1} complete",  end="\r")
