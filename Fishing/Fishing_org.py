# -*- coding:utf-8 -*-

from ImageSearch_org import *

# Search for the logo on the whole screen
# note that the search only works on your primary screen
admissionPic    = str(pathlib.Path(__file__).parent.absolute()) + "/fish.png"
fishPic         = str(pathlib.Path(__file__).parent.absolute()) + "/fish1.png"
        
# RandomA
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
    time.sleep(randomDelay(2.0, 2.5))
    """ 點擊修理工具 """
    pressMouse(1289, 692, 0.3)
    time.sleep(randomDelay(0.3, 0.4))
    """ 點擊修理全部 """
    pressMouse(877, 745, 0.3)
    time.sleep(randomDelay(0.3, 0.4))
    """ 確認修理 """
    pressKey("enter")
    time.sleep(randomDelay(1.0, 1.5))
    """ 點擊退出 """
    pressMouse(1790, 1023, 0.3)
    time.sleep(randomDelay(1.5, 2.0))
    """ 關閉寵物界面 """
    pressMouse(1379, 205, 0.3)

# Find Pic
if True:
    def admissionPic_hwnd(hwnd): # 找尋魚龍可以按G的照片
        pos = imagesearch_hwnd_loop(admissionPic, hwnd, 0.1)
        print("Admission found ", pos[0], pos[1])

    def fishPic_hwnd(hwnd): # 找尋釣魚驚嘆號
        counter = 0
        pos = imagesearch_hwnd(fishPic, hwnd)
        while pos[0] == -1:
            print(fishPic + " not found, waiting")
            time.sleep(0.1)
            pos = imagesearch_hwnd(fishPic, hwnd)
            counter += 1
            if counter == 100:
                break
            print(counter)
        return pos

if __name__ == "__main__":
    runCounter  = 0

    time.sleep(3)
    hwnd = FindWindow_bySearch("LOST ARK")
    VK_KEY_A = 0x41

    while True:

        for i in range(40):
            """ 按A拋竿 """
            print("---------- Reload ----------")
            pyautogui.moveTo(1178, 227, duration=randomDelay(0.2, 0.3), tween=pyautogui.easeInOutQuad) # 移到水中
            win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, VK_KEY_A, 0)
            time.sleep(0.1)
            win32gui.PostMessage(hwnd, win32con.WM_KEYUP, VK_KEY_A, 0)
            time.sleep(randomDelay(1.0, 1.5))
            fishPic_hwnd(hwnd)
            win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, VK_KEY_A, 0)
            time.sleep(0.1)
            win32gui.PostMessage(hwnd, win32con.WM_KEYUP, VK_KEY_A, 0)
            time.sleep(randomDelay(6.5, 6.6))

            runCounter = runCounter + 1
            print("Run:  ", runCounter)

        time.sleep(randomDelay(0.4, 0.6))
        Repair()
        time.sleep(randomDelay(1.0, 1.2))
