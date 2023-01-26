import os 
os.system("cls")

import random

letras_minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letras_mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["!", "#", "$", "%", "&"]

caracteres = letras_minusculas + letras_mayusculas + numeros + simbolos

tamano = int(input("Cuantos caracteres deberia tener tu contraseña?: "))

primer_caracter = random.choice(letras_minusculas)
segundo_caracter = random.choice(letras_mayusculas)
tercer_caracter = random.choice(numeros)
cuarto_caracter = random.choice(simbolos)

contrasena = [primer_caracter, segundo_caracter, tercer_caracter, cuarto_caracter]

for i in range(tamano - 4):
    caracter = random.choice(caracteres)
    contrasena.append(caracter)

random.shuffle(contrasena)
contrasena = "".join(contrasena)

print(contrasena)