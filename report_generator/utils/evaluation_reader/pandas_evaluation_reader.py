import abc
import pandas as pd
from os import path
from functools import reduce
from report_generator.domain import Evaluation
from report_generator.usecases.port import (
    EvaluationReader,
    EvaluationReaderConfig
)


class PandasEvaluationReader(EvaluationReader, abc.ABC):

    def __init__(self, config: EvaluationReaderConfig):
        super().__init__(config)
        self.df = None
        self.filename = None

    @abc.abstractmethod
    def get_dataframe(cls, filename):
        pass

    def read(self, filename: str):
        try:
            self.df = self.get_dataframe(filename)
            self.filename = filename
        except Exception as error:
            raise self.ParsingError(filename, error)

        evaluation = Evaluation(
            professor=self.get_professors_name(),
            course=self.get_course_name(),
            student_count=self.get_number_of_students(),
            question_count=self.get_number_of_questions(),
            score=self.calculate_total_points(),
            maximum=self.get_maximum_score()
        )

        return evaluation

    def get_professors_name(self):
        if self.instructor_signature not in self.df.columns:
            raise self.ColumnNotFound(self.instructor_signature)

        return self.df[self.instructor_signature].mode().iloc[0]

    def calculate_total_points(self):

        def calculator(total, match): return total + \
            int(match.group('points')) if match else total

        total_points = 0

        for column in self.df.columns:
            if column.startswith(self.question_signature):
                matches = [self.program.match(
                    element) for element in self.df[column] if isinstance(element, str)]
                total_points += reduce(calculator, matches, 0)

        return total_points

    def get_course_name(self):
        # Just return the name of the file since
        # the name of the course is not mentioned anywhere else
        return path.basename(self.filename)

    def get_number_of_students(self):
        row_count, _ = self.df.shape

        return row_count

    def get_number_of_questions(self):
        def count_questions(total, question):
            if question.startswith(self.question_signature):
                return total + 1
            return total

        return reduce(count_questions, self.df.columns, 0)//self.max_points_per_question

    def get_maximum_score(self):
        return self.max_points_per_question *\
            self.get_number_of_questions() *\
            self.get_number_of_students()

    class ColumnNotFound(Exception):
        def __init__(self, column):
            super().__init__(f"The following column was not found: {column}")
