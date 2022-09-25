import pyautogui
import time

print("10秒後に座標を取得します")
time.sleep(3)

x,y = pyautogui.position()
print(f"({x},{y})")