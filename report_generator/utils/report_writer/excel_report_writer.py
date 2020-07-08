from report_generator.usecases.port import ReportWriter


class ExcelReportWriter(ReportWriter):

    def write(self, report):
        raise NotImplementedError
