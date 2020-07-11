

class Evaluation:

    def __init__(self, professor: str, course: str, student_count: int, question_count: int, score: int, maximum: int):
        self.professor = professor
        self.course = course
        self.student_count = student_count
        self.question_count = question_count
        self.score = score
        self.maximum = maximum

    @property
    def average(self):
        # Formula: number_of_points_obtained / question_count * student_count
        average = self.score/(self.question_count*self.student_count)

        return round(average, 2)
