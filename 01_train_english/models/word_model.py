import sqlite3
import os

# Crea la BBDD
class WordModel:
    def __init__(self, db_path="01_train_english/database/words.db"):
        self.conn = sqlite3.connect(db_path)
        # Esto permite que luego al acceder al valor obtenido en la consulta podamos filtrarlo por nombre de columna. **Más visual
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS words(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            meaning TEXT NOT NULL,
            topic TEXT NOT NULL
        ) 
        """)
        self.conn.commit()    

# Añado una palabra
    def add_word(self, word, meaning, topic):
        self.cursor.execute("INSERT INTO words (word, meaning, topic) VALUES (?, ?, ?)", (word, meaning, topic))
        self.conn.commit()
        print("Palabra añadida correctamente")
        
# Obtengo una palabra aleatoria filtrando por tema
    def get_word_by_topic(self, topic):
        self.cursor.execute("SELECT * FROM words WHERE topic = ?",(topic,))
        return self.cursor.fetchall()
    
# Visualizar todos los tópis disponibles
    def get_all_topis(self):
        self.cursor.execute("SELECT DISTINCT topic from words ORDER BY topic DESC")
        rows = self.cursor.fetchall()
        return [row["topic"] for row in rows]