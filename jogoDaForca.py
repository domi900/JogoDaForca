from tkinter.constants import S
import PySimpleGUI as sg
from random import randint

from PySimpleGUI.PySimpleGUI import Button, POPUP_BUTTONS_OK, POPUP_BUTTONS_YES_NO, popup, popup_ok

sg.theme('Dark')
palavras = ("cama", "caneca", "celular", "copo", "faca", "garfo", "basquete", "futebol", "volei")
dicas =  ("Quarto",  "Cozinha", "Comunicação", "Cozinha", "Cozinha", "Cozinha", "Esporte", "Esporte", "Esporte")

def graves(p):
    a = ""
    for x in range(len(p)):
        a += p[x]
        a += " "
    return a

def testar_letra(letra, palavra, pO):
    if letra in palavra and letra != "":
        new_pO = ""
        for c in range(len(palavra)):
            if letra[0] == palavra[c]:
                new_pO += letra[0]
            else:
                if pO[c] == "_":
                    new_pO += "_"
                else:
                    new_pO += pO[c]
        return new_pO
    else:
        return pO

def ocultar_palavra(p):
    pO = ""
    for c in range(len(p)):
        pO += "_"
    return pO



indice = randint(0, len(palavras) - 1)
palavra_escolhida = palavras[indice]
dica_da_palavra = dicas[indice]

imagens = (r"python/images/Img0.png", r"python/images/Img1.png", r"python/images/Img2.png",
        r"python/images/Img3.png", r"python/images/Img4.png",
         r"python/images/Img5.png", r"python/images/Img6.png" )

cont = 0
image = imagens[cont]
palavraOculta = ocultar_palavra(palavras[indice])


coluna_1 = [[sg.Image(image, key="-IMAGE-")],
            [sg.Text("Dica: " + dicas[indice], size = (20,1))]]
coluna_2 = [[sg.Text(graves(palavraOculta), key="-pO-")],
            
            [sg.Text("Palavra"), sg.Input(k= "a", size = (10,1), key='-in2-',do_not_clear=False)]],[sg.Text("Letra"), sg.Input(k = 'in',size = (2,1), key='-in-', do_not_clear=False),
            [sg.Button("OK",size=(25,1))]]

layout = [coluna_1, coluna_2]

window = sg.Window("Demo", layout, element_justification="center")

while True:
    event, values = window.read()
    
    pontos = len(palavra_escolhida)
    
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "OK":
        if values['-in2-'] != "":
            s = values['-in2-']
            if s.strip().lower() == palavra_escolhida:
                sg.popup(f"sua pontuação foi {pontos}")
                break
            else:
                sg.popup("voce perdeu.", button_type=POPUP_BUTTONS_OK)
                break
        else:    
            a = values['-in-'].lower()
            print(a)
            nova_palavra_oculta = testar_letra(a, palavras[indice], palavraOculta)
            if  nova_palavra_oculta != palavraOculta:
                palavraOculta = nova_palavra_oculta
            else:    
                if cont < 6:
                    cont += 1
                    image = imagens[cont]
                    pontos -= 1
                else:
                    sg.popup("voce perdeu.", button_type=POPUP_BUTTONS_OK)
                    break
                
    print(palavraOculta)
    
    window["-IMAGE-"].update(image)
    window["-pO-"].update(graves(palavraOculta))
    if palavraOculta == palavras[indice]:
        sg.popup(f"sua pontuação foi {pontos}")
        break
window.close
