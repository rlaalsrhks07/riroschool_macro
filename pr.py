import pyautogui
from PIL import Image

location = None
while location is None:
    location = pyautogui.locateOnScreen("jungjung.png", grayscale=True, confidence=0.6)
pyautogui.scroll(-4890)

pyautogui.click(552,383)

pyautogui.scroll(-1000)

pyautogui.click(552,528)

pyautogui.scroll(-530)

pyautogui.click(1025,527)