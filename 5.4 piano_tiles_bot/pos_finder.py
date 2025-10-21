from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from selenium import webdriver

color=(172,172,172)

while True:
    x,y=pyautogui.position()
    print(f"x={x} y={y}",end="\r")

