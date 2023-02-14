
import lib
import os

bag_of_pawns = lib.Pawns()
bag_of_pawns.createBag()

player_pawns = lib.Pawns()
for _ in range(7):
    player_pawns.addPawn(bag_of_pawns.takeRandomPawn())


board = lib.Board()
board.showBoard()
player_pawns.showPawns()
while True:
    player_frecuency = player_pawns.getFrecuency()
    option = input("Introducir una Palabra (P) | Ayuda (A) | Salir (S)\n").upper()
    if option == "P":
        new_word = lib.Word.readWord()

        if lib.Dictionary.validateWord(new_word):
            option = input("A) Introducir coordenadas.\n"
                           "B) Posibles coordenadas (Ayuda)\n").upper()
            
            if option == "A":
                x = int(input("Introduce la cordenada x: ")) - 1
                y = int(input("Introduce la cordenada y: ")) - 1
                d = input ("Introduce la direccion (H: Horizontal, V: Vertical): ").upper()


                word_table = new_word.getFrecuency()
                is_possible = board.isPossible(x, y, d, word= new_word)

                if is_possible[0]:
                    pawns_to_complete = board.getPawns(x, y, d, word= new_word)
                    frecuency_pawns_complete = pawns_to_complete.getFrecuency()


                    if lib.FrecuencyTable.isSubset(frecuency_pawns_complete, player_frecuency):
                        #os.system("cls")
                        board.placeWord(x, y, d, word= new_word, pawns= player_pawns)
                        board.showBoard()
                        print(f"Puntuación: {board.score}")
                        for i in range(7 - player_pawns.getTotalPawns()):
                            player_pawns.addPawn(bag_of_pawns.takeRandomPawn())
                        player_pawns.showPawns()

                    else:
                        print("No cuentas con las fichas requeridas de la palabra.")
                else:
                    print(is_possible[1])
            
            elif option == "B":
                board.showWordPlacement(player_pawns, new_word)
            
            else:
                print("Ninguna opcion es valida")

    elif option == "A":
        option = input("A) 5 Palabras validas a formar con tus fichas\n"
                       "B) 5 Palabras a formar con una ficha del tablero\n"
                       "C) Posibles colocaciones de una palabra sobre el tablero\n").upper()
        if option == "A":
            print(lib.Dictionary.showWord(player_frecuency))
        elif option == "B":
            caracter = input("Introduce una ficha: ").upper()
            print(lib.Dictionary.showWordPlus(player_pawns, caracter))
        elif option == "C":
            word = lib.Word.readWord()
            lib.Board.showWordPlacement(player_pawns, word)
        else:
            print("Opción no valida")

    elif option == "S":
        print(f"Puntuación Final: {board.score}")
        break

    else:
        print("Opción no valida")