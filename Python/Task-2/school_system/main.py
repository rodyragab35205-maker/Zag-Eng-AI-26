from teachers.teacher_model import Teacher
from courses.course_model import Course
from students.student_model import Student

t1=Teacher(1,"Dr. Ahmed","AI")
s1=Student(10,"Omar","course")
c1=Course(100,"Machine Learning",t1)
s1.enroll(c1)
print(s1.name,"enrolled in:",s1.courses)
