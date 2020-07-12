from .pandas_report_writer import PandasReportWriter


class ExcelReportWriter(PandasReportWriter):

    def export_df(self, df, filename):
        df.to_excel(filename, index=False)
