import pyautogui
import time

time.sleep(5)
print(pyautogui.position())
pyautogui.alert(text='Local do mouse definido', title='Mouse', button='OK')