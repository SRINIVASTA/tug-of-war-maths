# 🪢 Tug-of-War Maths, Engineering & IQ Arena

An enterprise-grade, multi-device classroom, laboratory, and home-learning competition platform built with **Python** and **Streamlit**. Two teams compete simultaneously to pull a virtual tug-of-war rope across the victory line by solving curriculum-aligned problems across **Brain Training & IQ Puzzles**, **School (Class 1–10)**, **Intermediate (MPC, BiPC, MEC, CEC)**, **Competitive Exams (EAPCET, JEE, GATE)**, and **B.Tech Engineering (CSE/IT, ECE/EEE, Mechanical, Civil)** streams.

## About

Tug-of-War Maths, Engineering & IQ Arena transforms passive screen time and problem-solving into an active, collaborative team challenge designed for **Mobile Phones, Tablets, Laptops, and Interactive Classroom Smartboards**.

Built and maintained by [@SRINIVASTA](https://github.com/SRINIVASTA), this repository features a decoupled 14-stream problem engine, a real-time dynamic SVG vector arena with 3 illustrated players per team, instant toast answer feedback, celebratory victory animations, responsive split-screen mobile/desktop CSS, and automated CI/CD unit testing via GitHub Actions.

## Modules in this repo

| Module | Description |
| :--- | :--- |
| `src/engine.py` | Decoupled problem generator and validator supporting **14 distinct academic & IQ streams** across Brain Training, School (Class 1–10), Intermediate, Competitive Exams (EAPCET/JEE/GATE), and B.Tech branches with randomized multiple-choice distractors. |
| `src/ui_components.py` | Responsive dark-mode CSS injector (optimized for Mobile, Tablet, Laptop & Smartboard), custom SVG vector tug-of-war arena (3 players per team with dynamic rope physics), and fixed bottom branding bar with contact links. |
| `app.py` | Main Streamlit web application handling side-by-side split-screen team controls, instant toast feedback, victory balloons, session state tracking, response-time telemetry, and one-click CSV report exports. |
| `tests/test_engine.py` | Automated `pytest` suite executing **560+ randomized checks** across all 14 academic/IQ streams and SVG rendering helpers. |

### Architecture & Workflow

```mermaid
flowchart TD
    subgraph User_Interface_Layer["User Interface Layer - Mobile, Tablet & Smartboard"]
        A["app.py<br>Responsive Split-Screen Streamlit Gateway"] e1@-->|"Select Stream & Win Threshold"| B{"Curriculum & IQ Stream Router"}
    end

    subgraph Problem_Engine_Layer["src/engine.py - 14-Stream Problem Generator"]
        B e2@-->|"IQ & Class 1 - 10"| C["Brain Training & School Engine<br>Series, Coding, Arithmetic, Quadratics & Trig"]
        B e3@-->|"Inter MPC / BiPC / MEC / CEC"| D["Intermediate Engine<br>Calculus, Matrices, Bio-pH & Commerce"]
        B e4@-->|"EAPCET / JEE / GATE & B.Tech"| E["Competitive & Engineering Engine<br>Vectors, Eigenvalues, Binary, Laplace, Thermo & Civil"]
    end

    subgraph Gameplay_Telemetry_Layer["Session State & Telemetry Engine"]
        C e5@-->|"4 Tap Choices"| F["Answer & Speed Validator + Toast Feedback"]
        D e6@-->|"4 Tap Choices"| F
        E e7@-->|"4 Tap Choices"| F
        F e8@-->|"Correct Answer"| G["Rope Physics Shift ±1<br>& Victory Balloons Trigger"]
        F e9@-->|"Every Attempt"| H["Pandas Session Logger<br>One-Click CSV Export"]
    end

    subgraph Visual_Rendering_Layer["src/ui_components.py - Vector Arena"]
        G e10@-->|"Clamped Rope Position"| I["Dynamic SVG Arena<br>6 Players + Victory Line"]
    end

    e1@{ animate: true }
    e2@{ animate: true }
    e3@{ animate: true }
    e4@{ animate: true }
    e5@{ animate: true }
    e6@{ animate: true }
    e7@{ animate: true }
    e8@{ animate: true }
    e9@{ animate: true }
    e10@{ animate: true }
```

### Supported Academic & Brain-Training Streams (14 Tracks)

* **Brain Training & IQ:** Number Series Patterns, Alphabet Coding-Decoding, Analogies, Clock Angles, and Logical Brain-Teasers.
* **School Levels (Class 1–10):**
  * **Class 1–8:** Addition & Subtraction (≤ 10), Multi-digit Operations, Multiplication/Division, Percentages, and Linear Equations.
  * **Class 9–10:** Quadratic Equation Roots, Coordinate Geometry Distances, Trigonometry Identities, and Basic Probability.
* **Intermediate (Class 11–12):**
  * **MPC:** Determinants, Derivatives, and Trigonometry.
  * **BiPC:** pH/pOH Calculations, Cellular Respiration ATP, and Mendelian Genetics Ratios.
  * **MEC / CEC:** Simple Interest, Price Elasticity of Demand, Accountancy, and Statistics.
* **Entrance & Competitive Exams:**
  * **EAPCET / JEE:** Vector Dot Products, Complex Number Modulus, Limits, and Rapid Physics/Chemistry Concepts.
  * **GATE:** Engineering Mathematics (Eigenvalues, Matrix Trace, Differential Equations, Probability) and Quantitative Aptitude.
* **B.Tech Engineering Branches:**
  * **CSE / IT:** Binary Conversion, Modular Arithmetic, Algorithm Time Complexity (Big-O), and Networking.
  * **ECE / EEE:** Ohm's Law Networks, Dynamic Laplace Transforms, Nyquist Sampling, and Digital Gates.
  * **Mechanical:** Engineering Mechanics, Fluid Dynamics (Bernoulli/Reynolds), Thermodynamics, and Machine Design.
  * **Civil:** Cantilever Bending Moments, Compressive Stress, Concrete Mix Ratios, and Geotech.

### Key Capabilities

* **Multi-Device Responsive Split-Screen UI:** Fluid flexbox and `clamp()` styling keeps both teams side-by-side on **Mobile Phones, Tablets, Laptops, and Classroom Smartboards**.
* **Dynamic Vector Tug-of-War Arena:** Custom SVG canvas featuring 3 leaning players per side and a central victory flag that shifts smoothly with every correct answer.
* **Instant Feedback & Celebrations:** Real-time `st.toast` alerts confirm correct/wrong answers immediately, accompanied by celebratory balloons (`st.balloons()`) on match victory.
* **Teacher & Faculty Analytics:** Tracks per-team accuracy and response times in seconds, exportable as a `.CSV` report at the end of any session.

## 📲 Mobile App Installation (100% Safe — No APK Required)

Students, parents, and teachers can install this directly onto any **Android** or **iOS** home screen safely without downloading external `.apk` files:

1. Open the live link in **Google Chrome** (Android) or **Safari** (iOS):
   `[https://streamlit.app](https://tug-of-war-maths-g4xuhkbc5jggrcgvcskg9f.streamlit.app/)`
2. Tap the **3 dots (`⋮`)** in Chrome (or **Share (`↑`)** in Safari).
3. Tap **"Install and create shortcut"** ➔ **"Install"** (or **"Add to Home Screen"**).

## Repository Structure

```text
tug-of-war-maths/
├── .github/
│   └── workflows/
│       └── ci.yml              # Automated pytest quality gate on push/PR
├── .streamlit/
│   └── config.toml             # Dark theme & minimal toolbar configuration
├── src/
│   ├── __init__.py
│   ├── engine.py               # 14-stream problem & choice generator
│   └── ui_components.py        # Responsive SVG arena, multi-device CSS & footer
├── tests/
│   └── test_engine.py          # Parametrized unit tests across all 14 streams
├── .gitignore
├── app.py                      # Main split-screen web application
├── Dockerfile                  # Container setup for self-hosted lab servers
├── README.md
└── requirements.txt            # Production Python dependencies
```

## Installation & Local Setup

### 1. Clone the repository

```bash
git clone https://github.com
cd tug-of-war-maths
```

### 2. Set up Python environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run unit tests

```bash
python -m pytest
```

### 4. Launch the application

```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`.

## License

This repository is licensed under the MIT License — Copyright (c) 2026 [SRINIVASTA](https://github.com/SRINIVASTA).

## Disclaimer

This application is designed for educational engagement, classroom gamification, cognitive skill-building, and academic practice across school, competitive exam, and engineering curricula.

## ⭐ Support & Contribution

If you clone, test, or deploy this project in your classroom, lab, or home, please consider giving it a **Star (⭐)** on GitHub!

* **Found a bug or want to add a new subject track?** Open an [Issue](https://github.com).
* **Want to contribute?** Fork this repository and submit a Pull Request.

---

* **Lead Architect & Developer:** [T A Srinivas (Srinivasta)](https://github.com/SRINIVASTA) • **Tanakala AI Solutions**

### 🌐 Let’s Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/srinivas-t-a-557637119/)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/srinivasta)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tasrinivass@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SRINIVASTA)
[![Website](https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=website&logoColor=white)](https://srinivasta.github.io)

💡 *“Bridging two decades of analytical expertise with modern AI and interactive engineering to build engaging, real-world learning systems.”*
