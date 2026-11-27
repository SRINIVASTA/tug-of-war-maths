from dataclasses import dataclass
import random
from typing import List


@dataclass
class MathProblem:
    question: str
    answer: int
    choices: List[int]
    topic: str


class MathEngine:

    @staticmethod
    def generate(grade_level: str) -> MathProblem:
        if grade_level == "Grade 1 (Addition/Subtraction ≤ 10)":
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = random.choice(["+", "-"])
            if op == "-" and a < b:
                a, b = b, a
            ans = a + b if op == "+" else a - b
            topic = "Number Sense"
        elif grade_level == "Grade 2-3 (Two-Digit & Intro Mult)":
            op = random.choice(["+", "-", "×"])
            if op == "×":
                a, b = random.randint(2, 10), random.randint(2, 5)
                ans = a * b
            else:
                a, b = random.randint(10, 50), random.randint(5, 25)
                if op == "-" and a < b:
                    a, b = b, a
                ans = a + b if op == "+" else a - b
            topic = "Operations"
        else:
            a, b = random.randint(4, 15), random.randint(3, 12)
            op = "×"
            ans = a * b
            topic = "Multiplication"

        distractors = set()
        while len(distractors) < 3:
            offset = random.choice([-4, -3, -2, -1, 1, 2, 3, 4, 5])
            candidate = ans + offset
            if candidate >= 0 and candidate != ans:
                distractors.add(candidate)

        choices = list(distractors) + [ans]
        random.shuffle(choices)
        return MathProblem(f"{a} {op} {b}", ans, choices, topic)
