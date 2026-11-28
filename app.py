import time
import pandas as pd
import streamlit as st
from src.engine import MathEngine
from src.ui_components import inject_kiosk_css, render_arena_svg, render_footer

st.set_page_config(
    page_title="Tug-of-War Maths & Engineering Arena",
    page_icon="🪢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_kiosk_css()

STREAMS = (
    "Brain Training - Logical Reasoning & IQ Puzzles",
    "Class 1 (Add & Subtract ≤ 10)",
    "Class 2-5 (Operations & Mult/Div)",
    "Class 6-8 (Percentages & Algebra)",
    "Class 9-10 (Quadratics, Coord Geometry & Trig)",
    "Inter - MPC (Calculus, Matrices & Trig)",
    "Inter - BiPC (Genetics, pH & Bio-Calculations)",
    "Inter - MEC / CEC (Commerce, Economics & Stats)",
    "Entrance - EAPCET / JEE (Vectors, Limits & Complex)",
    "Competitive - GATE (Engg Math & Aptitude)",
    "B.Tech - CSE / IT (Discrete Math, Binary & Big-O)",
    "B.Tech - ECE / EEE (Circuits, Signals & Laplace)",
    "B.Tech - Mechanical (Thermo, Fluids & Mechanics)",
    "B.Tech - Civil (Structures, Concrete & Geotech)",
)

WIN_OPTIONS = (3, 5, 7, 10)


def init_session() -> None:
    if "stream" not in st.session_state:
        st.session_state.stream = STREAMS[0]
    if "win_threshold" not in st.session_state:
        st.session_state.win_threshold = 5
    if "rope_pos" not in st.session_state:
        st.session_state.rope_pos = 0
    if "team_a_score" not in st.session_state:
        st.session_state.team_a_score = 0
    if "team_b_score" not in st.session_state:
        st.session_state.team_b_score = 0
    if "celebrated" not in st.session_state:
        st.session_state.celebrated = False
    if "prob_a" not in st.session_state:
        st.session_state.prob_a = MathEngine.generate(st.session_state.stream)
        st.session_state.start_a = time.time()
    if "prob_b" not in st.session_state:
        st.session_state.prob_b = MathEngine.generate(st.session_state.stream)
        st.session_state.start_b = time.time()
    if "logs" not in st.session_state:
        st.session_state.logs = []


def reset_match(new_stream: str) -> None:
    st.session_state.stream = new_stream
    st.session_state.rope_pos = 0
    st.session_state.team_a_score = 0
    st.session_state.team_b_score = 0
    st.session_state.celebrated = False
    st.session_state.prob_a = MathEngine.generate(new_stream)
    st.session_state.prob_b = MathEngine.generate(new_stream)
    st.session_state.start_a = time.time()
    st.session_state.start_b = time.time()


def handle_answer(team: str, selected: str) -> None:
    now = time.time()
    if team == "A":
        prob = st.session_state.prob_a
        elapsed = round(now - st.session_state.start_a, 2)
        is_correct = selected == prob.answer
        if is_correct:
            st.session_state.rope_pos -= 1
            st.session_state.team_a_score += 1
        st.session_state.prob_a = MathEngine.generate(st.session_state.stream)
        st.session_state.start_a = now
    else:
        prob = st.session_state.prob_b
        elapsed = round(now - st.session_state.start_b, 2)
        is_correct = selected == prob.answer
        if is_correct:
            st.session_state.rope_pos += 1
            st.session_state.team_b_score += 1
        st.session_state.prob_b = MathEngine.generate(st.session_state.stream)
        st.session_state.start_b = now

    if is_correct:
        st.toast(f"✅ Team {team}: Correct! (+1 Pull)", icon="🔥")
    else:
        st.toast(f"❌ Team {team}: Wrong! Correct: {prob.answer}", icon="⚠️")

    st.session_state.logs.append(
        {
            "Team": f"Team {team}",
            "Stream": st.session_state.stream,
            "Topic": prob.topic,
            "Question": prob.question,
            "Selected": selected,
            "Correct_Answer": prob.answer,
            "Is_Correct": is_correct,
            "Response_Time_Sec": elapsed,
        }
    )


init_session()
# --- TOP CONTROL BAR ---
ctrl_col1, ctrl_col2, ctrl_col3, ctrl_col4 = st.columns((4, 2, 1.5, 2))

with ctrl_col1:
    chosen_stream = st.selectbox(
        "Curriculum Stream",
        STREAMS,
        index=STREAMS.index(st.session_state.stream),
        label_visibility="collapsed",
    )
    if chosen_stream != st.session_state.stream:
        reset_match(chosen_stream)
        st.rerun()

with ctrl_col2:
    st.session_state.win_threshold = st.selectbox(
        "Win Pulls",
        WIN_OPTIONS,
        index=WIN_OPTIONS.index(st.session_state.win_threshold),
        format_func=lambda x: f"Target: {x} Pulls",
        label_visibility="collapsed",
    )

with ctrl_col3:
    if st.button("🔄 Reset", use_container_width=True):
        reset_match(st.session_state.stream)
        st.rerun()

with ctrl_col4:
    if st.session_state.logs:
        csv_data = pd.DataFrame(st.session_state.logs).to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 CSV Report",
            data=csv_data,
            file_name="tug_of_war_telemetry.csv",
            mime="text/csv",
            use_container_width=True,
        )
    else:
        st.button("📥 CSV (0)", disabled=True, use_container_width=True)

