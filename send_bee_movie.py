import pyautogui
from time import sleep


def get_words():
    with open("script.txt", "r") as script:
        for word in script:
            yield word.strip()


sleep(5)  # better get your cursor ready!!!

for _ in get_words():
    pyautogui.typewrite(_)
    pyautogui.press("enter")
