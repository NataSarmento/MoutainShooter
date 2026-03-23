import sqlite3
from datetime import datetime

class DBProxy:
    def __init__(self, db_name='vampire.db'):
        """Inicializa a conexão e garante a existência da tabela de ranking."""
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        """Cria a estrutura do banco de dados caso ela não exista."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ranking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                score_value INTEGER NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def save_score(self, player_name, score_value):
        """Persiste uma nova pontuação no banco de dados."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        cursor.execute(
            'INSERT INTO ranking (player_name, score_value, date) VALUES (?, ?, ?)',
            (player_name, score_value, now)
        )
        conn.commit()
        conn.close()

    def get_top_scores(self):
        """Recupera os 10 melhores resultados ordenados por pontuação."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(
            'SELECT player_name, score_value, date FROM ranking ORDER BY score_value DESC LIMIT 10'
        )
        results = cursor.fetchall()
        conn.close()
        return results