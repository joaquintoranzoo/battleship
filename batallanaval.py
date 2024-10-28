"""
Realizar un programa que permita jugar al popular juego batalla naval. El programa consiste definir dos matrices
de 5x5 y solicitarles a los usuarios 1 y 2 respectivamente, las coordenadas para acomodar sus 5 barcos.
Una vez dispuestos los barcos de cada jugador, se comenzara a pedir que se den las coordenadas de disparo,
mostrando en pantalla los disparos ya realizados y las consecuencias de los mismos (hundido o agua), una
vez realizado el disparo el programa debe informar la consecuencia del mismo y pasar al otro jugador.
En el caso que un jugador hunda todos los barcos del otro jugador, se lo declara ganador.
El programa debe dar la opción de repetirse con una opción.
"""

print("Bienvenido a Batalla Naval")

nombrejugador1 = input("Ingrese el nombre del primer jugador: ")
nombrejugador2 = input("Ingrese el nombre del segundo jugador: ")

def mostrar_tablero(tablero):
    for fila in tablero:
        for celda in fila:
            print(celda, end=" ")
        print()
    print()

def colocar_barcos(tablero):
    for i in range(5):
        while True:
            x = int(input(f"Ingrese la coordenada X para el barco {i + 1} (0-4): "))
            y = int(input(f"Ingrese la coordenada Y para el barco {i + 1} (0-4): "))
            
            if 0 <= x <= 4 and 0 <= y <= 4:
                if tablero[x][y] == 0:  
                    tablero[x][y] = 1
                    break  
                else:
                    print("Ya hay un barco en esa posición, elija otra.")
            else:
                print("Coordenadas fuera del rango permitido. Ingrese nuevamente.")

def realizar_disparo(tablero, x, y):
    if tablero[x][y] == 1:
        tablero[x][y] = "X"
        return "Hundido"
    else:
        tablero[x][y] = "-"
        return "Agua"

def todos_barcos_hundidos(tablero):
    for fila in tablero:
        if 1 in fila:
            return False
    return True

def jugar_batalla_naval():
    tablero_pj = [[0 for _ in range(5)] for _ in range(5)]
    tablero_sj = [[0 for _ in range(5)] for _ in range(5)]

    print(f"{nombrejugador1}, coloca tus barcos:")
    colocar_barcos(tablero_pj)

    print(f"{nombrejugador2}, coloca tus barcos:")
    colocar_barcos(tablero_sj)

    while True:
        print(f"{nombrejugador1}, es tu turno:")
        mostrar_tablero(tablero_sj)
        x = int(input("Ingresa la coordenada X para disparar (0-4): "))
        y = int(input("Ingresa la coordenada Y para disparar (0-4): "))
        print(realizar_disparo(tablero_sj, x, y))
        if todos_barcos_hundidos(tablero_sj):
            print(f"{nombrejugador1} ganó!")
            break

        print(f"{nombrejugador2}, es tu turno:")
        mostrar_tablero(tablero_pj)
        x = int(input("Ingresa la coordenada X para disparar (0-4): "))
        y = int(input("Ingresa la coordenada Y para disparar (0-4): "))
        print(realizar_disparo(tablero_pj, x, y))
        if todos_barcos_hundidos(tablero_pj):
            print(f"{nombrejugador2} ganó!")
            break

def repetir_juego():
    while True:
        respuesta = input("¿Queres jugar de nuevo? (sí/no): ")
        if respuesta in ('sí', 'si', 's'):
            return True
        elif respuesta in ('no', 'n'):
            return False
        else:
            print("Respuesta inválida. Por favor, escribí 'sí' o 'no'.")

while True:
    jugar_batalla_naval()
    if not repetir_juego():
        print("Gracias por jugar!")
        break
