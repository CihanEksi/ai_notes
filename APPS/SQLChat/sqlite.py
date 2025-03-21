import sqlite3

connection= sqlite3.connect('employees.db')

cursor= connection.cursor()

tableInfo = '''
CREATE TABLE IF NOT EXISTS employees(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(100), Department VARCHAR(100), Salary INT)
'''

cursor.execute(tableInfo)

## insert data

cursor.execute("INSERT INTO employees VALUES(1,'John', 'HR', 50000)")
cursor.execute("INSERT INTO employees VALUES(2,'Jane', 'IT', 60000)")
cursor.execute("INSERT INTO employees VALUES(3,'Jim', 'Finance', 70000)")
cursor.execute("INSERT INTO employees VALUES(4,'Jill', 'HR', 80000)")
cursor.execute("INSERT INTO employees VALUES(5,'Jack', 'IT', 90000)")

print("Data inserted successfully")

data = cursor.execute("SELECT * FROM employees")

for row in data:
    print(row)


connection.commit()
connection.close()