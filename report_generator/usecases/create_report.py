from report_generator.domain.report import Report

from report_generator.usecases.port import (
    ReportWriter,
    EvaluationReader
)


class CreateReport:

    def __init__(self, reader: EvaluationReader, writer: ReportWriter):
        self.evaluation_reader = reader
        self.report_writer = writer
        self.report = Report()

    def add(self, file):
        evaluation = self.evaluation_reader.read(file)
        self.report.add(evaluation)

    def create(self):
        if self.report.number_of_evaluations == 0:
            raise self.EmptyReport

    class EmptyReport(Exception):
        def __init__(self):
            super().__init__("The Report is Empty")
