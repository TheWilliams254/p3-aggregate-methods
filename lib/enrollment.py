class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {} 
    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    @property
    def course_count(self):
        return len(self._enrollments)

    @property
    def average_grade(self):
        if not self._grades:
            return 0
        return sum(self._grades.values()) / len(self._grades)

    def add_grade(self, enrollment, grade):
        if enrollment in self._enrollments:
            self._grades[enrollment] = grade
        else:
            raise ValueError("Enrollment not found for this student")
