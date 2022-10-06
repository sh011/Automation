import time

# It can be installed using the basic cmd command:
# pip install time
import pyautogui
time.sleep(10)

# This makes program execution pause for 10 sec
pyautogui.moveTo(1000, 1000, duration=1)

# This moves mouse to 1000, 1000.
pyautogui.dragRel(100, 0, duration=1)

# drags mouse 100, 0 relative to its previous position,
# thus dragging it to 1100, 1000
pyautogui.dragRel(0, 100, duration=1)
pyautogui.dragRel(-100, 0, duration=1)
pyautogui.dragRel(0, -100, duration=1)
