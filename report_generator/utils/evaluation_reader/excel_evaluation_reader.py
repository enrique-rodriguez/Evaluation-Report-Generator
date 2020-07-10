import pandas as pd
from .pandas_evaluation_reader import PandasEvaluationReader


class ExcelEvaluationReader(PandasEvaluationReader):

    def get_dataframe(self, filename):
        return pd.read_excel(filename, lineterminator='\n', engine="openpyxl")
