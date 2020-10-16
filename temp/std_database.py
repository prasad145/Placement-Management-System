import sqlite3
from student_class import Student
connection = sqlite3.connect('std_data.db')

cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students(
                usn varchar(20) PRIMARY KEY,
                firstName text,
                lastname text,
                sem real,
                cgpa int,
                backlogs int,
                phone int
            )""")

def insert_students(std):
    with connection:  # with - context manager (to avoid closing of cursor everytime)
        cur.execute("INSERT or IGNORE INTO students VALUES(:usn, :firstName, :lastname, :sem, :cgpa, :backlogs, :phone)",
         {'usn' : std.USN,'firstName' : std.first_name, 'lastname' : std.Last_Name, 'sem' : std.Sem, 'cgpa' : std.CGPA, 'backlogs': std.Current_Backlogs, 'phone' : std.Phone_Number}) 

def get_all_students():
    cur.execute("SELECT * FROM students")
    return cur.fetchall()

def get_students_details_on_id(id_no):
    cur.execute("SELECT firstName, lastname, cgpa, backlogs FROM students WHERE usn = :usn", {'usn': id_no})
    return cur.fetchone()

def update_student_details(std, cur_cgpa, cur_backlogs, cur_sem ):
    with connection:
        cur.execute("UPDATE students SET cgpa = :cgpa, sem = :sem ,backlogs = :backlogs  WHERE usn = :usn", {'cgpa' : cur_cgpa, 'sem' : cur_sem, 'backlogs' : cur_backlogs, 'usn' : std.usn})

def remove_student(id_no):
    with connection:
        cur.execute("DELETE FROM students WHERE usn = :usn ", {'usn' : id_no })

def get_student_details(CGPA):
    cur.execute("SELECT * FROM students WHERE cgpa >= :cgpa", {'cgpa' : CGPA })
    return cur.fetchall()
#def create_Student(ENG17CS0158r)
#    Student(ENG17CS0158,2nd, .. , )

std_1 = Student('ENG17CS0141','Nikith', 'Kumar', 7, 7.62, 0, 9786543212)
std_2 = Student('ENG17CS0158','Prasad', 'acharya', 7, 8.65, 1, 9786543212)
std_3 = Student('ENG17CS0147','vamshi', 'P V', 7, 6.72, 2, 9786543612)
std_4 = Student('ENG17CS0142','Nithin', 'Kumar', 7, 9.00, 0, 9786543912)
std_5 = Student('ENG17CS0143','Natesh', 'S', 7, 8.90, 0, 9786543823)

insert_students(std_1)
insert_students(std_2)
insert_students(std_3)
insert_students(std_4)
insert_students(std_5)

stds = get_all_students()
print(stds)

stdd = get_students_details_on_id('ENG17CS0158')  
print(stdd)

"""
update_students_details(std3, )
empss = get_students_details(95000) 
print(empss)
"""
remove_student('ENG17CS0147')

ep = get_all_students()
print(ep)
