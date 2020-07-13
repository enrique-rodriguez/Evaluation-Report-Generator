from utils.container import Container
from report_generator.usecases import CreateReport
from configuration import config

from report_generator.utils.evaluation_reader import (
    ExcelEvaluationReader,
    CSVEvaluationReader,
    EvaluationReaderConfig
)

from report_generator.utils.report_writer import (
    ExcelReportWriter,
    CSVReportWriter
)

from gui.presenters import (
    TkinterCreateReportPresenter
)

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
    lambda c: TkinterCreateReportPresenter()
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
