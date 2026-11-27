import pytest
from src.engine import MathEngine

ALL_GRADES = [
    "Class 1 (Add & Subtract ≤ 10)",
    "Class 2-3 (Two-Digit & Intro Mult)",
    "Class 4-5 (Multiplication & Division)",
    "Class 6-7 (Fractions & Percentages)",
    "Class 8 (Linear Equations)",
]


@pytest.mark.parametrize("grade", ALL_GRADES)
def test_all_grades_generate_valid_problems(grade):
    for _ in range(50):
        prob = MathEngine.generate(grade)
        assert isinstance(prob.question, str) and len(prob.question) > 0
        assert isinstance(prob.answer, str)
        assert prob.answer in prob.choices
        assert len(prob.choices) == 4
        assert len(set(prob.choices)) == 4


def test_class_1_no_negatives():
    for _ in range(50):
        prob = MathEngine.generate("Class 1 (Add & Subtract ≤ 10)")
        assert int(prob.answer) >= 0


def test_class_8_algebra_solution():
    for _ in range(50):
        prob = MathEngine.generate("Class 8 (Linear Equations)")
        assert prob.question.startswith("Solve x:")
        assert 2 <= int(prob.answer) <= 12
