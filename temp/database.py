import sqlite3

CREATE_STUD_TABLE = " CREATE TABLE IF NOT EXISTS Details(id integer PRIMARY KEY,USN TEXT, stud_Name TEXT NOT NULL, Email_ID TEXT, CGPA FLOAT);"

INSERT_STUD_DET = "INSERT INTO Details(USN, stud_Name, Email_ID, CGPA) VALUES (?, ?, ?, ?) ;"

GET_ALL_STUD_DET = "SELECT * FROM Details ;"

GET_STUD_NAME = "SELECT * from Details WHERE USN = ? ; "

GET_STUD_ELIGIBLE = ''' SELECT * FROM Details
                        WHERE CGPA >= ?
                        ORDER BY CGPA DESC;
'''
global cur

def connect():
    return sqlite3.connect("std_data.db")
        
def create_table(connection):
    with connection:
        cur = connection.cursor()
        cur.execute(CREATE_STUD_TABLE)


def add_stdent(connection, USN, stud_Name, Email_ID, CGPA):
    with connection:
        cur = connection.cursor()
        cur.execute(INSERT_STUD_DET ,(USN,stud_Name,Email_ID,CGPA))
        connection.commit()
        cur.close()

def get_all_std_det(connection):
    with connection:
        return connection.execute(GET_ALL_STUD_DET).fetchall()

def get_std_name(connection, USN):
    with connection:
        return connection.execute(GET_STUD_NAME, (USN,)).fetchall()

def get_eligible(connection, CGPA):
    with connection:
        return connection.execute(GET_STUD_ELIGIBLE ,(CGPA,)).fetchall()