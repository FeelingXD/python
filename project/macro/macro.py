import pyautogui
import msvcrt as ms

img = pyautogui.locateOnScreen('clickit.png')
img_center = pyautogui.center(img)

while True:
    pyautogui.click(img_center)
    pyautogui.press('enter')
    pyautogui.press('enter')
    key = ms.getch().decode('ASCII')
    if(key!='\n'):
        exit()
