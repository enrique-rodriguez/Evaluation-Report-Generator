import abc


class EvaluationReader(abc.ABC):

    @abc.abstractmethod
    def read(self, evaluation):
        pass
