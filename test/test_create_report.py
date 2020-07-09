from unittest import TestCase
from unittest.mock import Mock
from report_generator.usecases import CreateReport


class TestCreateReport(TestCase):

    def setUp(self):
        reader = Mock()
        writer = Mock()

        self.create_report = CreateReport(reader=reader, writer=reader)

    def test_raises_empty_report(self):
        with self.assertRaises(self.create_report.EmptyReport):
            self.create_report.create()

    def test_evaluation_added_to_report(self):
        self.create_report.add('file.csv')
        self.create_report.create()
