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
        # --- SCHOOL LEVELS (Class 1–8) ---
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
                pct = random.choice()
                base = random.choice()
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
                p = random.choice()
                r = random.choice()
                t = random.randint(2, 4)
                ans = int((p * r * t) / 100)
                return MathEngine._int_choices(
                    f"Simple Interest: P={p}, R={r}%, T={t}yr",
                    ans,
                    "Financial Math",
                )
            elif mode == "elasticity":
                dq = random.choice()
                dp = random.choice()
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
                return MathEngine._str_choices(q, ans, dist, "Electronics")

        elif level == "B.Tech - Mechanical (Thermo, Fluids & Machine Design)":
            mode = random.choice(["force", "theory"])
            if mode == "force":
                m = random.randint(5, 25)
                a = random.randint(2, 10)
                ans = m * a
                return MathEngine._int_choices(
                    f"Force (N): Mass = {m}kg, Accel = {a}m/s²",
                    ans,
                    "Engg Mechanics",
                )
            mech_bank = [
                ("Bernoulli's equation conserves", "Energy", ["Mass", "Momentum", "Viscosity"]),
                ("Reynolds number > 4000 indicates", "Turbulent flow", ["Laminar flow", "Transitional", "Static"]),
                ("Carnot efficiency depends only on", "Temperatures", ["Working fluid", "Pressure", "Volume"]),
                ("Gear module (m) formula (D=pitch dia, T=teeth)", "D / T", ["T / D", "D × T", "πD / T"]),
            ]
            q, ans, dist = random.choice(mech_bank)
            return MathEngine._str_choices(q, ans, dist, "Thermo & Fluids")

        else:  # B.Tech - Civil (Structures, Geotech, Surveying & Concrete)
            mode = random.choice(["beam_moment", "stress_dynamic", "theory"])
            if mode == "beam_moment":
                w = random.randint(4, 20)
                l = random.randint(2, 8)
                ans = int((w * (l**2)) / 2)
                return MathEngine._int_choices(
                    f"Max BM (kN·m) Cantilever: UDL={w}kN/m, L={l}m",
                    ans,
                    "Structural Analysis",
                )
            elif mode == "stress_dynamic":
                area = random.randint(2, 10)
                stress = random.randint(10, 50)
                force = area * stress
                return MathEngine._int_choices(
                    f"Compressive Stress (MPa): Load={force}kN, Area={area}×10³mm²",
                    stress,
                    "Strength of Materials",
                )
            else:
                civil_bank = [
                    ("Nominal mix ratio for M20 concrete", "1 : 1.5 : 3", ["1 : 2 : 4", "1 : 1 : 2", "1 : 3 : 6"]),
                    ("Bending moment at free end of cantilever", "0", ["WL", "WL/2", "WL²/2"]),
                    ("Max BM of simply supported beam (point load W at center)", "WL / 4", ["WL / 2", "WL / 8", "WL² / 8"]),
                    ("Whole Circle Bearing (WCB) of South", "180°", ["90°", "270°", "360°"]),
                    ("Instrument used to measure horizontal & vertical angles", "Theodolite", ["Dumpy Level", "Planimeter", "Clinometer"]),
                    ("Void ratio (e) in terms of porosity (n)", "n / (1 - n)", ["n / (1 + n)", "1 - n", "n × (1 - n)"]),
                ]
                q, ans, dist = random.choice(civil_bank)
                return MathEngine._str_choices(
                    q, ans, dist, "Geotech, Survey & Concrete"
                )

    @staticmethod
    def _int_choices(
        question: str, ans: int, topic: str, allow_neg: bool = False
    ) -> MathProblem:
        distractors = set()
        while len(distractors) < 3:
            offset = random.choice([-6, -4, -3, -2, -1, 1, 2, 3, 4, 6])
            candidate = ans + offset
            if (allow_neg or candidate >= 0) and candidate != ans:
                distractors.add(candidate)
        choices = [str(x) for x in list(distractors) + [ans]]
        random.shuffle(choices)
        return MathProblem(question, str(ans), choices, topic)

    @staticmethod
    def _str_choices(
        question: str, ans: str, distractors: List[str], topic: str
    ) -> MathProblem:
        choices = list(distractors[:3]) + [ans]
        random.shuffle(choices)
        return MathProblem(question, ans, choices, topic)
