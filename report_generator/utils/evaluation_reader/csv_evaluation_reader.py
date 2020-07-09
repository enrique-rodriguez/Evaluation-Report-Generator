import pandas as pd
from functools import reduce
from report_generator.usecases.port import EvaluationReader
from report_generator.domain import Evaluation


class CSVEvaluationReader(EvaluationReader):

    def __init__(self, question_signature, maximum_points_per_question):
        super().__init__(question_signature, maximum_points_per_question)
        self.df = None

    def read(self, file):
        self.df = pd.read_csv(file, lineterminator='\n')

        evaluation = Evaluation(
            professor=self.get_professors_name(),
            course=None,
            student_count=self.get_number_of_students(),
            question_count=self.get_number_of_questions(),
            score=0,
            maximum=1
        )

        return evaluation

    def get_professors_name(self):
        return self.df["Nombre del Instructor:"].mode().iloc[0]

    def calculate_total_points(self):
        pass

    def get_course_name(self):
        pass

    def get_number_of_students(self):
        row_count, col_count = self.df.shape

        return row_count

    def get_number_of_questions(self):
        def count_questions(total, question):
            if question.startswith(self.question_signature):
                return total + 1
            return total

        return reduce(count_questions, self.df.columns, 0)//self.max_points_per_question
