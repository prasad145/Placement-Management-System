import database
import string
OPTIONS = """
  WELCOME PLACEMENT 2021

  1) ADD STUDENTS
    11) Add Student details
    12) see all students
    13) Find a student name by USN
    14) Fine Who are eligible
  
  2) ADD COMPANY
    21) add new comapany
    22) company criteria
    23) see elgible students 

  3) EXIT
    
"""

def menu():
    connection = database.connect()
    database.create_table(connection)
    while True:
      user_input = int(input(OPTIONS)) 
      if user_input == 3:
        break
      elif user_input == 1:
        user_input = int(input("enter student option"))    
        if user_input == 11:
          option_add_new_stu(connection)
        elif user_input ==  12:
          option_get_std(connection)
                  
        #user_input = input(OPTIONS)
def option_add_new_stu(connection):
    usn = (input("Enter the student USN :"))
    Name = input("Enter the Student Name :")
    email = (input("Valid Email ID :"))
    cgpa = int(input("Current CGPA"))
    database.add_stdent(connection, usn, Name, email, cgpa)

def option_get_std(connection):
    students = database.get_all_std_det(connection)
    for std in students:
      print(" USN : { } Name : '{ }' ".format(std[1] , std[2]))

menu()