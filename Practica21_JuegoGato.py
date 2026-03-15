from random import randrange


def mostrar_tablero(tablero):
    for fila in tablero:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   " + str(fila[0]) + "   |   " + str(fila[1]) + "   |   " + str(fila[2]) + "   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def pedir_movimiento(tablero):
    while True:
        try:
            movimiento = int(input("Elige un número de 1 a 9 para colocar tu ficha: "))
            if movimiento < 1 or movimiento > 9:
                print("Número inválido. Debe estar entre 1 y 9.")
                continue

            fila = (movimiento - 1) // 3
            columna = (movimiento - 1) % 3

            if tablero[fila][columna] in ["X", "O"]:
                print("Ese cuadro ya está ocupado. Intenta de nuevo.")
                continue

            tablero[fila][columna] = "O"
            break

        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")


def obtener_campos_libres(tablero):
    libres = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] not in ["X", "O"]:
                libres.append((fila, columna))
    return libres


def victoria(tablero, signo):
    for fila in range(3):
        if tablero[fila][0] == signo and tablero[fila][1] == signo and tablero[fila][2] == signo:
            return True

    for columna in range(3):
        if tablero[0][columna] == signo and tablero[1][columna] == signo and tablero[2][columna] == signo:
            return True

    if tablero[0][0] == signo and tablero[1][1] == signo and tablero[2][2] == signo:
        return True

    if tablero[0][2] == signo and tablero[1][1] == signo and tablero[2][0] == signo:
        return True

    return False


def movimiento_maquina(tablero):
    libres = obtener_campos_libres(tablero)
    if len(libres) > 0:
        pos = randrange(len(libres))
        fila, columna = libres[pos]
        tablero[fila][columna] = "X"


tablero = [[1, 2, 3],
           [4, "X", 6],
           [7, 8, 9]]

while True:
    mostrar_tablero(tablero)

    if victoria(tablero, "X"):
        print("¡La máquina ha ganado!")
        break

    if victoria(tablero, "O"):
        print("¡Has ganado!")
        break

    campos_libres = obtener_campos_libres(tablero)
    if len(campos_libres) == 0:
        print("¡Empate!")
        break

    pedir_movimiento(tablero)
    mostrar_tablero(tablero)

    if victoria(tablero, "O"):
        print("¡Has ganado!")
        break

    campos_libres = obtener_campos_libres(tablero)
    if len(campos_libres) == 0:
        print("¡Empate!")
        break

    movimiento_maquina(tablero)

    if victoria(tablero, "X"):
        mostrar_tablero(tablero)
        print("¡La máquina ha ganado!")
        break

    campos_libres = obtener_campos_libres(tablero)
    if len(campos_libres) == 0:
        mostrar_tablero(tablero)
        print("¡Empate!")
        break
