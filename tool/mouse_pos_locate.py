import pyautogui
import time

while True:
    mouse_pos = pyautogui.position()
    if mouse_pos[0] == 0 or mouse_pos[1] == 0:
        break
    print(mouse_pos)
    time.sleep(1)
