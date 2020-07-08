from report_generator.usecases.port import EvaluationReader


class CSVEvaluationReader(EvaluationReader):

    def read(self, evaluation):
        raise NotImplementedError
