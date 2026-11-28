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
    def generate(level: str) -> MathProblem:
        # --- SCHOOL LEVELS (Class 1–10) ---
        if level == "Class 1 (Add & Subtract ≤ 10)":
            a, b = random.randint(1, 10), random.randint(1, 10)
            op = random.choice(["+", "-"])
            if op == "-" and a < b:
                a, b = b, a
            ans = a + b if op == "+" else a - b
            return MathEngine._int_choices(f"{a} {op} {b}", ans, "Number Sense")

        elif level == "Class 2-5 (Operations & Mult/Div)":
            op = random.choice(["+", "-", "×", "÷"])
            if op == "×":
                a, b = random.randint(3, 15), random.randint(3, 12)
                ans = a * b
            elif op == "÷":
                b = random.randint(2, 12)
                ans = random.randint(3, 15)
                a = b * ans
            else:
                a, b = random.randint(15, 60), random.randint(5, 30)
                if op == "-" and a < b:
                    a, b = b, a
                ans = a + b if op == "+" else a - b
            return MathEngine._int_choices(f"{a} {op} {b}", ans, "Arithmetic")

        elif level == "Class 6-8 (Percentages & Algebra)":
            if random.choice([True, False]):
                pct = random.choice([10, 20, 25, 50, 75])
                base = random.choice([40, 60, 80, 100, 120, 200])
                ans = int((pct / 100) * base)
                return MathEngine._int_choices(
                    f"{pct}% of {base}", ans, "Percentages"
                )
            x = random.randint(2, 12)
            m = random.randint(2, 6)
            c = random.randint(1, 15)
            return MathEngine._int_choices(
                f"Solve x: {m}x + {c} = {m*x + c}", x, "Algebra"
            )

        elif level == "Class 9-10 (Quadratics, Coord Geometry & Trig)":
            mode = random.choice(["quad", "coord", "trig_10"])
            if mode == "quad":
                r1, r2 = random.randint(1, 6), random.randint(2, 7)
                b_coef = -(r1 + r2)
                c_coef = r1 * r2
                ans = r1 + r2
                return MathEngine._int_choices(
                    f"Sum of roots: x² {b_coef}x + {c_coef} = 0",
                    ans,
                    "Quadratic Equations",
                )
            elif mode == "coord":
                x, y = random.choice([(3, 4), (6, 8), (5, 12), (8, 15), (9, 12)])
                ans = int((x**2 + y**2) ** 0.5)
                return MathEngine._int_choices(
                    f"Distance of ({x}, {y}) from origin",
                    ans,
                    "Coordinate Geometry",
                )
            else:
                trig10_bank = [
                    ("If sin(θ) = 3/5, find cos(θ)", "4/5", ["3/4", "5/3", "1/5"]),
                    ("Value of 9·sec²A - 9·tan²A", "9", ["1", "0", "8"]),
                    ("If tan(A) = 1, angle A is", "45°", ["30°", "60°", "90°"]),
                    ("Probability of getting Head in 1 toss", "1/2", ["1/4", "1", "0"]),
                ]
                q, ans, dist = random.choice(trig10_bank)
                return MathEngine._str_choices(q, ans, dist, "Class 10 Trig & Stats")

        # --- INTERMEDIATE (Class 11–12 Groups) ---
        elif level == "Inter - MPC (Calculus, Matrices & Trig)":
            mode = random.choice(["det", "deriv", "trig"])
            if mode == "det":
                a, b = random.randint(2, 8), random.randint(1, 6)
                c, d = random.randint(1, 6), random.randint(2, 8)
                ans = a * d - b * c
                return MathEngine._int_choices(
                    f"Det |[{a}, {b}], [{c}, {d}]|",
                    ans,
                    "Matrices",
                    allow_neg=True,
                )
            elif mode == "deriv":
                n = random.randint(2, 5)
                x = random.randint(1, 4)
                ans = n * (x ** (n - 1))
                return MathEngine._int_choices(
                    f"d/dx (x^{n}) at x={x}", ans, "Calculus"
                )
            else:
                trig_bank = [
                    ("sin(30°) + cos(60°)", "1", ["0", "1/2", "√3/2"]),
                    ("tan(45°) + sec(0°)", "2", ["1", "0", "√2"]),
                    ("sin²(30°) + cos²(30°)", "1", ["1/2", "3/4", "0"]),
                    ("2·sin(30°)·cos(30°)", "√3/2", ["1/2", "1", "1/√2"]),
                ]
                q, ans, dist = random.choice(trig_bank)
                return MathEngine._str_choices(q, ans, dist, "Trigonometry")

        elif level == "Inter - BiPC (Genetics, pH & Bio-Calculations)":
            bipc_bank = [
                ("pH of 0.001 M HCl solution", "3", ["1", "2", "4"]),
                ("pOH of solution with pH = 9", "5", ["9", "4", "7"]),
                ("ATP net gain in Glycolysis", "2", ["4", "36", "38"]),
                ("Monohybrid F2 phenotypic ratio", "3:1", ["1:2:1", "9:3:3:1", "1:1"]),
                ("Dihybrid F2 phenotypic ratio", "9:3:3:1", ["3:1", "1:2:1", "2:1"]),
                ("Human diploid chromosome count", "46", ["23", "44", "48"]),
                ("mRNA codon length (bases)", "3", ["2", "4", "6"]),
            ]
            q, ans, dist = random.choice(bipc_bank)
            return MathEngine._str_choices(q, ans, dist, "BiPC Core")

        elif level == "Inter - MEC / CEC (Commerce, Economics & Stats)":
            mode = random.choice(["si", "elasticity", "commerce"])
            if mode == "si":
                p = random.choice([1000, 2000, 5000, 10000])
                r = random.choice([5, 8, 10, 12])
                t = random.randint(2, 4)
                ans = int((p * r * t) / 100)
                return MathEngine._int_choices(
                    f"Simple Interest: P={p}, R={r}%, T={t}yr",
                    ans,
                    "Financial Math",
                )
            elif mode == "elasticity":
                dq = random.choice([10, 20, 30, 40])
                dp = random.choice([5, 10])
                ans = int(dq / dp)
                return MathEngine._int_choices(
                    f"Price Elasticity: %ΔQ={dq}%, %ΔP={dp}%", ans, "Economics"
                )
            else:
                comm_bank = [
                    ("Assets = ₹50k, Liabilities = ₹18k. Capital = ?", "₹32k", ["₹68k", "₹18k", "₹22k"]),
                    ("Mean of 10, 20, 30, 40, 50", "30", ["25", "35", "20"]),
                    ("Median of 4, 8, 12, 16, 20", "12", ["10", "14", "16"]),
                ]
                q, ans, dist = random.choice(comm_bank)
                return MathEngine._str_choices(
                    q, ans, dist, "Accountancy & Stats"
                )
        # --- COMPETITIVE EXAMS (EAPCET, JEE & GATE) ---
        elif level == "Entrance - EAPCET / JEE (Vectors, Limits & Complex)":
            mode = random.choice(["vectors", "complex", "formula_bank"])
            if mode == "vectors":
                a1, a2 = random.randint(1, 5), random.randint(1, 5)
                b1, b2 = random.randint(1, 5), random.randint(1, 5)
                ans = (a1 * b1) + (a2 * b2)
                return MathEngine._int_choices(
                    f"Dot product: ({a1}i + {a2}j) · ({b1}i + {b2}j)",
                    ans,
                    "Vector Algebra",
                )
            elif mode == "complex":
                x, y = random.choice([(3, 4), (5, 12), (8, 15), (7, 24)])
                ans = int((x**2 + y**2) ** 0.5)
                return MathEngine._int_choices(
                    f"Modulus |{x} + {y}i|", ans, "Complex Numbers"
                )
            else:
                jee_bank = [
                    ("lim (x→0) [sin(5x) / x]", "5", ["1", "0", "1/5"]),
                    ("Value of i^4 + i^2 (where i = √-1)", "0", ["2", "-2", "1"]),
                    ("Slope of line perpendicular to 2x + y = 5", "1/2", ["-2", "2", "-1/2"]),
                    ("Dimensional formula of Force", "[MLT⁻²]", ["[ML²T⁻²]", "[MLT⁻¹]", "[MT⁻²]"]),
                    ("Bond order of O₂ molecule", "2", ["1", "2.5", "3"]),
                ]
                q, ans, dist = random.choice(jee_bank)
                return MathEngine._str_choices(q, ans, dist, "EAPCET / JEE Rapid")

        elif level == "Competitive - GATE (Engg Math & Aptitude)":
            mode = random.choice(["eigen", "aptitude", "gate_bank"])
            if mode == "eigen":
                a, d = random.randint(2, 9), random.randint(2, 9)
                b, c = random.randint(1, 5), random.randint(1, 5)
                ans = a + d
                return MathEngine._int_choices(
                    f"Sum of eigenvalues of [[{a}, {b}], [{c}, {d}]]",
                    ans,
                    "Linear Algebra",
                )
            elif mode == "aptitude":
                n = random.randint(6, 12)
                ans = (n * (n - 1)) // 2
                return MathEngine._int_choices(
                    f"Total handshakes among {n} people",
                    ans,
                    "General Aptitude",
                )
            else:
                gate_bank = [
                    ("Trace of a 3×3 Identity Matrix", "3", ["1", "0", "9"]),
                    ("If P(A)=0.4, P(B)=0.5 (independent), P(A∩B)=", "0.2", ["0.9", "0.1", "0.45"]),
                    ("Integrating factor of dy/dx + 2y = e^x", "e^(2x)", ["e^x", "2x", "e^(-2x)"]),
                    ("Rank of a 3×3 zero matrix", "0", ["1", "3", "Undefined"]),
                ]
                q, ans, dist = random.choice(gate_bank)
                return MathEngine._str_choices(q, ans, dist, "GATE Engg Math")

        # --- B.TECH (All Engineering Branches Separately) ---
        elif level == "B.Tech - CSE / IT (Discrete Math, Binary & Big-O)":
            mode = random.choice(["binary", "mod", "theory"])
            if mode == "binary":
                num = random.randint(5, 31)
                ans = bin(num)[2:]
                distractors = set()
                while len(distractors) < 3:
                    fake = bin(random.randint(4, 31))[2:]
                    if fake != ans:
                        distractors.add(fake)
                return MathEngine._str_choices(
                    f"Decimal {num} to Binary",
                    ans,
                    list(distractors),
                    "Digital Logic",
                )
            elif mode == "mod":
                a = random.randint(25, 99)
                b = random.randint(4, 12)
                ans = a % b
                return MathEngine._int_choices(
                    f"Compute: {a} mod {b}", ans, "Discrete Math"
                )
            else:
                cse_bank = [
                    ("Worst-case time of Binary Search", "O(log n)", ["O(n)", "O(n²)", "O(1)"]),
                    ("Worst-case time of Merge Sort", "O(n log n)", ["O(n²)", "O(n)", "O(log n)"]),
                    ("Max nodes in binary tree of height h", "2^(h+1) - 1", ["2^h", "2h + 1", "h²"]),
                    ("IPv4 address bit length", "32 bits", ["64 bits", "128 bits", "16 bits"]),
                ]
                q, ans, dist = random.choice(cse_bank)
                return MathEngine._str_choices(
                    q, ans, dist, "Algorithms & Networks"
                )

        elif level == "B.Tech - ECE / EEE (Circuits, Signals & Laplace)":
            mode = random.choice(["ohm", "laplace_dynamic", "theory"])
            if mode == "ohm":
                i = random.randint(2, 10)
                r = random.randint(5, 20)
                ans = i * r
                return MathEngine._int_choices(
                    f"Voltage (V) if I = {i}A, R = {r}Ω", ans, "Network Theory"
                )
            elif mode == "laplace_dynamic":
                a = random.randint(2, 9)
                q = f"Laplace L{{e^(-{a}t)}}"
                ans = f"1/(s+{a})"
                dist = [f"1/(s-{a})", f"{a}/(s+{a})", f"s/(s+{a})"]
                return MathEngine._str_choices(q, ans, dist, "Signals & Systems")
            else:
                ece_bank = [
                    ("Nyquist sampling rate (max freq fm)", "2·fm", ["fm", "fm/2", "4·fm"]),
                    ("Ideal Op-Amp input impedance", "Infinity", ["Zero", "50 Ω", "1 kΩ"]),
                    ("NAND gate output when A=1, B=1", "0", ["1", "High-Z", "X"]),
                ]
                q, ans, dist = random.choice(ece_bank)
                return MathEngine._str_choices(q, ans, dist, "Electronics & Digital")

        elif level == "B.Tech - Mechanical (Thermo, Fluids & Mechanics)":
            mech_bank = [
                ("Force (N) for mass 15 kg, accel 4 m/s²", "60 N", ["19 N", "3.75 N", "30 N"]),
                ("Reynolds number > 4000 in pipe indicates", "Turbulent flow", ["Laminar flow", "Transitional", "Static"]),
                ("First Law of Thermodynamics expresses", "Energy conservation", ["Entropy increase", "Absolute zero", "Heat transfer"]),
                ("Power (W) if Torque = 50 N·m, ω = 20 rad/s", "1000 W", ["2.5 W", "70 W", "500 W"]),
            ]
            q, ans, dist = random.choice(mech_bank)
            return MathEngine._str_choices(q, ans, dist, "Mechanical Core")

        elif level == "B.Tech - Civil (Structures, Concrete & Geotech)":
            civil_bank = [
                ("Max bending moment of cantilever (load P, len L)", "P·L", ["P·L / 2", "P·L / 4", "P·L² / 2"]),
                ("Nominal mix ratio for M20 grade concrete", "1 : 1.5 : 3", ["1 : 2 : 4", "1 : 3 : 6", "1 : 1 : 2"]),
                ("Compressive stress if Load = 200 kN, Area = 0.04 m²", "5000 kPa", ["8 kPa", "500 kPa", "2000 kPa"]),
                ("Void ratio (e) in terms of porosity (n)", "n / (1 - n)", ["n / (1 + n)", "1 - n", "n · (1 - n)"]),
            ]
            q, ans, dist = random.choice(civil_bank)
            return MathEngine._str_choices(q, ans, dist, "Civil Engineering")

        # --- BRAIN TRAINING & LOGICAL REASONING ---
        elif level == "Brain Training - Logical Reasoning & IQ Puzzles":
            mode = random.choice(["series", "coding", "iq_bank"])
            if mode == "series":
                series_type = random.choice(["sq_plus", "arith", "geom"])
                if series_type == "sq_plus":
                    start = random.randint(1, 5)
                    seq = [n * n + 1 for n in range(start, start + 4)]
                    ans = (start + 4) ** 2 + 1
                elif series_type == "arith":
                    start = random.randint(2, 12)
                    diff = random.randint(3, 9)
                    seq = [start + i * diff for i in range(4)]
                    ans = start + 4 * diff
                else:
                    start = random.randint(1, 4)
                    seq = [start * (2**i) for i in range(4)]
                    ans = start * 16
                q = f"Next in series: {', '.join(map(str, seq))}, ?"
                return MathEngine._int_choices(q, ans, "Number Series")
            elif mode == "coding":
                word = random.choice(["CAT", "BAT", "DOG", "SUN", "MAP", "PEN", "BOX", "WIN"])
                ans = sum(ord(ch) - 64 for ch in word)
                return MathEngine._int_choices(
                    f"If A=1, B=2..., value of '{word}' =",
                    ans,
                    "Coding-Decoding",
                )
            else:
                iq_bank = [
                    ("Odd one out: 2, 3, 5, 9, 11", "9", ["2", "3", "11"]),
                    ("Clock angle between hands at 3:00", "90°", ["60°", "120°", "180°"]),
                    ("If 5 machines take 5 min for 5 widgets, 100 machines take?", "5 min", ["100 min", "20 min", "1 min"]),
                    ("A farmer has 17 sheep; all but 9 die. How many are left?", "9", ["8", "17", "0"]),
                    ("Which number comes next: 1, 1, 2, 3, 5, 8, ?", "13", ["11", "12", "15"]),
                    ("Doctor : Hospital :: Teacher : ?", "School", ["Court", "Laboratory", "Bank"]),
                    ("Mirror image time of 8:00 on analog clock", "4:00", ["8:00", "2:00", "10:00"]),
                ]
                q, ans, dist = random.choice(iq_bank)
                return MathEngine._str_choices(q, ans, dist, "Logical & IQ Puzzles")

        else:
            raise ValueError(f"Unknown academic stream: {level}")

    @staticmethod
    def _int_choices(
        question: str, answer: int, topic: str, allow_neg: bool = False
    ) -> MathProblem:
        distractors = set()
        while len(distractors) < 3:
            offset = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 10])
            fake = answer + offset
            if fake != answer and (allow_neg or fake >= 0):
                distractors.add(fake)
        choices = [str(answer)] + [str(d) for d in distractors]
        random.shuffle(choices)
        return MathProblem(
            question=question, answer=str(answer), choices=choices, topic=topic
        )

    @staticmethod
    def _str_choices(
        question: str, answer: str, distractors: List[str], topic: str
    ) -> MathProblem:
        choices = [answer] + distractors[:3]
        random.shuffle(choices)
        return MathProblem(
            question=question, answer=answer, choices=choices, topic=topic
        )
