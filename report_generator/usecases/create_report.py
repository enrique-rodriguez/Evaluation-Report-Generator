from typing import Dict
from report_generator.domain.report import Report

from report_generator.usecases.port import (
    ReportWriter,
    EvaluationReader
)


class CreateReport:

    def __init__(self, readers: Dict[str, EvaluationReader], writer: ReportWriter):
        self.evaluation_readers = readers
        self.report_writer = writer

    def create(self, evaluations=[]):
        if len(evaluations) == 0:
            raise self.EmptyReport

        report, errors = self.get_report(evaluations)

        self.report_writer.write(report)

    def get_report(self, evaluations):
        errors = {}
        report = Report()

        for file in evaluations:
            try:
                reader = self.get_appropriate_reader(file)
                evaluation = reader.read(file)
                report.add(evaluation)
            except Exception as error:
                errors[file] = error

        return report, errors

    def get_appropriate_reader(self, file):
        # Not the best way to know the type of file, but it will have to do
        name, extension = file.split('.')

        if extension not in self.evaluation_readers:
            raise self.EvaluationReaderNotAvailable(extension)

        return self.evaluation_readers.get(extension)

    class EmptyReport(Exception):
        def __init__(self):
            super().__init__("The Report is Empty")

    class EvaluationReaderNotAvailable(Exception):
        def __init__(self, file_extension):
            error = f"Do not know how to read '{file_extension}' files."
            super().__init__(error)
