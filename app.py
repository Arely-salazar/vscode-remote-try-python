#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random


#definimos una funcion para el elemento random
def random_element():
    
    return random.choice(["rock", "paper", "scissors"]) #elementos random para el juego

#definimos una funcion para jugar
def jugar():
    
    print("-----Bienvenido al juego------. \nDe las siguientes opciones: \nRock \nPaper \nScissors")
    menu_op = input("Elija una: ")

    elemento = random_element() #variable para el elemento random
    global victorias #variable global para contar las victorias

    if menu_op.lower()== "rock":
        if elemento == "rock": #si el elemento random es igual a rock es empate
            print(f"Opción del oponente: {elemento}")
            print("Empate")

        elif elemento == "paper": #si el elemento random es igual a paper pierde
            print(f"Opción del oponente: {elemento}")
            print("Perdiste")
            
        elif elemento == "scissors": #si el elemento random es igual a scissors gana
            print(f"Opción del oponente: {elemento}")
            print("Ganaste")
            victorias += 1 #se suma una victoria a la variable global

    elif menu_op.lower() == "paper":
        if elemento == "rock":
            print(f"Opción del oponente: {elemento}")
            print("Ganaste")
            victorias += 1
            
        elif elemento == "paper":
            print(f"Opción del oponente: {elemento}")
            print("Empate")
            
        elif elemento == "scissors":
            print(f"Opción del oponente: {elemento}")
            print("Perdiste")
            

    elif menu_op.lower() == "scissors":
        if elemento == "rock":
            print(f"Opción del oponente: {elemento}")
            print("Perdiste")

        elif elemento == "paper":
            print(f"Opción del oponente: {elemento}")
            print("Ganaste")
            victorias += 1

        elif elemento == "scissors":
            print(f"Opción del oponente: {elemento}")
            print("Empate")

    else:
        print("Opción incorrecta")


victorias = 0 #variable para contar las victorias
rondas = 0 #variable para contar las rondas

#bucle para jugar de nuevo
while True:
    jugar()

    rondas += 1 #se suma una ronda
    
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (SI/NO): ")
    if jugar_de_nuevo.lower() != 'si':
        break       #si la respuesta es diferente a si se rompe el bucle

print(f"Puntuacion final: {victorias}. \nRondas jugadas: {rondas}")