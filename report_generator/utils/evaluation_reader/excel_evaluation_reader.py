from report_generator.usecases.port import EvaluationReader


class ExcelEvaluationReader(EvaluationReader):

    def read(self, evaluation):
        raise NotImplementedError
