import sqlite3
import os

# Crea la BBDD
class WordModel:
    def __init__(self, db_path="01_train_english/database/words.db"):
        self.conn = sqlite3.connect(db_path)
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
    def get_random_word(self, topic):
        self.cursor.execute("SELECT * FROM words  WHERE topic = ? ORDER BY RANDOM() LIMIT 1",(topic,))
        return self.cursor.fetchone()
    
# Visualizar todos los tópis disponibles
    def get_all_topis(self):
        self.cursor.execute("SELECT DISTINCT topic from words ORDER BY topic DESC")
        return self.cursor.fetchall()
