import abc


class CreateReportPresenter(abc.ABC):

    @abc.abstractmethod
    def present(self, errors, files_written):
        pass
