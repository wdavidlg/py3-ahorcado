from random import choice


words = ["dinero", "invierno", "rodilla", "verano", "ojos", "pez", "taza", "tarta", "hojas", "rio"]

def getWord():
    return choice(words) 

def showWord(word, *args):
    hide = ""
    for letter in word:
        if letter in args:
            hide += letter + " "
        else:
            hide += "__ "
    return hide

def isLetterInWord(word, letter):
    return letter in word

def inputLetter():
    salir = False
    letter = ""
    while salir == False:
        letter = input("Ingrese una letra: ").lower()
        if(len(letter) > 1 or not letter.isalpha()):
            print("Error: la entrada debe ser una letra")
            continue
        salir = True
    return letter