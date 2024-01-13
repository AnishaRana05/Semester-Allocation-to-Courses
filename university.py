class University:
    def __init__(self, name):
        self.name = name
        self.semesters = []

    def add_semester(self, semester):
        self.semesters.append(semester)