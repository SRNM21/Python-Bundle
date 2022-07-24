import time
import pyautogui

time.sleep(5)

spam = 0
msg = "ML KAYA LODS"

while spam <= 10:
    pyautogui.typewrite(msg)
    pyautogui.press('enter')
    spam = spam + 1
