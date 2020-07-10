import pandas as pd
from .pandas_evaluation_reader import PandasEvaluationReader


class CSVEvaluationReader(PandasEvaluationReader):

    def get_dataframe(self, filename):
        return pd.read_csv(filename, lineterminator='\n')
