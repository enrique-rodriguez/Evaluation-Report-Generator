import abc

from report_generator.domain import Report


class ReportWriter(abc.ABC):

    @abc.abstractmethod
    def write(self, report: Report):
        pass
