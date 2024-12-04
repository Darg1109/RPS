import random
import os
partidas = True
p1 = 0
p2 = 0
lista = [1, 2, 3]
jugadores = int(input("Modos de juego: 1. 1v1, 2. 1vPC: "))
if jugadores == 1:
    while partidas:
        print("Partida numero", partidas)
        partidas += 1
        j1 = int(input("""1. piedra
2. papel
3. tijera.
Ingrese su opcion en numero: """))
        j2 = int(input("""1. piedra
2. papel
3. tijera.
Ingrese su opcion en numero: """))
        if j1 == j2:
            print("Empate")
            p1 += 1
            p2 += 1
        elif j1 == j2-1:
            print("Gana jugador 2")
            p2 += 2
        elif j2 == j1-1:
            print("Gana jugador 1")
            p1 += 2
        elif j1 < j2:
            print("Gana jugador 1")
            p1 += 2
        elif j2 < j1:
            print("Gana jugador 2")
            p2 += 2
        condicion = int(input("Desea seguir jugando: 1. SI, 2. NO: "))
        if condicion == 2:
            partidas = False
        os.system("cls")
else:
    while partidas:
        print("Partida numero", partidas)
        partidas += 1
        j1 = int(input("""1. piedra
2. papel
3. tijera.
Ingrese su opcion en numero: """))
        j2 = random.choice(lista)
        if j1 == j2:
            print("Empate")
            p1 += 1
            p2 += 1
        elif j1 == j2-1:
            print("Gana jugador 2")
            p2 += 2
        elif j2 == j1-1:
            print("Gana jugador 1")
            p1 += 2
        elif j1 < j2:
            print("Gana jugador 1")
            p1 += 2
        elif j2 < j1:
            print("Gana jugador 2")
            p2 += 2
        condicion = int(input("Desea seguir jugando: 1. SI, 2. NO: "))
        if condicion == 2:
            partidas = False
        os.system("cls")
        
if p1 > p2:
    print("El juego ha terminado, el ganador es el jugador numero 1 con", p1, "puntos")
elif p1 < p2:
    print("El juego ha terminado, el ganador es el jugador numero 2 con", p2, "puntos")
else:
    print("El juego ha terminado, los jugadores acaban de empatar")