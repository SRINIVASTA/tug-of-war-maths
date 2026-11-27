import pytest
from src.engine import MathEngine

ALL_STREAMS = [
    "Class 1 (Add & Subtract ≤ 10)",
    "Class 2-5 (Operations & Mult/Div)",
    "Class 6-8 (Percentages & Algebra)",
    "Inter - MPC (Calculus, Matrices & Trig)",
    "Inter - BiPC (Genetics, pH & Bio-Calculations)",
    "Inter - MEC / CEC (Commerce, Economics & Stats)",
    "B.Tech - CSE / IT (Discrete Math, Binary & Big-O)",
    "B.Tech - ECE / EEE (Circuits, Signals & Laplace)",
    "B.Tech - Mechanical (Thermo, Fluids & Machine Design)",
    "B.Tech - Civil (Structures, Geotech, Surveying & Concrete)",
]


@pytest.mark.parametrize("stream", ALL_STREAMS)
def test_all_streams_generate_valid_problems(stream):
    for _ in range(50):
        prob = MathEngine.generate(stream)
        assert isinstance(prob.question, str) and len(prob.question) > 0
        assert isinstance(prob.topic, str) and len(prob.topic) > 0
        assert prob.answer in prob.choices
        assert len(prob.choices) == 4
        assert len(set(prob.choices)) == 4


def test_class_1_no_negatives():
    for _ in range(50):
        prob = MathEngine.generate("Class 1 (Add & Subtract ≤ 10)")
        assert int(prob.answer) >= 0


def test_btech_cse_binary_format():
    for _ in range(50):
        prob = MathEngine.generate(
            "B.Tech - CSE / IT (Discrete Math, Binary & Big-O)"
        )
        if "to Binary" in prob.question:
            assert set(prob.answer).issubset({"0", "1"})


def test_btech_ece_laplace_format():
    for _ in range(50):
        prob = MathEngine.generate(
            "B.Tech - ECE / EEE (Circuits, Signals & Laplace)"
        )
        if "Laplace" in prob.question:
            assert prob.answer.startswith("1/(s+")


def test_btech_civil_positive_values():
    for _ in range(50):
        prob = MathEngine.generate(
            "B.Tech - Civil (Structures, Geotech, Surveying & Concrete)"
        )
        if "Cantilever" in prob.question or "Compressive Stress" in prob.question:
            assert int(prob.answer) > 0
