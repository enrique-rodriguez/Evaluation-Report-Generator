from utils import Config

# Load application settings

SETTINGS_FILE = "settings.json"

try:
    user_settings = Config(SETTINGS_FILE)
except FileNotFoundError:
    print("Settings file not found, using default settings")
    user_settings = Config(SETTINGS_FILE, default_config).save()
