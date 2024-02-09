# _*_ coding: utf8 _*_
import pyautogui
import time

pyautogui.PAUSE = 0.3
municipios = ['Londrina', 'Angelina', 'Joinville']

for municipio in municipios:

    #passo 1 acessar o site do cadprev
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")

    pyautogui.write("https://cadprev.previdencia.gov.br/Cadprev/pages/index.xhtml")
    pyautogui.press("enter")
    time.sleep(1)

    #passo 2 pesquisa do município
    #ClicK Consultas Públicas
    pyautogui.click(x=101, y=246)
    time.sleep(1)

    #ClicK DRAA
    pyautogui.click(x=120, y=377)
    time.sleep(1)

    #Click Consultar Demonstrativos após 2014
    pyautogui.click(x=93, y=461)
    time.sleep(1)

    #selecionar ente
    pyautogui.click(x=1150, y=239)
    time.sleep(1)

    #escreve o nome do ente
    pyautogui.click(x=942, y=240)
    pyautogui.write(str(municipio))
    pyautogui.press('enter')
    time.sleep(3)

    #Click Pesquisar
    ok = pyautogui.locateOnScreen('ok.png')
    pyautogui.click(pyautogui.center(ok))
    time.sleep(1)

    #Click selecionar
    pyautogui.click(x=1381, y=365)
    time.sleep(2)

    #escreve o exercicio
    pyautogui.click(x=694, y=265)
    exercicio = '2023'
    pyautogui.write(str(exercicio))
    time.sleep(1)

    #autenticador recaptcha
    pyautogui.click(x=926, y=388)
    time.sleep(2)

    #Click consultar
    pyautogui.click(x=1035, y=445)
    time.sleep(2)

    #Click baixar
    pyautogui.click(x=793, y=536)
    time.sleep(3)