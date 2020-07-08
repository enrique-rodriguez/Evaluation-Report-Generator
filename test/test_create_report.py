from unittest import TestCase
from unittest.mock import Mock
from report_generator.usecases import CreateReport


class TestCreateReport(TestCase):

    def setUp(self):
        report_writer = Mock()
        self.create_report = CreateReport(report_writer)

    def test_raises_empty_report(self):

        with self.assertRaises(self.create_report.EmptyReport):
            self.create_report.create()
