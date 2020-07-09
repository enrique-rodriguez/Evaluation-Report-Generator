from unittest import TestCase
from unittest.mock import Mock
from report_generator.usecases import CreateReport


class TestCreateReport(TestCase):

    def setUp(self):
        readers = {'csv': Mock()}
        writer = Mock()

        self.create_report = CreateReport(readers=readers, writer=writer)

    def test_raises_empty_report(self):
        with self.assertRaises(self.create_report.EmptyReport):
            self.create_report.create()

    def test_evaluation_added_to_report(self):
        self.create_report.create(['file.csv'])

    def test_raises_reader_not_available(self):
        with self.assertRaises(self.create_report.EvaluationReaderNotAvailable):
            self.create_report.get_appropriate_reader('file.txt')
