from report_generator.usecases.port import ReportWriter
from report_generator.domain import Report


class PDFReportWriter(ReportWriter):

    def write(self, report: Report, filename: str):
        raise NotImplementedError