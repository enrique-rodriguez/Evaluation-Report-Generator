import json
from utils.container import Container
from report_generator.usecases import CreateReport

from .config import Config

from report_generator.utils.evaluation_reader import (
    ExcelEvaluationReader,
    CSVEvaluationReader,
    EvaluationReaderConfig
)

from report_generator.utils.report_writer import (
    ExcelReportWriter,
    CSVReportWriter
)

from report_generator.presenters.console import (
    ConsoleCreateReportPresenter
)

SETTINGS_FILE = "settings.json"

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
    config = Config(SETTINGS_FILE)
except FileNotFoundError:
    print("Settings file not found, using default settings")
    config = Config(SETTINGS_FILE, default_config)
    config.save()

# Stores all of the dependencies in one place for easy access
container = Container()

# Utilities initialization
container.register(
    "EvaluationReaderConfig",
    lambda c: EvaluationReaderConfig(
        config["professor_signature"],
        config["question_signature"],
        config["max_points_per_question"],
        config["answer_pattern"]
    )
)

# Readers Initialization
container.register(
    "EvaluationReaders",
    lambda c: {
        'csv': CSVEvaluationReader(c.get("EvaluationReaderConfig")),
        'xlsx': ExcelEvaluationReader(c.get("EvaluationReaderConfig"))
    }
)

# Writers Initialization
container.register(
    "ReportWriters",
    lambda c: {
        'csv': CSVReportWriter(),
        'xlsx': ExcelReportWriter(),
    }
)

# Presenters initialization

container.register(
    "CreateReportPresenter",
    lambda c: ConsoleCreateReportPresenter()
)

# Use Case Initialization
container.register(
    "CreateReport",
    lambda c: CreateReport(
        readers=c.get("EvaluationReaders"),
        writers=c.get("ReportWriters"),
        presenter=c.get("CreateReportPresenter")
    )
)
