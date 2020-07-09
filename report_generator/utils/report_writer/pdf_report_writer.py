from report_generator.usecases.port import ReportWriter


class PDFReportWriter(ReportWriter):

    def write(self, report):
        raise NotImplementedError
