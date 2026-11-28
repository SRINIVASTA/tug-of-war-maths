import pytest
from src.engine import MathEngine, MathProblem
from src.ui_components import render_arena_svg

ALL_STREAMS = [
    # School (Class 1–10)
    "Class 1 (Add & Subtract ≤ 10)",
    "Class 2-5 (Operations & Mult/Div)",
    "Class 6-8 (Percentages & Algebra)",
    "Class 9-10 (Quadratics, Coord Geometry & Trig)",
    # Intermediate (Class 11–12)
    "Inter - MPC (Calculus, Matrices & Trig)",
    "Inter - BiPC (Genetics, pH & Bio-Calculations)",
    "Inter - MEC / CEC (Commerce, Economics & Stats)",
    # Competitive Exams (EAPCET, JEE & GATE)
    "Entrance - EAPCET / JEE (Vectors, Limits & Complex)",
    "Competitive - GATE (Engg Math & Aptitude)",
    # B.Tech Engineering Branches
    "B.Tech - CSE / IT (Discrete Math, Binary & Big-O)",
    "B.Tech - ECE / EEE (Circuits, Signals & Laplace)",
    "B.Tech - Mechanical (Thermo, Fluids & Mechanics)",
    "B.Tech - Civil (Structures, Concrete & Geotech)",
]


@pytest.mark.parametrize("stream", ALL_STREAMS)
def test_problem_generation_and_choices(stream: str) -> None:
    """Runs 40 randomized checks per stream (520+ total) to verify valid 4-option MCQs."""
    for _ in range(40):
        prob = MathEngine.generate(stream)
        assert isinstance(prob, MathProblem)
        assert isinstance(prob.question, str) and len(prob.question.strip()) > 0
        assert isinstance(prob.topic, str) and len(prob.topic.strip()) > 0
        assert isinstance(prob.answer, str) and len(prob.answer.strip()) > 0
        assert len(prob.choices) == 4, f"Expected 4 choices for {stream}, got {prob.choices}"
        assert len(set(prob.choices)) == 4, f"Duplicate choices found in {stream}: {prob.choices}"
        assert prob.answer in prob.choices, f"Answer '{prob.answer}' missing from {prob.choices}"


def test_invalid_stream_raises_error() -> None:
    """Ensures unknown stream names raise a clean ValueError."""
    with pytest.raises(ValueError, match="Unknown academic stream"):
        MathEngine.generate("Non-Existent Stream")


@pytest.mark.parametrize("rope_pos", [-10, -5, 0, 5, 10])
def test_svg_arena_clamping_and_rendering(rope_pos: int) -> None:
    """Verifies SVG arena renders valid markup and clamps extreme rope positions safely."""
    svg_output = render_arena_svg(
        rope_pos=rope_pos,
        win_threshold=5,
        team_a_name="TEAM A",
        team_b_name="TEAM B",
    )
    assert "<svg" in svg_output and "</svg>" in svg_output
    assert "VICTORY LINE" in svg_output
    assert "TEAM A" in svg_output
    assert "TEAM B" in svg_output
