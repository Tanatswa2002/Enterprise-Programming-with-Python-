#Description
""" Simulate small school managemnt system that will cover: - Polymorphism, abstraction, encapsulation and iheritance and illustrate why these pillars are so important or useful
    The ssytem will manage user data and pergorm takss based on the roles of the user"""

from Student import Student
from Teacher import Teacher
from Admin import Admin
from User import User
    #create objects
student = Student("Tanatswa", 23, "ST123", [85, 90, 78])
teacher = Teacher("Mr. Dube", 40, "Math", 25000)
admin = Admin("Mrs. Moyo", 35, "Admissions")

User = [student, teacher,admin]
for user in User:
    print (user.describe())
    