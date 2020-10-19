import sqlite3
db1 = sqlite3.connect('companyDB.db')
cur1 = db1.cursor()

create1 = " CREATE TABLE IF NOT EXISTS companies(comp_id int PRIMARY KEY AUTOINCREMENT, company_name text, CTC int, offered_Role TEXT, CGPA FLOAT, backs INT);"
cur1.execute(create1)
print("successfully created")
db1.commit()