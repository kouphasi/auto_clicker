import time
import pyautogui
import keyboard


def mouse_click(x1, y1, x2, y2):
    for i in range(30):
        if keyboard.is_pressed("q"):
            break
        pyautogui.moveTo(x1, y1)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(x2, y2)
        pyautogui.click()
        time.sleep(1)
    time.sleep(10)


# print("10病後に開始しますウインドウを用意してください")
# time.sleep(10)#10秒後に開始します

mouse_click(1314, 689, 1283, 507)  # この部分にx座標y座標を埋め込んで実行しよう
