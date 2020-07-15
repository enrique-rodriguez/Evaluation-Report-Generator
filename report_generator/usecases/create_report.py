from typing import Dict, List
from report_generator.domain.report import Report

from report_generator.usecases.port.presenter import (
    CreateReportPresenter
)

from report_generator.usecases.port import (
    ReportWriter,
    EvaluationReader
)


class CreateReport:

    def __init__(self, readers: Dict[str, EvaluationReader], writers: Dict[str, ReportWriter], presenter: CreateReportPresenter):
        self.evaluation_readers = readers
        self.report_writers = writers
        self.presenter = presenter
        self.errors = {}

    def create(self, evaluations: List[str], output_file: str):

        if len(evaluations) == 0:
            raise ValueError("No files provided, no report to create.")

        report = self.get_report(evaluations, output_file)

        if len(report) == 0:
            raise self.EmptyReport(self.errors)

        writer = self.get_appropriate_writer(output_file)

        total_written = writer.write(report)

        self.presenter.present(self.errors, total_written)

    def get_report(self, evaluations: List[str], name: str):
        self.errors.clear()
        report = Report(name)

        for file in evaluations:
            try:
                evaluation = self.read_evaluation_file(file)
                report.add(evaluation)
            except Exception as error:
                self.errors[file] = error

        return report

    def get_appropriate_writer(self, filename: str):
        if '.' not in filename:
            raise ValueError("File has no extension")

        name, extension = filename.split('.')

        if extension not in self.report_writers:
            raise self.ReportWriterNotAvailable(extension)

        return self.report_writers.get(extension)

    def read_evaluation_file(self, file: str):

        for file_format, reader in self.evaluation_readers.items():
            try:
                evaluation = reader.read(file)
                return evaluation
            except EvaluationReader.ParsingError:
                pass

        raise self.EvaluationReaderNotAvailable(file)

    def get_write_formats(self):
        return list(self.report_writers.keys())

    class EmptyReport(Exception):
        def __init__(self, errors):
            super().__init__("The Report is Empty")
            self.errors = errors

    class EvaluationReaderNotAvailable(Exception):
        def __init__(self, file):
            error = f"No reader available for {file}."
            super().__init__(error)

    class ReportWriterNotAvailable(Exception):
        def __init__(self, output_format):
            error = f"Do not know how to write to '{output_format}' file."
            super().__init__(error)
