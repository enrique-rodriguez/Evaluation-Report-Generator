import abc

from report_generator.domain.evaluation import Evaluation


class EvaluationReader(abc.ABC):

    def __init__(self, question_signature, max_points_per_question):
        self.question_signature = question_signature
        self.max_points_per_question = max_points_per_question

    @abc.abstractmethod
    def read(self, evaluation):
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

    class ParsingError(Exception):
        def __init__(self, error):
            super().__init__(f"Error parsing file: {error}")