# --- DYNAMIC SVG TUG-OF-WAR ARENA ---
render_arena_svg(
    rope_pos=st.session_state.rope_pos,
    win_threshold=st.session_state.win_threshold,
    team_a_name=f"TEAM A ({st.session_state.team_a_score})",
    team_b_name=f"TEAM B ({st.session_state.team_b_score})",
)

# --- VICTORY CHECK WITH BALLOONS OR SPLIT-SCREEN GAMEPLAY ---
threshold = st.session_state.win_threshold
if st.session_state.rope_pos <= -threshold:
    if not st.session_state.celebrated:
        st.balloons()
        st.session_state.celebrated = True
    st.success("🏆 **TEAM A WINS THE TUG-OF-WAR!** Click **Reset** to play again.")
elif st.session_state.rope_pos >= threshold:
    if not st.session_state.celebrated:
        st.balloons()
        st.session_state.celebrated = True
    st.success("🏆 **TEAM B WINS THE TUG-OF-WAR!** Click **Reset** to play again.")
else:
    col_a, col_b = st.columns(2)

    # TEAM A PANEL
    with col_a:
        pa = st.session_state.prob_a
        st.markdown(
            f'<div class="question-box">🔵 {pa.question}</div>',
            unsafe_allow_html=True,
        )
        a_r1c1, a_r1c2 = st.columns(2)
        with a_r1c1:
            if st.button(pa.choices[0], key="a_opt_0", use_container_width=True):
                handle_answer("A", pa.choices[0])
                st.rerun()
        with a_r1c2:
            if st.button(pa.choices[1], key="a_opt_1", use_container_width=True):
                handle_answer("A", pa.choices[1])
                st.rerun()

        a_r2c1, a_r2c2 = st.columns(2)
        with a_r2c1:
            if st.button(pa.choices[2], key="a_opt_2", use_container_width=True):
                handle_answer("A", pa.choices[2])
                st.rerun()
        with a_r2c2:
            if st.button(pa.choices[3], key="a_opt_3", use_container_width=True):
                handle_answer("A", pa.choices[3])
                st.rerun()

    # TEAM B PANEL
    with col_b:
        pb = st.session_state.prob_b
        st.markdown(
            f'<div class="question-box">🟡 {pb.question}</div>',
            unsafe_allow_html=True,
        )
        b_r1c1, b_r1c2 = st.columns(2)
        with b_r1c1:
            if st.button(pb.choices[0], key="b_opt_0", use_container_width=True):
                handle_answer("B", pb.choices[0])
                st.rerun()
        with b_r1c2:
            if st.button(pb.choices[1], key="b_opt_1", use_container_width=True):
                handle_answer("B", pb.choices[1])
                st.rerun()

        b_r2c1, b_r2c2 = st.columns(2)
        with b_r2c1:
            if st.button(pb.choices[2], key="b_opt_2", use_container_width=True):
                handle_answer("B", pb.choices[2])
                st.rerun()
        with b_r2c2:
            if st.button(pb.choices[3], key="b_opt_3", use_container_width=True):
                handle_answer("B", pb.choices[3])
                st.rerun()

render_footer()
