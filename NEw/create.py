from configparser import ConfigParser
import psycopg2
def load_config(filename='database1.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

def create_table():
    """ Create PhoneBook table in PostgreSQL """
    conn = None

    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS PhoneBook (
                name TEXT NOT NULL,
                phoneNumber TEXT NOT NULL
            )
            """)
        conn.commit()
        print("Table 'PhoneBook' created successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Database connection closed.")

if __name__ == '__main__':

    config = load_config()
    create_table()
