import abc


class ReportWriter(abc.ABC):

    @abc.abstractmethod
    def write(self, report):
        pass
