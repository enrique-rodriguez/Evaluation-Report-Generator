from unittest import TestCase
from unittest.mock import Mock
from report_generator.usecases import CreateReport


class TestCreateReport(TestCase):

    def setUp(self):
        readers = {'csv': Mock()}
        writers = {'csv': Mock()}

        self.create_report = CreateReport(readers=readers, writers=writers)

    def test_raises_empty_report(self):
        with self.assertRaises(self.create_report.EmptyReport):
            self.create_report.create([], 'report.csv')

    def test_evaluation_added_to_report(self):
        self.create_report.create(['file.csv'], 'file.csv')

    def test_raises_reader_not_available(self):
        with self.assertRaises(self.create_report.EvaluationReaderNotAvailable):
            self.create_report.get_appropriate_reader('file.txt')

    def test_raises_writer_not_available(self):
        with self.assertRaises(self.create_report.ReportWriterNotAvailable):
            self.create_report.get_appropriate_writer("file.docx")
