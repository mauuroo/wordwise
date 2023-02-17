from .pawns_module import FrecuencyTable

class Word(object):
    def __init__(self) -> None:
        self.word = []
    
    def __str__(self):
        word = "".join(self.word)
        return (f"{word}")


    def areEqual(self, w):
        """
        Comprueba si la palabra es igual a otra palabra
        """
        return True if self.word == w.word else False

    def isEmpty(self):
        """"
        Comprueba si la longitud de la palabra es 0
        """
        return True if self.getLenghtWord == 0 else False


    @property
    def getLenghtWord(self):
        return len(self.word)

    @staticmethod
    def readWordFromFile(f):
        """
        Recive un fichero de tipo txt, del cual devuelve un objeto de la clase Word

        Args:
            f (txt): Fichero en el que se encuentran todas las palabras validas del juego
        """
        line = f.readline()[:-1]
        word = Word()
        for c in line:
            word.word.append(c)
        return word
            

    def getFrecuency(self):
        """
        Retorna la lista de frecuencias de las fichas del objeto
        """
        frecuency = FrecuencyTable()
        for letter in self.word:
            frecuency.update(letter)
        return frecuency



    @classmethod
    def readWord(cls):
        """
        Solicita una palabra  y crea un objeto de la clase Word.
        """
        word = cls()
        string = input("Introduce una palabra: ").upper()
        
        for c in string:
            word.word.append(c)
        return word
    





class Dictionary(object):
    filepath = "dictionary.txt"
    @staticmethod
    def validateWord(word):
        """
        Devuelve True si la palabra dada se encuentra en el fichero txt del diccionario.

        Args:
            word (object): Objeto de la clase Word
        """
        with open(Dictionary.filepath, "r") as f:
            w = Word.readWordFromFile(f)
            while not word.areEqual(w) and not w.isEmpty():
                w = Word.readWordFromFile(f)
                

        if w.isEmpty() and not word.areEqual(w):
            print("La palabra no se encuentra en el diccionario")
            input("Enter para continuar...")
            return False
        return True


    @staticmethod
    def showWord(frecuency_pawns):
        with open(Dictionary.filepath, "r") as f:
            words = []
            word_file = Word.readWordFromFile(f)
            while not word_file.isEmpty():
                frecuency_wfile = word_file.getFrecuency()

                if FrecuencyTable.isSubset(frecuency_wfile, frecuency_pawns):
                    words.append("".join(word_file.word))
                
                word_file = Word.readWordFromFile(f)
        if len(words) >= 5:
            return (words, 5)
        else:
            return(words, len(words))
    
    @staticmethod
    def showWordPlus(pawns, c):
        with open(Dictionary.filepath, "r") as f:
            word_file = Word.readWordFromFile(f)
            words = []
            frecuency_pawns = pawns.getFrecuency()
            frecuency_pawns.update(c)

            while not word_file.isEmpty():  
                if c in word_file.word:
                    word_frecuency = word_file.getFrecuency()
                    if FrecuencyTable.isSubset(word_frecuency, frecuency_pawns):
                        words.append("".join(word_file.word))
            
                word_file = Word.readWordFromFile(f)
        
        if len(words) >= 5:
            return (words, 5)
        else:
            return(words, len(words))
    