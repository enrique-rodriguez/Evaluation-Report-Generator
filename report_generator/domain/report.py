

class Report:

    def __init__(self):
        self.evaluations = list()

    def add(self, evaluation):
        self.evaluations.append(evaluation)

    def __iter__(self):
        return iter(self.evaluations)

    def __len__(self):
        return len(self.evaluations)
