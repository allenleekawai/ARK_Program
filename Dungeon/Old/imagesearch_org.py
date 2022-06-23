# -*- coding:utf-8 -*-

import re
import cv2
import time
import random
import pyautogui
import numpy as np

import win32ui
import win32gui
import win32con

def FindWindow_bySearch(pattern):
    window_list = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), window_list)
    for each in window_list:
        if re.search(pattern, win32gui.GetWindowText(each)) is not None:
            return each

def getWindow_W_H(hwnd):
    # 取得目標視窗的大小
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    width = right - left - 15
    height = bot - top - 11
    return (left, top, width, height)

def getWindow_Img(hwnd):
    # 將 hwnd 換成 WindowLong
    s = win32gui.GetWindowLong(hwnd,win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, s|win32con.WS_EX_LAYERED)
    # 判斷視窗是否最小化
    show = win32gui.IsIconic(hwnd)
    # 將視窗圖層屬性改變成透明
    # 還原視窗並拉到最前方
    # 取消最大小化動畫
    # 取得視窗寬高
    if show == 1:
        win32gui.SystemParametersInfo(win32con.SPI_SETANIMATION, 0)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 0, win32con.LWA_ALPHA)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        x, y, width, height = getWindow_W_H(hwnd)
    # 創造輸出圖層
    hwindc = win32gui.GetWindowDC(hwnd)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    # 取得視窗寬高
    x, y, width, height = getWindow_W_H(hwnd)
    # 如果視窗最小化，則移到Z軸最下方
    if show == 1: win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, x, y, width, height, win32con.SWP_NOACTIVATE)
    # 複製目標圖層，貼上到 bmp
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0 , 0), (width, height), srcdc, (8, 3), win32con.SRCCOPY)
    # 將 bitmap 轉換成 np
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height, width, 4) #png，具有透明度的
    # 釋放device content
    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())
    # 還原目標屬性
    if show == 1 :
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
        win32gui.SystemParametersInfo(win32con.SPI_SETANIMATION, 1)
    # 回傳圖片
    return img

'''
grabs a region (topx, topy, bottomx, bottomy)
to the tuple (topx, topy, width, height)

input : a tuple containing the 4 coordinates of the region to capture
output : a PIL image of the area selected.
'''
def region_grabber(region):
    x1 = region[0]
    y1 = region[1]
    width = region[2]-x1
    height = region[3]-y1

    return pyautogui.screenshot(region=(x1,y1,width,height))

'''
Searchs for an image within an area

input :
image : path to the image file (see opencv imread for supported types)
x1 : top left x value
y1 : top left y value
x2 : bottom right x value
y2 : bottom right y value
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
im : a PIL image, usefull if you intend to search the same unchanging region for several elements

returns : the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not
'''
def imagesearcharea(image, x1, y1, x2, y2, precision=0.8, im=None) :
    if im is None :
        im = region_grabber(region=(x1, y1, x2, y2))
        #im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc

'''
click on the center of an image with a bit of random.
eg, if an image is 100*100 with an offset of 5 it may click at 52,50 the first time and then 55,53 etc
Usefull to avoid anti-bot monitoring while staying precise.

this function doesn't search for the image, it's only ment for easy clicking on the images.

input :
image : path to the image file (see opencv imread for supported types)
pos : array containing the position of the top left corner of the image [x,y]
action : button of the mouse to activate : "left" "right" "middle", see pyautogui.click documentation for more info
time : time taken for the mouse to move from where it was to the new position
'''
def click_image(image, pos, action, timestamp, offset=5):
    img = cv2.imread(image)
    height, width, channels = img.shape
    pyautogui.moveTo(pos[0] + r(width / 2, offset), pos[1] + r(height / 2,offset),
                     timestamp)
    pyautogui.click(button=action)

'''
Searchs for an image on the screen

input :
image : path to the image file (see opencv imread for supported types)
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
im : a PIL image, usefull if you intend to search the same unchanging region for several elements

returns : the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not
'''
def imagesearch(image, precision=0.8):
    im = pyautogui.screenshot()
    #im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1,-1]
    return max_loc

def imagesearch_hwnd(image, hwnd, precision=0.8):
    im = getWindow_Img(hwnd)
    #im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1,-1]
    return max_loc

'''
Searchs for an image on screen continuously until it's found.

input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image 
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8

returns : the top left corner coordinates of the element if found as an array [x,y] 
'''
def imagesearch_loop(image, timesample, precision=0.8):
    pos = imagesearch(image, precision)
    while pos[0] == -1:
        print(image+" not found, waiting")
        time.sleep(timesample)
        pos = imagesearch(image, precision)
    return pos

def imagesearch_hwnd_loop(image, hwnd, timesample, precision=0.8):
    pos = imagesearch_hwnd(image, hwnd, precision)
    while pos[0] == -1:
        print(image+" not found, waiting")
        time.sleep(timesample)
        pos = imagesearch_hwnd(image, hwnd, precision)
    return pos

'''
Searchs for an image on screen continuously until it's found or max number of samples reached.

input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image
maxSamples: maximum number of samples before function times out.
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8

returns : the top left corner coordinates of the element if found as an array [x,y] 
'''
def imagesearch_numLoop(image, timesample, maxSamples, precision=0.8):
    pos = imagesearch(image, precision)
    count = 0
    while pos[0] == -1:
        print(image+" not found, waiting")
        time.sleep(timesample)
        pos = imagesearch(image, precision)
        count = count + 1
        if count > maxSamples:
            break
    return pos

'''
Searchs for an image on a region of the screen continuously until it's found.

input :
image : path to the image file (see opencv imread for supported types)
time : Waiting time after failing to find the image 
x1 : top left x value
y1 : top left y value
x2 : bottom right x value
y2 : bottom right y value
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8

returns : the top left corner coordinates of the element as an array [x,y] 
'''
def imagesearch_region_loop(image, timesample, x1, y1, x2, y2, precision=0.8):
    pos = imagesearcharea(image, x1,y1,x2,y2, precision)

    while pos[0] == -1:
        time.sleep(timesample)
        pos = imagesearcharea(image, x1, y1, x2, y2, precision)
    return pos

'''
Searches for an image on the screen and counts the number of occurrences.

input :
image : path to the target image file (see opencv imread for supported types)
precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8

returns : the number of times a given image appears on the screen.
optionally an output image with all the occurances boxed with a red outline.
'''
def imagesearch_count(image, precision=0.8):
    img_rgb = pyautogui.screenshot()
    img_rgb = np.array(img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= precision)
    count = 0
    for pt in zip(*loc[::-1]):  # Swap columns and rows
        #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2) // Uncomment to draw boxes around found occurances
        count = count + 1
    #cv2.imwrite('result.png', img_rgb) // Uncomment to write output image with boxes drawn around occurances
    return count

def r(num, rand):
    return num + rand*random.random()
