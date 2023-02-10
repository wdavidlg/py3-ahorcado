
# Nota: *args es la propagacion de una lista.
# **kwargs sirve para tratar parametros con palabra clave y lo traduce a un diccionario
# Ejemplo: sum(a=2, b=4),
# def sum(**kwargs)

# Cuando se quiere utilizar *args y **kwargs en una misma funcion se recomienda el siguiente orden:
# def funcion( a, b, *args, **kwargs)

from palabras import getWord, showWord, isLetterInWord, inputLetter

correctLetters = set()
incorrectLetters = set()
vidas = 6
word = getWord()
letter = ""
gano = False

while vidas != 0 and gano == False:
    print("----------------------------------------------------------------------------")
    print("\t\t\tJUEGO DEL AHORCADO")
    print("\t\t\t\t\t\t\tVidas: ", vidas)
    print("\t\t\t",showWord(word, *correctLetters))
    print()
    letter = inputLetter()
    if( isLetterInWord(word, letter) ):
        correctLetters.add(letter)
    else:
        incorrectLetters.add(letter)
        vidas -= 1
    print("----------------------------------------------------------------------------")
    if(len(correctLetters) == len(word)):
        gano = True

if(gano):
    print("FELICIDADES HAS GANADO")
    print("LA PALABRA ES ", word.upper())
else:
    print("Perdiste, la palabra era ", word)