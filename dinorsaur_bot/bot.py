from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from selenium import webdriver

COLOR=(172,172,172)
X_CACTUS=680
Y_CACTUS=362
while True:
    while keyboard.is_pressed('q') == False:
        if pyautogui.pixel(X_CACTUS, Y_CACTUS) == COLOR:
            pyautogui.press('space')

