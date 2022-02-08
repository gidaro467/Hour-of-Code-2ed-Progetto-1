import re

while True:
    password = input("Password da stampare: ")

    valida = True
    if len(password) < 8:
        print("La password deve essere lunga almeno 8 caratteri")
        valida = False


    if not re.search("[A-Z]+",password):
        print("La password deve contenere almeno un carattere maiuscolo")
        valida = False

    if not re.search("[a-z]+",password):
        print("La password deve contenere almeno un carattere minuscolo")
        valida = False
    
    if not re.search("[0-9]+",password):
        print("La password deve contenere almeno un numero")
        valida = False

    if not re.search("[\.,_\-]+", password):
        print(" La password deve contenere almeno un carattere speciale: .,_-")
        valida = False

    if valida:
        print("password valida")
        break
    else:
        continue


print("Chiudo il programma.")