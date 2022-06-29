from ast import While
from imagesearch_org import *

# Random
def randomDelay(Sec, toSec):
    return round(random.uniform(Sec, toSec), random.randint(2, 5))

def pressKey(Key):
    pyautogui.keyDown(Key) # 按下
    time.sleep(randomDelay(0.1, 0.2))
    pyautogui.keyUp(Key) # 放開

def pressMouse(x, y, Delay):
    pyautogui.moveTo(x, y, duration=Delay, tween=pyautogui.easeInOutQuad)
    time.sleep(randomDelay(0.2, 0.3))
    pyautogui.mouseDown(x, y)
    time.sleep(randomDelay(0.1, 0.2))
    pyautogui.mouseUp(x, y)

def Repair():
    """ 叫出寵物界面 """
    pyautogui.keyDown('alt')
    time.sleep(randomDelay(0.1, 0.2))
    pressKey("P")
    time.sleep(randomDelay(0.1, 0.2))
    pyautogui.keyUp('alt')
    time.sleep(randomDelay(3.0, 3.5))
    """ 點擊修理工具 """
    pressMouse(1252, 689, 0.2)
    time.sleep(randomDelay(0.3, 0.4))
    """ 點擊修理全部 """
    pressMouse(1090, 682, 0.2)
    time.sleep(randomDelay(0.3, 0.4))
    """ 點擊退出 """
    pressMouse(1790, 1023, 0.2)
    time.sleep(randomDelay(1.5, 2.0))
    """ 關閉寵物界面 """
    pressMouse(1379, 205, 0.2)

def EnterAnywhere():
    """ 叫出綜合副本 """
    pyautogui.keyDown('alt')
    time.sleep(randomDelay(0.1, 0.2))
    pressKey("Q")
    time.sleep(randomDelay(0.1, 0.2))
    pyautogui.keyUp('alt')
    time.sleep(randomDelay(0.5, 0.7))

if __name__ == "__main__":

    time.sleep(3)

    while True:

        EnterAnywhere()

        time.sleep(600)

        Repair()

        time.sleep(600)
