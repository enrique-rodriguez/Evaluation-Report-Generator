from .pandas_report_writer import PandasReportWriter


class CSVReportWriter(PandasReportWriter):

    def export_df(self, df, filename):
        df.to_csv(filename, index=False)
