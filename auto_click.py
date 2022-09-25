import time
import pyautogui


def mouse_click(x1,y1,x2,y2):
    while True:
        for i in range(30):
            pyautogui.moveTo(x1,y1)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveTo(x2,y2)
            pyautogui.click()
            time.sleep(1)
        time.sleep(10)
# print("10病後に開始しますウインドウを用意してください")
# time.sleep(10)#10秒後に開始します

while True:
    mouse_click(1314,689,1283,507)#この部分にx座標y座標を埋め込んで実行しよう