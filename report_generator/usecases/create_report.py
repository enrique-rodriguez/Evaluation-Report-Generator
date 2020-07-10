from typing import Dict, List
from report_generator.domain.report import Report

from report_generator.usecases.port import (
    ReportWriter,
    EvaluationReader
)


class CreateReport:

    def __init__(self, readers: Dict[str, EvaluationReader], writers: Dict[str, ReportWriter]):
        self.evaluation_readers = readers
        self.report_writers = writers

    def create(self, evaluations: List[str], output_format: str):
        if len(evaluations) == 0:
            raise self.EmptyReport

        report, errors = self.get_report(evaluations)

        writer = self.get_appropriate_writer(output_format)
        writer.write(report)

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

    def get_appropriate_writer(self, output_format):

        if output_format not in self.report_writers:
            raise self.ReportWriterNotAvailable(output_format)

        return self.report_writers.get(output_format)

    def get_appropriate_reader(self, file):
        # Not the best way to know the type of file, but it will have to do
        if '.' not in file:
            raise ValueError("File has no extension")

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

    class ReportWriterNotAvailable(Exception):
        def __init__(self, output_format):
            error = f"Do not know how to write to '{output_format}' file."
            super().__init__(error)
