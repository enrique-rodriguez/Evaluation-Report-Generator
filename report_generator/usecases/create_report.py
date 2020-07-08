from report_generator.usecases.port import ReportWriter


class CreateReport:

    def __init__(self, report_writer: ReportWriter, evaluations=[]):
        self.report_writer = report_writer
        self.evaluations = evaluations

    def create(self):
        if len(self.evaluations) == 0:
            raise self.EmptyReport

    class EmptyReport(Exception):
        def __init__(self):
            super().__init__(self, "The Report is Empty")
