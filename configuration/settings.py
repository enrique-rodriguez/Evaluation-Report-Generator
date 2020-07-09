import json
from utils.container import Container

container = Container()

with open('settings.json', 'r') as settings_file:
    config = json.load(settings_file)
