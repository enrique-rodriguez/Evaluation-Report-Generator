from report_generator.usecases.port import EvaluationReader
from report_generator.domain import Evaluation


class CSVEvaluationReader(EvaluationReader) -> Evaluation:

    def read(self, evaluation) -> Evaluation:
        raise NotImplementedError
