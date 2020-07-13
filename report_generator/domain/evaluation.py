

class Evaluation:

    def __init__(self, professor: str, course: str, student_count: int, score: int, maximum: int, questions: list):
        self.professor = professor
        self.course = course
        self.student_count = student_count
        self.score = score
        self.maximum = maximum
        self.questions = questions

    @property
    def question_count(self):
        return len(self.questions)

    @property
    def average(self):
        # Formula: number_of_points_obtained / question_count * student_count
        average = self.score/(self.question_count*self.student_count)

        return round(average, 2)
