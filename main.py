from university import University
from semester import Semester
from course import Course

# Creating instances
uni = University("Islamia university")
sem1 = Semester("Semester 1")
course1 = Course("C101", "Object Oriented Programming")

# Adding semester and allocating course
uni.add_semester(sem1)
sem1.allocate_course(course1)

# Accessing information
print(uni.name)
print(uni.semesters[0].name)
print(uni.semesters[0].allocated_courses[0].name)