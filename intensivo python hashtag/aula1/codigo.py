import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5
#Entrar no navegador
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey("ctrl","t")

#Acesssar o formulario(é falso, só para fins de aprendizado)
pyautogui.write("file:///C:/Users/Jo%C3%A3o%20Pedro/Documents/Treinos%20de%20python/Treino-python/intensivo%20python%20hashtag/aula1/site/form.html")
pyautogui.press("enter")
time.sleep(2)

#Inserir os dados
