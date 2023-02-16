
import csv
from numpy import random
class Pawns(object):
    """
    Clase que administra las fichas del juego y la cantidad de fichas
    """

    points = {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2,
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3,
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10
    }

    def __init__(self) -> None:
        self.letter = []
    
    def addPawn(self, caracter):
        """
        Recibe un caracter y lo agrega a las fichas del objeto.
        """
        self.letter.append(caracter)
    
    def addPawns(self, caracter, n):
        """
        Recibe un caracter y las veces que se quiere que este se agrege a las fichas del objeto
        """
        for _ in range(n):
            self.addPawn(caracter)

    
    def createBag(self):
        """
        Crea la bolsa de palabras gracias a un archivo .csv
        """
        path = "bag_of_pawns.csv"
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                self.addPawns(row["Letter"], int(row["Count"]))


    def takeRandomPawn(self):
        """
        Retorna una ficha aleratoria de la bolsa, a la vez que la elimina de la bolsa.
        """
        card = random.choice(self.letter)
        self.letter.remove(card)
        return card
    
    def takePawn(self, pawn):
        """
        Elimina una ficha indicada del array.

        Args:
            pawn(str): ficha (letra) a eliminar de las fichas del objeto.
        """
        self.letter.remove(pawn)

    def showPawns(self):
        """
        Muestra las fichas totales del objeto
        """
        frecuency = self.getFrecuency()
        FrecuencyTable.showFrecuency(frecuency)
    
    def getFrecuency(self):
        """
        Retorna la lista de frecuencias de las fichas del objeto.
        """
        obj = FrecuencyTable()
        for c in self.letter:
            obj.update(c)
        return obj

    def getTotalPawns(self):
        """
        Retorna la cantidad de fichas que tiene el objeto.
        """
        return len(self.letter)

    @staticmethod
    def getPoints(c):
        """
        Retorna los puntos que tiene una letra del juego.
        """
        return Pawns.points[c]


    @staticmethod
    def showPawnsPoints():
        """
        Muestra los puntos que tiene cada letra del juego.
        """
        for c in Pawns.points:
            point = Pawns.getPoints(c)
            print((c, point))

class FrecuencyTable(object):
    def __init__(self):
        self.letters = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        self.frecuencies = [0 for _ in range(26)]
    
    def showFrecuency(self):
        """
        Muestra la tabla de frecuencias del objeto (str, int).
        """
        for i in range(len(self.letters)):
            if self.frecuencies[i] > 0:
                print((self.letters[i], self.frecuencies[i]))
    
    def update(self, c):
        """
        Recibe una letra y aumenta la frecuencia de ese caracter.
        """
        self.frecuencies[self.letters.index(c)] += 1

    @staticmethod
    def isSubset(obj1, obj2):
        """
        Comprueba si obj1 es subconjunto de obj2 (para determinar si los elementos del obj1 estan en el obj2).
        """
        for i in range(len(obj1.frecuencies)):
            if obj1.frecuencies[i] > obj2.frecuencies[i]:
                return False
        return True



