import abc

from report_generator.domain.evaluation import Evaluation


class EvaluationReader(abc.ABC):

    @abc.abstractmethod
    def read(self, evaluation):
        pass

    class ParsingError(Exception):
        def __init__(self, error):
            super().__init__(f"Error parsing file: {error}")
