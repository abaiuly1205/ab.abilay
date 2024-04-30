import psycopg2
from config import load_config

def update_data():
    conn = None

    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cursor = conn.cursor()

        update_option = input("Update by (1) Username or (2) Phone Number: ")

        if update_option == "1":
            username = input("Enter username to update: ")
            new_phone_number = input("Enter new phone number: ")
            cursor.execute("UPDATE PhoneBook SET phone_number = %s WHERE username = %s", (new_phone_number, username))
        elif update_option == "2":
            phone_number = input("Enter phone number to update: ")
            new_phone_number = input("Enter new phone number: ")
            cursor.execute("UPDATE PhoneBook SET phone_number = %s WHERE phone_number = %s", (new_phone_number, phone_number))
        else:
            print("Invalid option selected.")

        conn.commit()
        print("Data updated successfully.")

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Database connection closed.")

if __name__ == '__main__':
    update_data()
