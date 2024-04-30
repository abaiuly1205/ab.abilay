import psycopg2
from config import load_config

def query_data_with_pattern():
    conn = None

    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cursor = conn.cursor()

        pattern = input("Enter username or number to filter: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE username LIKE %s OR phone_number LIKE %s", (f"%{pattern}%", f"%{pattern}%"))
        rows = cursor.fetchall()

        if rows:
            print("Результаты:")
            for row in rows:
                print("ID:", row[0])
                print("Имя пользователя:", row[1])
                print("Номер телефона:", row[2])
        else:
            print("Нет результатов для указанного шаблона.")

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Соединение с базой данных закрыто.")

if __name__ == '__main__':
    query_data_with_pattern()
