import pyautogui
import time
while True:
    n = input("")
    if(n==''):
        exit()
    img = pyautogui.locateOnScreen('img/clickit.png')
    q= pyautogui.center(img)
    pyautogui.click(q)
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(2)
