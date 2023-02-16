from .pawns_module import Pawns, FrecuencyTable
from .word_module import Word

class Board(object):
    score = 0
    def __init__(self):
        self.board = [
            [" " for _ in range(15)] for _ in range(15)
        ]

        self.totalWords = 0
        self.totalPawns = 0
    
    def showBoard(self):
        """
        Muestra el tablero con las casillas ocupadas y desocupadas
        """
        #Debe ser un numero par la variable espaces para que las columnas queden centradas
        spaces = 6
        for i in range(len(self.board)):
            print("  {}{}  ".format("0" if i < 9 else "", i+1), end= "")
        print()
        for i in range(len(self.board)):
            print("-" * 15 * spaces)
            for s in self.board[i]:
                print(f"  {s}  |", end= "")
            
            print(" {}{}".format("0" if i < 9 else "", i+1))

    def placeWord(self, x, y, d, word, pawns):
        """
        Escribe una palabra en las cordenadas y direccion indicadas, en el tablero.

        Args:
            x(int): posición de la cordenada x
            y(int): posición de la cordenada y
            d(str): dirección de la palabra
            word(obj): objeto de la clase Word
            pawns(obj): objeto de la clase Pawns
        """
        for c in word.word:    
            if self.board[x][y] != c:
                pawns.takePawn(c)
                self.totalPawns += 1
            self.board[x][y] = c
            Board.score += Pawns.getPoints(c)
        
            if d == "H":
                y += 1
            elif d == "V":
                x += 1
        self.totalWords += 1

    def isPossible(self, x, y, d, word):
        """
        Determina si es posible colocar una palabra en el tablero.

        Args:
            x(int): Posición Fila
            y(int): Posición Columna
            d(str): Dirección
            word(obj): Objeto de la clase word.
        
        Return:
            True(bool)
            False(bool)
        """
        if self.totalWords > 0:


            exist = False
            is_possible = True
            new_pawn = False
            connect_pawn = True

            x0 = x
            y0 = y
            for w in word.word:
                #Conmprueba si una letra se sale del rango del tablero
                if (0 > x or x > 14) or (0 > y or y > 14):
                    message = "La palabra se sale del rango del tablero."
                    return (False, message)
                
                #Comprueba si en la jugada almenos una letra ya se encontraba en el tablero
                if w == self.board[x][y]:
                    exist = True
                
                #Comprueba si la posicion del tablero cuenta ya con una ficha
                if self.board[x][y] != " " and w != self.board[x][y]:
                    message = f"No puedes reeplazar el caracter de la fila {x+1} y la columna {y+1}."
                    return (False, message)
                
                #Comprueba si hay almenos una nueva ficha nueva en la jugada.
                if self.board[x][y] == " ":
                    new_pawn = True
            
                if d == "H":
                    y += 1
                else:
                    x += 1


            #Comprueba si hay una letra antes o despues de la palabra
            if d == "H":
                if y0 > 0 and y0 + word.getLenghtWord <= 14:
                    if (self.board[x0][y0 - 1] != " ") or (self.board[x0][y0 + word.getLenghtWord] != " "):
                        connect_pawn = False
            elif d == "V":
                if x0 > 0 and x0 + word.getLenghtWord <= 14:
                    if (self.board[x0 - 1][y0] != " ") or (self.board[x0 + word.getLenghtWord][y0] != " "):
                        connect_pawn = False
                    
            
            if exist == True and is_possible == True and new_pawn == True and connect_pawn:
                message = "La palabra se puede situar en el tablero."
                return (True, word.word)
            
            elif not exist:
                message = "Almenos una letra de la palabra ya se debe encontrar en el tablero."
                return (False, message)
            elif not new_pawn:
                message = "La palabra no tiene ninguna letra adicional para cambiar el estado del tablero."
                return (False, message)
            elif not connect_pawn:
                message = "Hay una ficha antes o despues de la palabra. (Jugada Invalida)"
                return(False, message)
        
        else:
            is_possible = True
            if d == "H":
                if x != 7 or word.getLenghtWord + y < 7:
                    is_possible = False
            elif d == "V":
                if y != 7 or word.getLenghtWord + x < 7:
                    is_possible = False
            
            if is_possible:
                message = "La palabra se puede situar en el tablero."
                return (True, message)
            message = "Una letra de la primera palabra debe pasar por la casilla (08, 08)"
            return(False, message)
         
    def getPawns(self, x, y, d, word):
        """
        Recibe una palabra y devuelve las letras que faltan en el tablero para completar la palabra

        Args:
            x (int): Posición Fila
            y (int): Posición Columna
            d (str): Dirección
            word (obj): Objeto de la clase word
        
        return:
            Letras que faltan para completar la palabra en el tablero
        """
        pawns_to_complete = Word()
        for c in word.word:
            if self.board[x][y] == " ":
                pawns_to_complete.word.append(c)
    
            if d == "H":
                y += 1
            else:
                x += 1
        return pawns_to_complete

    def showWordPlacement(self, pawns, word):
        """
        Dadas las fichas del jugador y una palabra, muestra las posibles colocaciones de la palabra.
        """
        for direction in ["V", "H"]:
            print("{}:".format("Vertical" if direction == "V" else "Horizontal"))
            for i in range(15):
                for j in range(15):
                    if self.isPossible(i, j, direction, word)[0] == True:
                        needed_pawns = self.getPawns(i, j, direction, word)
                        if FrecuencyTable.isSubset(needed_pawns.getFrecuency(), pawns.getFrecuency()):
                            print("(x = {}, y = {})".format(i + 1, j + 1))
                        