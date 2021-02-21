import pyautogui
import time
import img_hash
import numpy
from PIL import Image
import os

# pyautogui.click(1225, 360)
# pyautogui.moveTo(5,5)
# time.sleep(1)
# for i in pyautogui.locateAllOnScreen("back_ld.png"):
#     print(i)
reg = (10, 41, 37, 20)
ss: Image = pyautogui.screenshot(region=reg)
ss.save("back_ss.png")
