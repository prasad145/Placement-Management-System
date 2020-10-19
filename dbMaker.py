# dbMaker.py

import xlrd
import sqlite3

loc = "students.xlsx"
db = sqlite3.connect('data.db')

cur = db.cursor()

xl = xlrd.open_workbook(loc)
s = xl.sheet_by_index(0)

num = s.nrows
create = " CREATE TABLE IF NOT EXISTS studentDB(USN text PRIMARY KEY, full_name text, first_name TEXT, CGPA FLOAT, backs INT);"
insert = "INSERT INTO studentDB(USN, full_name, first_name, CGPA, backs) values "

#create1 = " CREATE TABLE IF NOT EXISTS companies(comp_id int PRIMARY KEY AUTOINCREMENT, company_name text, CTC int, offered_Role TEXT, CGPA FLOAT, backs INT);"
#insert = "INSERT INTO companyDB(company_name, CTC, offered_Role, CGPA, backs) values "

cur.execute(create)

db.commit()


for i in range(num):
    data = s.row_values(i)
    usn = data[0]
    name = data[1]
    fname = data[2].lower()
    cgpa = data[27]
    backs = data[31]

    val = "('"+ usn + "' ,'" + name +"' ,'" + fname +"' ," + str(cgpa) +", " + str(backs) + ");"
    q = insert + val
    # print(q)
    try:
        cur.execute(q)
    except:
        print(val)


    # print(data)
db.commit()
