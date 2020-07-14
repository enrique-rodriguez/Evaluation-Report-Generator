from typing import List
from .evaluation import Evaluation


class Report:

    def __init__(self, name: str):
        self.name = name
        self.evaluations: List[Evaluation] = list()

    def add(self, evaluation: Evaluation):
        self.evaluations.append(evaluation)

    def __iter__(self):
        return iter(self.evaluations)

    def __len__(self):
        return len(self.evaluations)