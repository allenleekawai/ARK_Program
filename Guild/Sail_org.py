# -*- coding:utf-8 -*-

import pathlib
from imagesearch_org import *

# Search for the logo on the whole screen
# note that the search only works on your primary screen
completePic     = str(pathlib.Path(__file__).parent.absolute()) + "\complete.png"
stopPic         = str(pathlib.Path(__file__).parent.absolute()) + "\stop.png"

if True: # 固定宣告

    # Random
    def randomDelay(Sec, toSec):
        return round(random.uniform(Sec, toSec), random.randint(2, 5))

    # Press Key
    def pressKey(Key):
        pyautogui.keyDown(Key) # 按下
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.keyUp(Key) # 放開

    # Press Mouse Left
    def pressMouse(x, y, Delay):
        pyautogui.moveTo(x, y, duration=Delay, tween=pyautogui.easeInOutQuad)
        time.sleep(randomDelay(0.2, 0.3))
        pyautogui.mouseDown(x, y)
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.mouseUp(x, y)

    # Press Mouse Right
    def pressMouseRight(x, y, Delay):
        pyautogui.moveTo(x, y, duration=Delay, tween=pyautogui.easeInOutQuad)
        time.sleep(randomDelay(0.2, 0.3))
        pyautogui.mouseDown(x, y, button='right')
        pyautogui.mouseUp(x, y, button='right')

if True: # 統一動作（修船）

    def Repair():
        """ 叫出船務界面 """
        pressKey("Z")
        time.sleep(randomDelay(0.4, 0.5))
        pressMouse(1433, 1017, 0.2)
        time.sleep(randomDelay(0.1, 0.2))
        pressMouse(1225, 630, 0.2)
        time.sleep(randomDelay(0.3, 0.4))
        pressKey("Esc")
        time.sleep(randomDelay(0.4, 0.5))

if True: # Find Pic

    def completePic_hwnd(hwnd): # 找尋任務完成圖示
        pos = imagesearch_hwnd_loop(completePic, hwnd, 0.1)
        print("Complete found ", pos[0], pos[1])

    def stopPic_hwnd(hwnd): # 找尋回到港口圖示
        pos = imagesearch_hwnd_loop(stopPic, hwnd, 0.1)
        print("Stop found ", pos[0], pos[1])

