from dataclasses import dataclass

@dataclass
class Evaluation:

    professor: str = ""
    course: str = ""
    student_count: int = 0
    score: int = 0
    maximum: int = 0
    questions: list = None

    @property
    def question_count(self):
        return len(self.questions)

    @property
    def average(self):
        # Formula: number_of_points_obtained / question_count * student_count
        average = self.score/(self.question_count*self.student_count)

        return round(average, 2)
