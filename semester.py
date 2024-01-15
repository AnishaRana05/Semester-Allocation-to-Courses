from course import Course

class Semester:
    def __init__(self, number, max_credit_hours):
        self.number = number
        self.max_credit_hours = max_credit_hours
        self.courses = []

    def add_course(self, course):
        if self.remaining_credit_hours() >= course.credit_hours:
            self.courses.append(course)
            return True
        else:
            return False

    def remaining_credit_hours(self):
        used_credit_hours = sum(course.credit_hours for course in self.courses)
        return self.max_credit_hours - used_credit_hours