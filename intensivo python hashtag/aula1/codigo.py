import pyautogui
import time
import pandas as pd
from pathlib import Path

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

#Importar os dados
PROJECT_DIR = Path(__file__).parent
path = PROJECT_DIR / 'produtos.csv'
tabela = pd.read_csv(path)

#Inserir os dados
for linha in tabela.index:
    pyautogui.click(x=591, y=333)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.scroll(-5000)
    pyautogui.click(x=624, y=745)
    pyautogui.scroll(5000)






