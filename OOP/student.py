class Student:
    def __init__(self,first_name,last_name,age,country,code,school):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.code = code
        self.school = school
    
    def  greet_student(self):
        greeting = f"Hello {self. first_name} ,welcome to {self.school} your code is {self.code}"
        return  greeting
    
    def greet_student_by_year_of_birth(self):
        greeting = f"Hello {self.first_name}, you were born in {self.age}"
        return greeting

    def display_student_full_name(self):
        name = {self.first_name} +''+ {self.last_name}
        return name
    
          