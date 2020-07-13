from .config import Config

from report_generator.utils.evaluation_reader import (
    PROFESSOR_SIGNATURE,
    QUESTION_SIGNATURE,
    MAX_POINTS_PER_QUESTION,
    ANSWER_PATTERN
)

default_config = {
    "professor_signature": PROFESSOR_SIGNATURE,
    "question_signature": QUESTION_SIGNATURE,
    "max_points_per_question": MAX_POINTS_PER_QUESTION,
    "answer_pattern": ANSWER_PATTERN
}

# Load application settings

SETTINGS_FILE = "settings.json"

try:
    config = Config(SETTINGS_FILE)
except FileNotFoundError:
    print("Settings file not found, using default settings")
    config = Config(SETTINGS_FILE, default_config).save()
