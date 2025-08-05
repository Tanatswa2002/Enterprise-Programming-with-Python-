#Admin class 
from User import User
class Admin(User):

	def __init__(self, name,age, department):
		super().__init__(name, age)
		self.department = department 

	def get_role(self):
		return "Admin"

	def describe(self):
		return f"Role:{self.get_role()}\n Name: {self.get_name()} \nAge: {self.get_age()} \nDepartment: {self.department} "