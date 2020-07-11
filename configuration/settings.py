import json
from utils.container import Container

from report_generator.usecases import CreateReport

from report_generator.utils.evaluation_reader import (
    ExcelEvaluationReader,
    CSVEvaluationReader,
    EvaluationReaderConfig
)

ANSWER_PATTERN = "(Excelente|Bueno|Regular|Deficiente) \((?P<points>\d)\)"
PROFESSOR_SIGNATURE = "Nombre del Instructor:"
QUESTION_SIGNATURE = "Criterios de evaluación: >>"
MAX_POINTS_PER_QUESTION = 4


default_config = {
    "professor_signature": PROFESSOR_SIGNATURE,
    "question_signature": QUESTION_SIGNATURE,
    "max_points_per_question": MAX_POINTS_PER_QUESTION,
    "answer_pattern": ANSWER_PATTERN
}

try:
    settings = open('settings.json', 'r')
    config = json.load(settings_file)
    settings.close()
except FileNotFoundError:
    config = default_config


container = Container()

# Reader Initialization

container.register(
    "EvaluationReaderConfig",
    lambda c: EvaluationReaderConfig(
        config["professor_signature"],
        config["question_signature"],
        config["max_points_per_question"],
        config["answer_pattern"]
    )
)

container.register(
    "EvaluationReaders",
    lambda c: {
        'csv': CSVEvaluationReader(c.get("EvaluationReaderConfig")),
        'xlsx': ExcelEvaluationReader(c.get("EvaluationReaderConfig"))
    }
)

# TODO: Writer Initialization. Add writers here

# Use Case Initialization

container.register(
    "CreateReport",
    lambda c: CreateReport(
        readers=c.get("EvaluationReaders"),
        writers={
            'csv': None,
            'xlsx': None
        }
    )
)
