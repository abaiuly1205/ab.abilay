import psycopg2
from config import load_config
def connect(config):
    try:
        conn = psycopg2.connect(**config)
        print('Connected to the PostgreSQL server.')
        return conn
    except psycopg2.DatabaseError as error:
        print(f'Error connecting to PostgreSQL: {error}')

def create_game_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user_score (
                id SERIAL PRIMARY KEY,
                user_id INT NOT NULL,
                username TEXT NOT NULL,
                score INT NOT NULL,
                level INT NOT NULL
            )
        """)
        conn.commit()
        cur.close()
        print('Game table created successfully.')
    except psycopg2.DatabaseError as error:
        print(f'Error creating game table: {error}')

if __name__ == '__main__':
    config = load_config()

    conn = connect(config)

    create_game_table(conn)

    conn.close()
