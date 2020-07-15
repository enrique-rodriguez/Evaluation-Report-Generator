from unittest import TestCase
from unittest.mock import Mock
from report_generator.usecases import CreateReport
from report_generator.usecases.port.presenter import CreateReportPresenter
from report_generator.usecases.port.evaluation_reader import EvaluationReader
from report_generator.usecases.port.report_writer import ReportWriter
from report_generator.domain import Evaluation


class MockCSVEvaluationReader(Mock):

    def read(self, filename):

        if not filename.endswith('.csv'):
            raise EvaluationReader.ParsingError(
                filename, "Can only read csv file")

        return Evaluation("", filename, 1, 4, 4, ['question'])


class MockReportWriter(Mock):

    def write(self, report):
        return len(report)


class MockPresenter(Mock, CreateReportPresenter):

    def __init__(self):
        super().__init__()
        self.errors = {}
        self.files_written = 0

    def present(self, errors, files_written):
        self.errors = errors
        self.files_written = files_written


class TestCreateReport(TestCase):

    def setUp(self):
        readers = {'csv': MockCSVEvaluationReader()}
        writers = {'csv': MockReportWriter()}
        presenter = MockPresenter()

        self.create_report = CreateReport(
            readers=readers,
            writers=writers,
            presenter=presenter)

    def test_raises_no_files_provided(self):
        with self.assertRaises(ValueError):
            self.create_report.create([], 'report.csv')

    def test_raises_empty_report(self):
        with self.assertRaises(self.create_report.EmptyReport):
            self.create_report.create([''], 'report.csv')

    def test_evaluation_added_to_report(self):
        self.create_report.create(['file.csv'], 'file.csv')
        self.assertEqual(self.create_report.presenter.files_written, 1)

    def test_raises_reader_not_available(self):
        with self.assertRaises(self.create_report.EvaluationReaderNotAvailable):
            self.create_report.read_evaluation_file('file.txt')

    def test_raises_writer_not_available(self):
        with self.assertRaises(self.create_report.ReportWriterNotAvailable):
            self.create_report.get_appropriate_writer("file.docx")

    def test_no_evaluation_files_provided(self):
        with self.assertRaises(ValueError):
            self.create_report.create([], 'report.csv')
