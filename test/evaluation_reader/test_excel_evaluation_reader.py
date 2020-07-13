from unittest import TestCase
from report_generator.utils.evaluation_reader import (
    ExcelEvaluationReader,
    EvaluationReaderConfig
)

from report_generator.utils.evaluation_reader import (
    PROFESSOR_SIGNATURE,
    QUESTION_SIGNATURE,
    MAX_POINTS_PER_QUESTION,
    ANSWER_PATTERN,
    QUESTION_PATTERN
)
reader_config = EvaluationReaderConfig(
    PROFESSOR_SIGNATURE,
    QUESTION_SIGNATURE,
    MAX_POINTS_PER_QUESTION,
    QUESTION_PATTERN,
    ANSWER_PATTERN,
)


class TestExcelEvaluationReader(TestCase):

    def setUp(self):
        self.reader = ExcelEvaluationReader(reader_config)

        self.evaluation = self.reader.read('data/test_evaluation.xlsx')

    def test_get_professors_name(self):

        self.assertEqual(self.evaluation.professor, "Dr. Professor T. Johnson")

    def test_get_number_of_students(self):

        self.assertEqual(self.evaluation.student_count, 13)

    def test_number_of_questions(self):

        self.assertEqual(self.evaluation.question_count, 6)

    def test_get_course_name(self):

        self.assertEqual(self.evaluation.course, "test_evaluation.xlsx")

    def test_raises_invalid_max_points_per_question(self):
        with self.assertRaises(self.reader.InvalidMaximumPointsPerQuestion):
            ExcelEvaluationReader(EvaluationReaderConfig("", "", 0, ""))

    def test_calculate_total_points(self):
        self.assertEqual(self.evaluation.score, 299)

    def test_maximum_score(self):
        self.assertEqual(self.evaluation.maximum, 312)
