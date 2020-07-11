import pandas as pd
from report_generator.usecases.port import ReportWriter
from report_generator.domain import Report


class CSVReportWriter(ReportWriter):

    def write(self, report: Report, filename: str):

        df = pd.DataFrame({
            "Profesor": [evaluation.professor for evaluation in report],
            "Curso": [evaluation.course for evaluation in report],
            "Numero de Estudiantes": [evaluation.student_count for evaluation in report],
            "Numero de Preguntas": [evaluation.question_count for evaluation in report],
            "Puntuación Obtenida": [evaluation.score for evaluation in report],
            "Puntuación Máxima": [evaluation.maximum for evaluation in report],
            "Promedio": [evaluation.average for evaluation in report]
        })

        df.to_csv(filename, index=False)
