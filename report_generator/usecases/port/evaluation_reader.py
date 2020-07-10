import abc
import re
from report_generator.domain.evaluation import Evaluation


class EvaluationReader(abc.ABC):

    def __init__(self, instructor_signature: str, question_signature: str, max_points_per_question: int, answer_pattern: str):
        if max_points_per_question == 0:
            raise self.InvalidMaximumPointsPerQuestion(max_points_per_question)

        self.program = re.compile(answer_pattern)
        self.instructor_signature = instructor_signature
        self.question_signature = question_signature
        self.max_points_per_question = max_points_per_question

    @abc.abstractmethod
    def read(self, filename: str):
        pass

    @abc.abstractmethod
    def calculate_total_points(self):
        pass

    @abc.abstractmethod
    def get_professors_name(self):
        pass

    @abc.abstractmethod
    def get_course_name(self):
        pass

    @abc.abstractmethod
    def get_number_of_students(self):
        pass

    @abc.abstractmethod
    def get_number_of_questions(self):
        pass

    class InvalidMaximumPointsPerQuestion(Exception):
        def __init__(self, max_points_per_question):
            error = f"Invalid maximum points per question: {max_points_per_question}"
            super().__init__(error)

    class ParsingError(Exception):
        def __init__(self, filename, error):
            super().__init__(f"Error reading file '{filename}': {error}")
