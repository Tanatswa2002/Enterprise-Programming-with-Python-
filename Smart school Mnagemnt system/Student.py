from User import User   #import abstract class acting as blueprint

class Student(User):    #inherits attributes and methods from 'User' class
    def __init__(self, name, age,student_id,grades = None):
        super().__init__(name,age)
        self.student_id  = student_id
        self.grades = grades or []

    def get_role(self):
        return "Student"
    
    def describe(self):
        return f"Role:{ self.get_role()}\n Name:{self.get_name()} \n ID: {self.student_id}  \n Age: {self.get_age()} \n Grades:{self.grades}"
        
    def add_grade(self,grade):
        self.grades.append(grade)

        