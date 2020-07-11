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

    def create(self, evaluations: List[str], output_file: str):

        report, errors = self.get_report(evaluations)

        if len(report) == 0:
            raise self.EmptyReport

        writer = self.get_appropriate_writer(output_file)

        writer.write(report, output_file)

    def get_report(self, evaluations: List[str]):
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

    def get_appropriate_writer(self, filename: str):
        if '.' not in filename:
            raise ValueError("File has no extension")

        # Not the best way to know the type of file, but it will have to do
        name, extension = filename.split('.')

        if extension not in self.report_writers:
            raise self.ReportWriterNotAvailable(extension)

        return self.report_writers.get(extension)

    def get_appropriate_reader(self, file: str):
        if '.' not in file:
            raise ValueError("File has no extension")

        # Not the best way to know the type of file, but it will have to do
        name, extension = file.split('.')

        if extension not in self.evaluation_readers:
            raise self.EvaluationReaderNotAvailable(extension)

        return self.evaluation_readers.get(extension)

    def get_write_formats(self):
        return list(self.report_writers.keys())

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
