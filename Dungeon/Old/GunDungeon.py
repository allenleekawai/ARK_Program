# -*- coding:utf-8 -*-

from imagesearch_org import *

# Search for the logo on the whole screen
# note that the search only works on your primary screen
admissionPic    = "enter.png"
dungeonPic      = "exit.png"
deadPic         = "dead.png"

if True: # 固定宣告

    # Random
    def randomDelay(Sec, toSec):
        return round(random.uniform(Sec, toSec), random.randint(2, 5))

    # Press Key
    def pressKey(Key):
        pyautogui.keyDown(Key) # 按下
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.keyUp(Key) # 放開

    # Press Mouse
    def pressMouse(x, y, Delay):
        pyautogui.moveTo(x, y, duration=Delay, tween=pyautogui.easeInOutQuad)
        time.sleep(randomDelay(0.2, 0.3))
        pyautogui.mouseDown(x, y)
        time.sleep(randomDelay(0.1, 0.2))
        pyautogui.mouseUp(x, y)

if True: # 統一動作（修武器、死亡）

    def Enter():
        """ 抓到入場圖片，按G入場 """
        admissionPic_hwnd(hwnd)
        time.sleep(randomDelay(1.5, 2.0))
        pressKey("G")
        time.sleep(randomDelay(0.4, 0.5))
        pyautogui.moveTo(1533, 864, duration=randomDelay(0.2, 0.3), tween=pyautogui.easeInOutQuad) # 移到場地正中間
        pressMouse(1533, 864, 0.2)
        time.sleep(randomDelay(0.9, 1.1))
        pressKey("enter")

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

    def Dead():
        global deadCounter
        pos = imagesearch_hwnd(deadPic, hwnd)
        if pos == [-1, -1]:
            return False
        else:
            print("Dead found ", pos[0], pos[1])
            deadCounter = deadCounter + 1
            return True

    def deadExit():
        pressMouse(1373, 480, 0.2)
        time.sleep(randomDelay(0.8, 1.0))
        pressKey("enter")

if True: # Find Pic

    def admissionPic_hwnd(hwnd): # 找尋入場可以按G的照片
        counter = 0
        pos = imagesearch_hwnd(admissionPic, hwnd)
        while pos[0] == -1:
            print(admissionPic + " not found, waiting")
            time.sleep(0.1)
            pos = imagesearch_hwnd(admissionPic, hwnd)
            counter += 1
            if counter == 100:
                break
            print(counter)
        print("Admission found ", pos[0], pos[1])
        return pos

    def dungeonPic_hwnd(hwnd): # 找尋入場後的退出鈕
        counter = 0
        pos = imagesearch_hwnd(dungeonPic, hwnd)
        while pos[0] == -1:
            print(dungeonPic + " not found, waiting")
            time.sleep(0.1)
            pos = imagesearch_hwnd(dungeonPic, hwnd)
            counter += 1
            if counter == 100:
                break
            print(counter)
        print("Dungeon inside found ", pos[0], pos[1])
        return pos

if __name__ == "__main__":
    runCounter  = 0
    deadCounter = 0

    time.sleep(3)
    hwnd = FindWindow_bySearch("LOST ARK")

    while True:

        while True:

            """ 抓到入場圖片，按G入場 """
            Enter()
            time.sleep(randomDelay(3.0, 3.5))
            dungeonPic_hwnd(hwnd)
            time.sleep(randomDelay(1.5, 2.0))

            """ 入場後普攻，觸發怪物生成 """
            pyautogui.moveTo(958, 528, duration=randomDelay(0.1, 0.2), tween=pyautogui.easeInOutQuad) # 移到場地正中間
            time.sleep(randomDelay(0.1, 0.2))
            pressKey("C")
            time.sleep(randomDelay(7.5, 7.8))

            pressKey("R")
            time.sleep(randomDelay(7.5, 7.8))
            pressKey("X")
            time.sleep(randomDelay(2.5, 2.8))

            """ 偵測是否死亡 """
            if Dead():
                time.sleep(randomDelay(5.0, 5.5))
                deadExit()
                break

            pressKey("S")
            time.sleep(randomDelay(5.6, 5.8))
            pressKey("Z")
            time.sleep(randomDelay(0.3, 0.5))
            pressKey("X")
            time.sleep(randomDelay(0.3, 0.5))
            pyautogui.moveTo(958, 528, duration=randomDelay(0.1, 0.2), tween=pyautogui.easeInOutQuad) # 移到場地正中間
            pressKey("W")
            time.sleep(randomDelay(0.5, 0.8))

            pyautogui.moveTo(958, 528, duration=randomDelay(0.1, 0.2), tween=pyautogui.easeInOutQuad) # 移到場地正中間
            pressKey("E")
            time.sleep(randomDelay(0.5, 0.8))
            pressKey("E")
            time.sleep(randomDelay(0.5, 0.8))
            pressKey("E")
            time.sleep(randomDelay(1.0, 1.3))

            pyautogui.moveTo(958, 528, duration=randomDelay(0.1, 0.2), tween=pyautogui.easeInOutQuad) # 移到場地正中間
            pressKey("R")
            time.sleep(randomDelay(0.2, 0.5))
            pressKey("R")
            time.sleep(randomDelay(0.2, 0.5))
            pressKey("R")
            time.sleep(randomDelay(7.6, 7.8))

            """ 偵測是否死亡 """
            if Dead():
                time.sleep(randomDelay(5.0, 5.5))
                deadExit()
                break

            pressKey("Z")
            time.sleep(randomDelay(0.3, 0.5))
            pressKey("X")
            time.sleep(randomDelay(0.3, 0.5))
            pressKey("S")
            time.sleep(randomDelay(7.5, 7.8))

            """ 偵測是否死亡 """
            if Dead():
                time.sleep(randomDelay(5.0, 5.5))
                deadExit()
                break

            pressKey("Z")
            time.sleep(randomDelay(2.0, 2.3))
            pressKey("R")
            time.sleep(randomDelay(1.4, 1.7))

            """ 偵測是否死亡 """
            if Dead():
                time.sleep(randomDelay(5.0, 5.5))
                deadExit()
                break
            
            """ 點選退出 > Enter """
            pressMouse(129, 284, 0.2)
            time.sleep(randomDelay(0.4, 0.5))
            pressKey("enter")

            """ 偵測是否死亡 """
            time.sleep(randomDelay(3.0, 3.3))
            if Dead():
                time.sleep(randomDelay(5.0, 5.5))
                deadExit()
                break

            runCounter = runCounter + 1
            print("Run:  ", runCounter)
            print("Dead: ", deadCounter)

            Hour = int(time.strftime("%H", time.localtime()))
            Min  = int(time.strftime("%M", time.localtime()))
            if Hour == 17 and ((Min == 57) or (Min == 58) or (Min == 59)):
                while True:
                    Repair()
                    time.sleep(600)

        time.sleep(randomDelay(3.0, 3.5))
        admissionPic_hwnd(hwnd)
        time.sleep(randomDelay(2.0, 2.5))
        Repair()

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
