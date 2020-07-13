from .excel_evaluation_reader import ExcelEvaluationReader
from .csv_evaluation_reader import CSVEvaluationReader
from report_generator.usecases.port.evaluation_reader import EvaluationReaderConfig

ANSWER_PATTERN = "(Excelente|Bueno|Regular|Deficiente) \((?P<points>\d)\)"
PROFESSOR_SIGNATURE = ["Nombre del Instructor:", "Nombre de los recursos:"]
QUESTION_SIGNATURE = "Criterios de evaluación: >>"
MAX_POINTS_PER_QUESTION = 4
