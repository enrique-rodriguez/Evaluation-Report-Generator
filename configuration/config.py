import json


class Config:

    def __init__(self, file, settings=None):
        self.file = file

        if settings:
            self.settings = settings
        else:
            self.settings = Config.open(file)

    def __getitem__(self, attr):
        return self.settings[attr]

    def __setitem__(self, key, value):
        self.settings[key] = value

    def save(self):
        if self.settings is None:
            raise ValueError("Nothing to save. Empty config.")

        with open(self.file, 'w') as file:
            json.dump(self.settings, file)

    @staticmethod
    def open(filename):
        with open(filename, 'r') as file:
            return json.load(file)
