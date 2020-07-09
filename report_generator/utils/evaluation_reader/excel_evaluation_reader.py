from report_generator.usecases.port import EvaluationReader
from report_generator.domain import Evaluation


class ExcelEvaluationReader(EvaluationReader) -> Evaluation:

    def read(self, evaluation):
        raise NotImplementedError
