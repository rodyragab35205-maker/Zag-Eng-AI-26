class User:
    def __init__(self,name,email,_password):
        self.name = name
        self.email = email
        self._password = _password
    def set_password(self,new_password):
        self._password=new_password
    def check_password(self, password):
        return self._password==password
    def show_info(self):
        return f"Name: {self.name}, |Email: {self.email}"
class Student(User):
    def __init__(self, name, email, _password,level):
        super().__init__(name, email, _password)
        self.level = level
    def show_info(self):
        return f"Student: {self.name}, | Level: {self.level}"
class Instructor(User):
    def __init__(self, name, email, _password,speciality):
        super().__init__(name, email, _password)
        self.speciality = speciality
    def show_info(self):
        return f"Instructor: {self.name}, | Speciality: {self.speciality}"
s=Student("Ali","ali@gmail.com","1234","Beginner")
i=Instructor("Mona","mona@gmail.com","abcd","Machine Learning")
print(s.show_info())
print(i.show_info())
print(s.check_password("1234"))