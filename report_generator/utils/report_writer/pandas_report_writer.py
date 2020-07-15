import abc
import pandas as pd
from report_generator.usecases.port import ReportWriter
from report_generator.domain import Report


class PandasReportWriter(ReportWriter, abc.ABC):

    @abc.abstractmethod
    def export_df(self, df, filename):
        pass

    def get_grade_string(self, question):
        obtained, maximum = question

        return f"{obtained}/{maximum}"

    def write(self, report: Report):

        df = pd.DataFrame(self.get_statistics(report))

        self.add_questions_to_df(df, report)
        
        try:
            self.export_df(df, report.name)
        except Exception as error:
            raise self.WriteError(error)

        write_count = df.shape[0]

        return write_count

    def add_questions_to_df(self, df, report):
        reference = report.evaluations[0]

        for question in reference.questions:
            df[question] = [self.get_grade_string(
                evaluation.questions[question]) for evaluation in report.evaluations]

    def get_statistics(self, report):
        return {
            "Profesor": [evaluation.professor for evaluation in report],
            "Curso": [evaluation.course for evaluation in report],
            "Numero de Estudiantes": [evaluation.student_count for evaluation in report],
            "Numero de Preguntas": [evaluation.question_count for evaluation in report],
            "Puntuación Obtenida": [evaluation.score for evaluation in report],
            "Puntuación Máxima": [evaluation.maximum for evaluation in report],
            "Promedio": [evaluation.average for evaluation in report]
        }
