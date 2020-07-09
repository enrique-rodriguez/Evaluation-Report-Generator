

class Evaluation:

    def __init__(self, professor, course, student_count, question_count, score, maximum):
        self.professor = professor
        self.course = course
        self.student_count = student_count
        self.question_count = question_count
        self.score = score
        self.maximum = maximum

    @property
    def average(self):
        # Formula: number_of_points_obtained / question_count * student_count
        return 0
