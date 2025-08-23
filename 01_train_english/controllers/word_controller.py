from models.word_model import WordModel

class WordController:
    def __init__(self):
        self.model = WordModel()

    # Método para preguntar las palabras              
    def ask_words(self, topic):
        print("asdf")

    def run(self):
        while True:
            print("\n----- Práctica de inglés -----")
            print("1. Practicar un tema")
            print("2. Ver topics disponibles")
            print("3. Añadir un nuevo tópic")
            print("0. Salir")
            
            option = input("Elige una opción: ")
            
            match option:
                case "1":
                    # Muestro todos los topics, y con el topic elegido llamo al método que comprueba las palabras
                    # *** FALTA IMPLEMENTAR OBTENER LAS PALABRAS Y GUARDARLAS EN UNA LISTA CLAVE VALOR Y LUEGO IR PREGUNTANDO y eliminando de la lista***
                    print(self.model.get_all_topis())
                    topic_chose = input("Con que topic quieres jugar: ")
                    self.model.check_word_spanish(topic_chose)
                case "2":
                    # Enumero todos los temas disponibles si los hay
                    topics = self.model.get_all_topis()
                    if topics:
                        print("TOPICS: ")
                        for t in topics:
                            print(f"- {t}")
                    else:
                        print("No hay temas aún! ⚠️")
                case "3":
                    # Pido el tópic y luego voy pidiendo palabras e introduciéndolas
                    continuar = "si"
                    name_topic = input("Nombre del tópic: ")
                    while continuar == "si":
                        name_word = input("Nueva palabra: ")
                        name_meaning = input("Significado: ")
                        correcto = input(f"{name_word} se traduce como {name_meaning} es esto correcto? (si, no): ")
                        if correcto.lower() == "si":
                            self.model.add_word(name_word, name_meaning, name_topic)
                        else:
                            print("Vuelve a escribir la palabra:")
                        continuar = input("Quieres continuar introduciendo palabras (si, no): ")
                case "0":
                    print("Saliendo...💀")
                    break
                case _:
                    print("Escoge una de las opciones válidas!")