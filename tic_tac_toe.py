from random import randrange
board = ["1","2","3","4","X","6","7","8","9"]

def DisplayBoard(board):
    posicion = 0
    print("+---------" * 3,"+",sep="")
    for i in range(3):
        print("|         " * 3,"|",sep="")
        print("|   ", board[posicion], "   |   ", board[posicion+1], "   |   " ,board[posicion+2], "   |")
        print("|         " * 3,"|",sep="")
        print("+---------" * 3,"+",sep="")
        posicion += 3
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#

def EnterMove(board):
    permiso = True
    while permiso :
        jugada = int(input("Escoja pocisión donde marcar O: "))
        sign = "O"
        if jugada >= 1 and jugada <= 9 :
            if board[jugada-1] == "O" or board[jugada-1] == "X" :
                print("Casilla ocupada")
                EnterMove(board)
            else:
                board[jugada-1] = sign
            permiso = False
        else :
            print("Resultado incorrecto, por favor intentar nuevamente")
    return VictoryFor(board, sign)
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#

# def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#

def VictoryFor(board, sign):
    filas = 0
    columnas = 0
    for i in range(3):
        if board[filas] == sign and board[filas+1] == sign and board[filas+2] == sign :
            return True
        elif board[columnas] == sign and board[columnas+3] == sign and board[columnas+6] == sign :
            return True
        elif columnas == 0 :
            if board[columnas] == sign and board[columnas+4] == sign and board[columnas+8] == sign :
                return True
        elif columnas == 2:
            if board[columnas] == sign and board[columnas+2] == sign and board[columnas+4] == sign :
                return True
        filas += 3
        columnas += 1
    return False
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#

def DrawMove(board):
    jugada = randrange(9)
    sign = "X"
    if board[jugada-1] == "O" or board[jugada-1] == "X" :
        DrawMove(board)
    else:
        board[jugada-1] = sign
    return VictoryFor(board, sign)
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#

DisplayBoard(board)
while True :
    if EnterMove(board) :
        DisplayBoard(board)
        print("Felicidades tu ganaste")
        break
    if DrawMove(board) :
        DisplayBoard(board)
        print("Perdiste, ha ganado la CPU")
        break
    else :
        DisplayBoard(board)