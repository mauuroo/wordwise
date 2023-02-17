
import lib
import os
import numpy

def help():
    option = input("A) 5 Palabras validas a formar con tus fichas\n"
                   "B) 5 Palabras posibles a formar con una ficha del tablero\n"
                   "D) Atrás\n").upper()
                   
    if option == "A":
        words = lib.Dictionary.showWord(player_frecuency)
        number_of_words = words[1] #Si la cantidad de palabras es mayor o igual a 5, solo se permitiran 5 palabras
        print(numpy.random.choice(words[0], number_of_words, False))

    elif option == "B":
        caracter = input("Introduce una ficha: ").upper()
        words = lib.Dictionary.showWordPlus(player_pawns, caracter)
        number_of_words = words[1] #Si la cantidad de palabras es mayor o igual a 5, solo se permitiran 5 palabras
        print(numpy.random.choice(words[0], number_of_words, False))

    elif option == "C":
        initial_menu()
    else:
        print("Opción no valida")
        input("Enter para continuar...\n")
        os.system("cls")
        board.showBoard()
        player_pawns.showPawns()
        help()

def enter_word():
    new_word = lib.Word.readWord()
    if lib.Dictionary.validateWord(new_word):
        option = input("A) Introducir coordenadas.\n"
                       "B) Posibles coordenadas (Ayuda)\n"
                       "C) Atrás\n").upper()
        
        if option == "A":
            x = int(input("Introduce la cordenada x: ")) - 1
            y = int(input("Introduce la cordenada y: ")) - 1
            d = input ("Introduce la direccion (H: Horizontal, V: Vertical): ").upper()

            is_possible = board.isPossible(x, y, d, word= new_word)

            if is_possible[0]:
                pawns_to_complete = board.getPawns(x, y, d, word= new_word)
                frecuency_pawns_complete = pawns_to_complete.getFrecuency()


                if lib.FrecuencyTable.isSubset(frecuency_pawns_complete, player_frecuency):
                    os.system("cls")
                    board.placeWord(x, y, d, word= new_word, pawns= player_pawns)
                    for _ in range(7 - player_pawns.getTotalPawns()):
                        player_pawns.addPawn(bag_of_pawns.takeRandomPawn())

                else:
                    print("No cuentas con las fichas requeridas de la palabra.")
            else:
                print(is_possible[1])
                input("Enter para continuar...")
        
        elif option == "B":
            board.showWordPlacement(player_pawns, new_word)
            input("Enter para continuar...\n")

            enter_word()
        
        elif option == "C":
            initial_menu()
        else:
            print("Ninguna opcion es valida")
            input("Enter para continuar...\n")
            os.system("cls")
            board.showBoard()
            player_pawns.showPawns()
            initial_menu()


def initial_menu():
    global player_frecuency
    player_frecuency = player_pawns.getFrecuency()
    os.system("cls")  
    board.showBoard()
    print(f"Puntuación: {board.score}")
    player_pawns.showPawns()
    
    option = input("A) Introducir una Palabra\n"
                   "B) Ayuda\n"
                   "C) Mostrar Puntuación de las Fichas\n"
                   "D) Salir\n").upper()

    if option == "A":
        enter_word()
    elif option == "B":
        help()
    elif option == "C":
        for key, value in lib.Pawns().points.items():
            print(f"{key}= {value}")
        
        input("Enter para continuar...")
    elif option == "D":
        print(f"Puntuación: {lib.Board().score}")
        return False
    else:
        print("Opcion no valida.")
        input("Enter para continuar...")
    
    return True

def startgame():
    game_in_play = True

    global bag_of_pawns
    bag_of_pawns = lib.Pawns()
    bag_of_pawns.createBag()

    global player_pawns
    player_pawns = lib.Pawns()
    for _ in range(7):
        player_pawns.addPawn(bag_of_pawns.takeRandomPawn())

    global board
    board = lib.Board()

    board.showBoard()
    player_pawns.showPawns()

    while game_in_play:
        game_in_play = initial_menu()

startgame()