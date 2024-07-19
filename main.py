# Imports

import pyautogui, os

def error():
    my_screenshot = pyautogui.screenshot() # Screenshot recovery.
    my_screenshot.save(r"logs\ss.png") # Saving the screenshot.


os.system('cls') # Your code.
