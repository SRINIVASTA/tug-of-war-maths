from dataclasses import dataclass
import random
from typing import List


@dataclass
class MathProblem:
    question: str
    answer: str
    choices: List[str]
    topic: str


class MathEngine:

    @staticmethod
    def generate(grade_level: str) -> MathProblem:
        if grade_level == "Class 1 (Add & Subtract ≤ 10)":
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = random.choice(["+", "-"])
            if op == "-" and a < b:
                a, b = b, a
            ans = a + b if op == "+" else a - b
            return MathEngine._build_int_problem(
                f"{a} {op} {b}", ans, "Number Sense"
            )

        elif grade_level == "Class 2-3 (Two-Digit & Intro Mult)":
            op = random.choice(["+", "-", "×"])
            if op == "×":
                a, b = random.randint(2, 10), random.randint(2, 5)
                ans = a * b
            else:
                a, b = random.randint(10, 50), random.randint(5, 25)
                if op == "-" and a < b:
                    a, b = b, a
                ans = a + b if op == "+" else a - b
            return MathEngine._build_int_problem(
                f"{a} {op} {b}", ans, "Operations"
            )

        elif grade_level == "Class 4-5 (Multiplication & Division)":
            op = random.choice(["×", "÷"])
            if op == "×":
                a, b = random.randint(4, 15), random.randint(3, 12)
                ans = a * b
                q = f"{a} × {b}"
            else:
                b = random.randint(2, 12)
                ans = random.randint(3, 15)
                a = b * ans  # Ensures clean whole-number division
                q = f"{a} ÷ {b}"
            return MathEngine._build_int_problem(q, ans, "Mult & Div")

        elif grade_level == "Class 6-7 (Fractions & Percentages)":
            mode = random.choice(["percent", "fraction"])
            if mode == "percent":
                pct = random.choice([10, 20, 25, 50, 75])
                base = random.choice([20, 40, 60, 80, 100, 200])
                ans = int((pct / 100) * base)
                return MathEngine._build_int_problem(
                    f"{pct}% of {base}", ans, "Percentages"
                )
            else:
                denom = random.choice([3, 4, 5, 6, 8, 10])
                n1 = random.randint(1, denom - 1)
                n2 = random.randint(1, denom - n1)
                ans_str = f"{n1 + n2}/{denom}"
                distractors = set()
                while len(distractors) < 3:
                    fake_num = random.randint(1, denom + 2)
                    fake_den = random.choice([denom, denom * 2])
                    cand = f"{fake_num}/{fake_den}"
                    if cand != ans_str:
                        distractors.add(cand)
                choices = list(distractors) + [ans_str]
                random.shuffle(choices)
                return MathProblem(
                    f"{n1}/{denom} + {n2}/{denom}", ans_str, choices, "Fractions"
                )

        else:  # Class 8 (Linear Equations)
            x = random.randint(2, 12)
            m = random.randint(2, 6)
            c = random.randint(1, 15)
            rhs = m * x + c
            return MathEngine._build_int_problem(
                f"Solve x: {m}x + {c} = {rhs}", x, "Algebra"
            )

    @staticmethod
    def _build_int_problem(question: str, ans: int, topic: str) -> MathProblem:
        distractors = set()
        while len(distractors) < 3:
            offset = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
            candidate = ans + offset
            if candidate >= 0 and candidate != ans:
                distractors.add(candidate)
        choices = [str(x) for x in list(distractors) + [ans]]
        random.shuffle(choices)
        return MathProblem(question, str(ans), choices, topic)
