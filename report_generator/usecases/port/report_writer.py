import abc

from report_generator.domain import Report


class ReportWriter(abc.ABC):

    @abc.abstractmethod
    def write(self, report: Report):
        pass
    
    class WriteError(Exception):
        def __init__(self, error):
            super().__init__(f"There was a problem writing to file: {error}")