from unittest import TestCase
from report_generator.utils.evaluation_reader.csv_evaluation_reader import (
    CSVEvaluationReader
)


class TestCSVEvaluationReader(TestCase):

    def setUp(self):
        self.reader = CSVEvaluationReader("Criterios de evaluación: >>", 4)
        self.evaluation = self.reader.read('data/test_evaluation.csv')

    def test_get_professors_name(self):

        self.assertEqual(self.evaluation.professor, "Dr. Professor T. Johnson")

    def test_get_number_of_students(self):

        self.assertEqual(self.evaluation.student_count, 13)

    def test_number_of_questions(self):

        self.assertEqual(self.evaluation.question_count, 6)

    def test_get_course_name(self):

        self.assertEqual(self.evaluation.course, "test_evaluation.csv")
