from unittest import TestCase
from report_generator.utils.evaluation_reader.csv_evaluation_reader import (
    CSVEvaluationReader
)

ANSWER_PATTERN = "(Excelente|Bueno|Regular|Deficiente) \((?P<points>\d)\)"
PROFESSOR_SIGNATURE = "Nombre del Instructor:"
QUESTION_SIGNATURE = "Criterios de evaluación: >>"
MAX_POINTS_PER_QUESTION = 4


class TestCSVEvaluationReader(TestCase):

    def setUp(self):
        self.reader = CSVEvaluationReader(
            PROFESSOR_SIGNATURE,
            QUESTION_SIGNATURE,
            MAX_POINTS_PER_QUESTION,
            ANSWER_PATTERN
        )
        self.evaluation = self.reader.read('data/test_evaluation.csv')

    def test_get_professors_name(self):

        self.assertEqual(self.evaluation.professor, "Dr. Professor T. Johnson")

    def test_get_number_of_students(self):

        self.assertEqual(self.evaluation.student_count, 13)

    def test_number_of_questions(self):

        self.assertEqual(self.evaluation.question_count, 6)

    def test_get_course_name(self):

        self.assertEqual(self.evaluation.course, "test_evaluation.csv")

    def test_raises_invalid_max_points_per_question(self):
        with self.assertRaises(self.reader.InvalidMaximumPointsPerQuestion):
            CSVEvaluationReader('professor', 'question', 0, ANSWER_PATTERN)

    def test_calculate_total_points(self):
        self.assertEqual(self.evaluation.score, 299)

    def test_maximum_score(self):
        self.assertEqual(self.evaluation.maximum, 312)
