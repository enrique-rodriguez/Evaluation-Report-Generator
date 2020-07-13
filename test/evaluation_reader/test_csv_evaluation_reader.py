from unittest import TestCase
from report_generator.usecases.port import EvaluationReaderConfig
from report_generator.utils.evaluation_reader.csv_evaluation_reader import (
    CSVEvaluationReader,
)

from report_generator.utils.evaluation_reader import (
    PROFESSOR_SIGNATURE,
    QUESTION_SIGNATURE,
    MAX_POINTS_PER_QUESTION,
    QUESTION_PATTERN,
    ANSWER_PATTERN
)

reader_config = EvaluationReaderConfig(
    PROFESSOR_SIGNATURE,
    QUESTION_SIGNATURE,
    MAX_POINTS_PER_QUESTION,
    QUESTION_PATTERN,
    ANSWER_PATTERN
)


class TestCSVEvaluationReader(TestCase):

    def setUp(self):
        self.reader = CSVEvaluationReader(reader_config)
        self.evaluation = self.reader.read('data/test_evaluation.csv')
        self.evaluation2 = self.reader.read('data/test_evaluation2.csv')

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
            CSVEvaluationReader(EvaluationReaderConfig())

    def test_calculate_total_points(self):
        self.assertEqual(self.evaluation.score, 299)

    def test_maximum_score(self):
        self.assertEqual(self.evaluation.maximum, 312)

    def test_average_score(self):
        self.assertAlmostEqual(self.evaluation.average, 3.83)

    def test_each_question_score(self):
        expected = [84]
        index = 0

        for question, values in self.evaluation2.questions.items():
            self.assertEqual(values[0], expected[index])
            index += 1
            break
