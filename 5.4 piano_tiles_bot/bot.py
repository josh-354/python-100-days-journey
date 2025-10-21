from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from selenium import webdriver

#https://www.primarygames.com/arcade/music/pianotiles/mobile/
FIRST_X_POS=223
SECOND_X_POS=719
THIRD_X_POS=1182
FOURTH_X_POS=1704
Y_POS=502
COLOR=0,0,0

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
print("bot running (press q to exit)")

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(FIRST_X_POS, Y_POS) == COLOR:
        click(FIRST_X_POS, Y_POS)
    if pyautogui.pixel(SECOND_X_POS, Y_POS) == COLOR:
        click(SECOND_X_POS, Y_POS)
    if pyautogui.pixel(THIRD_X_POS, Y_POS) == COLOR:
        click(THIRD_X_POS, Y_POS)
    if pyautogui.pixel(FOURTH_X_POS, Y_POS) == COLOR:
        click(FOURTH_X_POS, Y_POS)

print("Exiting Bot")