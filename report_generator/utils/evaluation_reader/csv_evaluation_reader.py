import pandas as pd
from functools import reduce
from os import path
from report_generator.usecases.port import EvaluationReader
from report_generator.domain import Evaluation


class CSVEvaluationReader(EvaluationReader):

    def __init__(self, question_signature, maximum_points_per_question):
        super().__init__(question_signature, maximum_points_per_question)
        self.df = None
        self.filename = None

    def read(self, filename):
        self.df = pd.read_csv(filename, lineterminator='\n')
        self.filename = filename

        evaluation = Evaluation(
            professor=self.get_professors_name(),
            course=self.get_course_name(),
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
        # Just return the name of the file since
        # the name of the course its not mentioned anywhere else
        return path.basename(self.filename)

    def get_number_of_students(self):
        row_count, col_count = self.df.shape

        return row_count

    def get_number_of_questions(self):
        def count_questions(total, question):
            if question.startswith(self.question_signature):
                return total + 1
            return total

        return reduce(count_questions, self.df.columns, 0)//self.max_points_per_question
