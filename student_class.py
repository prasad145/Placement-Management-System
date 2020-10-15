
# class to create student database
class Student:

    def __init__(self, USN, first_name, Last_Name, Sem, CGPA, Current_Backlogs, Phone_Number):
        self.USN = USN
        self.first_name = first_name
        self.Last_Name = Last_Name
        self.Sem = Sem 
        self.CGPA = CGPA
        self.Current_Backlogs = Current_Backlogs
        self.Phone_Number = Phone_Number

    
    def __repr__(self):
        return "Student({}, {}, {}, {}, {}, {}, {})".format(self.USN, self.first_name, self.Last_Name, self.Sem, self.CGPA, self.Current_Backlogs, self.Phone_Number)
