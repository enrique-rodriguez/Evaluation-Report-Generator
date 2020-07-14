from .user_settings import user_settings

from report_generator.utils.evaluation_reader import (
    PROFESSOR_SIGNATURE,
    QUESTION_SIGNATURE,
    MAX_POINTS_PER_QUESTION,
    ANSWER_PATTERN,
    QUESTION_PATTERN
)

default_config = {
    "professor_signature": PROFESSOR_SIGNATURE,
    "question_signature": QUESTION_SIGNATURE,
    "max_points_per_question": MAX_POINTS_PER_QUESTION,
    "answer_pattern": ANSWER_PATTERN,
    "question_pattern": QUESTION_PATTERN
}