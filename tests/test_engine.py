from src.engine import MathEngine


def test_grade_1_no_negatives():
    for _ in range(50):
        prob = MathEngine.generate("Grade 1 (Addition/Subtraction ≤ 10)")
        assert prob.answer >= 0
        assert prob.answer in prob.choices
        assert len(prob.choices) == 4


def test_grade_2_3_valid_choices():
    for _ in range(50):
        prob = MathEngine.generate("Grade 2-3 (Two-Digit & Intro Mult)")
        assert prob.answer in prob.choices
        assert len(set(prob.choices)) == 4
