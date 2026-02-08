class Student:
    def __init__(self,id,name,courses):
        self.id=id
        self.name=name
        self.courses=[]
    def enroll(self,course):
        self.courses.append(course.title)