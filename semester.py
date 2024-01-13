from university import University

class Semester:
    def __init__(self, name):
        self.name = name
        self.allocated_courses = []

    def allocate_course(self, course):
        self.allocated_courses.append(course)