#Spam Bot Created By Abhimanyu Sharma A.K.A N1nja0p
import pyautogui
import time
time.sleep(5)
if __name__ == "__main__":
    f=open("bee_movie_script.txt")
    for i in f:
        pyautogui.typewrite(i)
        pyautogui.press("enter")
