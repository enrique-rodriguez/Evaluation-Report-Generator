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

        student_count = self.get_number_of_students()
        questions = self.get_questions(student_count)

        evaluation = Evaluation(
            professor=self.get_professors_name(),
            course=self.get_course_name(),
            student_count=student_count,
            score=self.calculate_total_points(questions),
            maximum=self.get_maximum_score(len(questions), student_count),
            questions=questions
        )

        return evaluation

    def get_professors_name(self):

        for signature in self.instructor_signature:
            if signature in self.df.columns:
                return self.df[signature].mode().iloc[0]

        raise self.InstructorColumnNotFound

    def calculate_total_points(self, questions):
        return sum([points for points, maximum in questions.values()])

    def get_course_name(self):
        # Just return the name of the file since
        # the name of the course is not mentioned anywhere else
        return path.basename(self.filename)

    def get_number_of_students(self):
        row_count, _ = self.df.shape

        return row_count

    def get_maximum_score(self, number_questions, number_of_students):
        return self.max_points_per_question *\
            number_questions *\
            number_of_students

    def get_questions(self, student_count):

        questions = {}

        for column in self.df.columns:
            match = self.question_matcher.match(column)

            if not match:
                continue

            question_title = match.group(1)
            column_sum = self.get_column_sum(column)

            if question_title not in questions:
                max_possible = student_count*self.max_points_per_question
                questions[question_title] = [column_sum, max_possible]
            else:
                questions[question_title][0] += column_sum

        return questions

    def get_column_sum(self, column):
        total = 0

        for element in self.df[column]:
            if isinstance(element, str):
                total += int(self.answer_matcher.match(element).group('points'))

        return total

    class InstructorColumnNotFound(Exception):
        def __init__(self):
            super().__init__("Instructor Column Not Found")