if True: # 跑船固定路線

    def Line1():
        """ 組合一 """
        # 點擊第二點
        pyautogui.keyDown('Alt')
        time.sleep(randomDelay(0.1, 0.2))
        pressMouse(1237, 275, 0.2)
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.keyUp('Alt')
        time.sleep(randomDelay(0.3, 0.4))

        # 點擊第三點
        pyautogui.keyDown('Alt')
        time.sleep(randomDelay(0.1, 0.2))
        pressMouse(931, 379, 0.2)
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.keyUp('Alt')
        time.sleep(randomDelay(0.3, 0.4))
        # 關閉地圖
        pressKey("Esc")

        # 等待任務完成圖示
        completePic_hwnd(hwnd)
        time.sleep(randomDelay(0.1, 0.2))
        # 點擊任務完成圖示
        pressMouse(2321, 389, 0.2)
        time.sleep(randomDelay(0.3, 0.4))
        # 點擊任務完成圖示
        pressMouse(354, 741, 0.2)
        time.sleep(randomDelay(0.3, 0.4))
        # 打開任務介面
        pyautogui.keyDown('alt')
        time.sleep(randomDelay(0.1, 0.2))
        pressKey("J")
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.keyUp('alt')
        time.sleep(randomDelay(0.7, 0.8))
        # 點擊公會委託
        pressMouse(1230, 776, 0.1)
        time.sleep(randomDelay(0.1, 0.2))
        # 接取航海任務
        pressMouse(1609, 321, 0.1)
        time.sleep(randomDelay(0.1, 0.2))
        # 關閉任務介面
        pressKey("Esc")
        time.sleep(randomDelay(0.3, 0.5))

        # 打開地圖
        pressKey("M")
        time.sleep(randomDelay(0.3, 0.5))
        pressMouse(1090, 505, 0.2)
        time.sleep(randomDelay(0.3, 0.5))
        """ 組合一 """

    def Line2():
        """ 組合二 """
        # 點擊第二點
        pyautogui.keyDown('Alt')
        time.sleep(randomDelay(0.1, 0.2))
        pressMouse(1237, 275, 0.2)
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.keyUp('Alt')
        time.sleep(randomDelay(0.3, 0.4))

        # 點擊第一點
        pyautogui.keyDown('Alt')
        time.sleep(randomDelay(0.1, 0.2))
        pressMouse(1542, 395, 0.2)
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.keyUp('Alt')
        time.sleep(randomDelay(0.3, 0.4))
        # 關閉地圖
        pressKey("Esc")

        # 等待任務完成圖示
        completePic_hwnd(hwnd)
        time.sleep(randomDelay(0.1, 0.2))
        # 點擊任務完成圖示
        pressMouse(2321, 389, 0.2)
        time.sleep(randomDelay(0.3, 0.4))
        # 點擊任務完成圖示
        pressMouse(354, 741, 0.2)
        time.sleep(randomDelay(0.3, 0.4))
        # 打開任務介面
        pyautogui.keyDown('alt')
        time.sleep(randomDelay(0.1, 0.2))
        pressKey("J")
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.keyUp('alt')
        time.sleep(randomDelay(0.7, 0.8))
        # 點擊公會委託
        pressMouse(1230, 776, 0.1)
        time.sleep(randomDelay(0.1, 0.2))
        # 接取航海任務
        pressMouse(1609, 321, 0.1)
        time.sleep(randomDelay(0.1, 0.2))
        # 關閉任務介面
        pressKey("Esc")
        time.sleep(randomDelay(0.3, 0.5))

        # 打開地圖
        pressKey("M")
        time.sleep(randomDelay(0.3, 0.5))
        pressMouse(1090, 505, 0.2)
        time.sleep(randomDelay(0.3, 0.5))
        """ 組合二 """

if __name__ == "__main__":

    time.sleep(3)
    hwnd = FindWindow_bySearch("LOST ARK")

    while True:

        pressKey("M")
        time.sleep(randomDelay(0.3, 0.5))
        pressMouse(1090, 505, 0.2)
        time.sleep(randomDelay(0.3, 0.5))

        pyautogui.keyDown('Alt')
        time.sleep(randomDelay(0.1, 0.2))
        pressMouse(1542, 395, 0.2)
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.keyUp('Alt')
        time.sleep(randomDelay(0.3, 0.4))

        for i in range(4):
            Line1()
            Line2()

        pyautogui.keyDown('Alt')
        time.sleep(randomDelay(0.1, 0.2))
        pressMouse(1667, 542, 0.2)
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.keyUp('Alt')
        time.sleep(randomDelay(0.3, 0.4))
        # 關閉地圖介面
        pressKey("Esc")

        time.sleep(randomDelay(5.0, 5.3))
        stopPic_hwnd(hwnd)
        time.sleep(randomDelay(0.3, 0.5))
        Repair()
        time.sleep(randomDelay(0.3, 0.5))

"""
# VK_Key_Code : http://www.kbdedit.com/manual/low_level_vk_list.html
VK_KEY_G = 0x47 # 進地牢 G
VK_KEY_C = 0x43 # 普攻 C
VK_RETURN = 0x0D # Enter

VK_KEY_Q = 0x51 # Q
VK_KEY_W = 0x57 # W
VK_KEY_E = 0x45 # E
VK_KEY_R = 0x52 # R

VK_KEY_A = 0x41 # A
VK_KEY_S = 0x53 # S
VK_KEY_D = 0x44 # D
VK_KEY_F = 0x46 # F

VK_LMENU = 0xA4 # Left ALT
VK_RMENU = 0xA5 # Right ALT
VK_KEY_P = 0x50 # P
VK_ESCAPE = 0x1B # Esc
"""
