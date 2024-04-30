import psycopg2
import csv

con = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="a.abylai7")
current = con.cursor()
def search():
    n = input("Contact Name or Number: ")
    current.execute(f"""SELECT * FROM Phone_Book WHERE name LIKE '{n}' OR phone_number LIKE '{n}';""")
    print(current.fetchone())
insert = """
    INSERT INTO PhoneBook VALUES(%s,%s) returning *;
"""

update1 = """
    UPDATE PhoneBook SET name = %s WHERE phonenumber = %s;
"""
update2 = """
    UPDATE PhoneBook SET phonenumber = %s WHERE name = %s;
"""

select = """
    SELECT * FROM PhoneBook
"""
select1 = """
    SELECT * FROM PhoneBook WHERE name= %s ;
"""
select2 = """
   SELECT * FROM PhoneBook WHERE phonenumber LIKE %s;

"""
delete = """
    DELETE FROM PhoneBook WHERE name = %s;
"""
delete1 = """
    DELETE FROM PhoneBook WHERE phonenumber LIKE %s;
"""

work = True
while work:


    n = input('******************************' + '\n' + 'inscsv - insert csv,'+'\n' + 'inscon - insert console,'+'\n' + 'nameupd - update of name,'+'\n' + 'phoneupd - update of phone,'+'\n' + 'sel - select,'+'\n' + 'namesel - select of name,'+'\n' + 'numsel - select of number,'+'\n' + 'del - delete,'+'\n' + 'numdel - delete of number,'+'\n' + 'check - check,' + '\n' + 'stop - stop.' + '\n' + '******************************' + '\n')
    if n == 'inscsv':
        with open("book.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, phoneNumber = row
                current.execute(insert, (name, phoneNumber))
        con.commit()
    if n == 'inscon':
        name = input("Name:")
        phoneNumber = input("Number:")
        current.execute(insert, (name, phoneNumber))
        con.commit()

    if n == 'nameupd':
        name = input("newName:")
        phone_number = input("Number:")
        current.execute(update1, (name, phone_number))
        con.commit()
    if n == 'phoneupd':
        name = input("Name:")
        phone_number = input("newnumber:")
        current.execute(update2, (phone_number,name))
        con.commit()
    if n == 'sel':
        current.execute(select)
        print(*current.fetchall(), sep='\n')
        con.commit()
    if n == 'namesel':
        name = input("Name: ")
        current.execute(select1,[name])
        print(*current.fetchall(), sep='\n')
        con.commit()
    if n == 'numsel':
        phone_number = input("Number: ")
        current.execute(select2, [phone_number])
        print(*current.fetchall(), sep='\n')
        con.commit()
    if n == 'del':
        name = input("Name:")
        current.execute(delete, [name])
        con.commit()
    if n == 'numdel':
        phone_number = input("Number:")
        current.execute(delete1, [phone_number])
        con.commit()
    if n == 'check':
        search()
    if n == 'stop':
        work = False


current.close()
con.commit()
con.close()