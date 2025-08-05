#Teacher class

from User import User

class Teacher(User):
	
	def __init__(self, age, name,subject, salary):
		super().__init__(name, age)
		self.__salary = salary
		self.subject = subject


	def get_role(self):
		return f"{self.subject} Teacher"

	def describe(self):
		return f"Role: {self.get_role()} Name: {self.get_name()} Age: {self.get_age()} Subject:{self.subject}"

	def get_salary(self):
		return f"R{self.__salary: .2f}"
