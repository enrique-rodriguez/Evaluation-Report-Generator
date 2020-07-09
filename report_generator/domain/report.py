

class Report:

    def __init__(self):
        self.evaluations = list()

    def add(self, evaluation):
        self.evaluations.append(evaluation)

    def __iter__(self):
        return iter(self.evaluations)

    @property
    def number_of_evaluations(self):
        return len(self.evaluations)
