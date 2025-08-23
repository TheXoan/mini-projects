from models.word_model import WordModel

database_words = WordModel()

while True:
    print("\n----- Práctica de inglés -----")
    print("1. Practicar un tema")
    print("2. Ver topics disponibles")
    print("3. Añadir un nuevo tópic")
    print("0. Salir")
    
    option = input("Elige una opción: ")
    
    match option:
        case "1":
            print
        case "2":
            print("Topis: \n")
            print(database_words.get_all_topis())
        case "3":
            continuar = True
            name_topic = input("Nombre del tópic: ")
            while continuar == True:
                name_word = input("Nueva palabra: ")
                name_meaning = input("Significado: ")
                correcto = input(f"{name_word} se traduce como {name_meaning} es esto correcto? (si, no): ")
                if correcto.lower() == "si":
                    database_words.add_word(name_word, name_meaning, name_topic)
                else:
                    print("Vuelve a escribir la palabra:")
                continuar = input("Quieres continuar introduciendo palabras: (True, False)")
        case "0":
            print("Saliendo...")
            break
        case _:
            print("Escoge una de las opciones válidas!")