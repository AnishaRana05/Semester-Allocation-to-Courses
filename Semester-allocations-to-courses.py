class Course:
    def __init__(self, name, credit_hours):
        self.name = name
        self.credit_hours = credit_hours

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
        # Create some courses
course1 = Course("Mathematics", 3)
course2 = Course("Computer Science", 4)
course3 = Course("History", 3)

# Create a semester with a maximum credit hours limit
semester1 = Semester(number=1, max_credit_hours=12)

# Add courses to the semester
result1 = semester1.add_course(course1)  # This should succeed
result2 = semester1.add_course(course2)  # This should succeed as well
result3 = semester1.add_course(course3)  # This should fail due to exceeding max credit hours

# Print results
print(f"Course 1 added: {result1}")
print(f"Course 2 added: {result2}")
print(f"Course 3 added: {result3}")

# Check remaining credit hours in the semester
remaining_hours = semester1.remaining_credit_hours()
print(f"Remaining credit hours: {remaining_hours}")