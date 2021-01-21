import pyautogui
import time
time.sleep(5)
f=open("bee_movie_script.txt")
for i in f:
    pyautogui.typewrite(i)
    pyautogui.press("enter")