import tkinter as tk
import random
from models.word_model import WordModel
from views.word_view import WordView

class WordController:
    def __init__(self):
        self.model = WordModel()
        self.root = tk.Tk()
        self.view = WordView(self.root, self)

    def run(self):
        self.root.mainloop()

    # ---- Métodos que la vista llamará ----

    def get_topics(self):
        return self.model.get_all_topis()

    def add_word(self, word, meaning, topic):
        self.model.add_word(word, meaning, topic)

    def start_practice(self, topic):
        palabras = self.model.get_word_by_topic(topic)

        # Crear diccionario palabra: significado
        palabras_topic = {row['word']: row['meaning'] for row in palabras}

        self.practice_loop(palabras_topic)

    def practice_loop(self, palabras_topic):
        if not palabras_topic:
            self.view.show_message("Felicidades! Has terminado el topic!")
            return

        # Seleccionar palabra aleatoria
        guess = random.choice(list(palabras_topic.keys()))

        # Pedir al usuario con la vista
        self.view.ask_meaning(
            guess,
            lambda user_try: self.check_answer(user_try, guess, palabras_topic)
        )

    def check_answer(self, user_try, guess, palabras_topic):
        if user_try.lower().strip() == palabras_topic[guess]:
            del palabras_topic[guess]
            self.view.show_message(f"✅ Correcto! Quedan {len(palabras_topic)}")
        else:
            self.view.show_message(f"❌ La respuesta correcta era: {palabras_topic[guess]}")

        # Continuar práctica
        self.practice_loop(palabras_topic)