import psycopg2
from config import load_config

def connect(config):
    try:
        conn = psycopg2.connect(**config)
        print('Connected to the PostgreSQL server.')
        return conn
    except psycopg2.DatabaseError as error:
        print(f'Error connecting to PostgreSQL: {error}')

def insert_game_data(conn, user_id, score, username, level):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, username, level))
        conn.commit()
        cur.close()
        print('Game data inserted successfully.')
    except psycopg2.DatabaseError as error:
        print(f'Error inserting game data: {error}')

if __name__ == '__main__':
    config = load_config()

    conn = connect(config)

    user_id = 1 
    score = 100 
    level = 3  

    insert_game_data(conn, user_id, score, level)

    conn.close()
