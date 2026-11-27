import time
import pandas as pd
import streamlit as st
from src.engine import MathEngine
from src.ui_components import inject_smartboard_css, render_arena

st.set_page_config(
    page_title="Tug-of-War Maths Enterprise", page_icon="🪢", layout="wide"
)
inject_smartboard_css()

GRADE_OPTIONS = [
    "Class 1 (Add & Subtract ≤ 10)",
    "Class 2-3 (Two-Digit & Intro Mult)",
    "Class 4-5 (Multiplication & Division)",
    "Class 6-7 (Fractions & Percentages)",
    "Class 8 (Linear Equations)",
]

if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.rope_pos = 0
    st.session_state.win_limit = 5
    st.session_state.team_a_name = "Blue Tigers"
    st.session_state.team_b_name = "Orange Lions"
    st.session_state.grade = GRADE_OPTIONS
    st.session_state.prob_a = MathEngine.generate(st.session_state.grade)
    st.session_state.prob_b = MathEngine.generate(st.session_state.grade)
    st.session_state.logs = []
    st.session_state.q_start_a = time.time()
    st.session_state.q_start_b = time.time()

with st.sidebar:
    st.header("🏫 Classroom Controls")
    st.session_state.team_a_name = st.text_input(
        "Team A Name", st.session_state.team_a_name
    )
    st.session_state.team_b_name = st.text_input(
        "Team B Name", st.session_state.team_b_name
    )

    selected_grade = st.selectbox("Select Class / Level", GRADE_OPTIONS)
    st.session_state.win_limit = st.slider("Pulls to Win", 3, 10, 5)

    if selected_grade != st.session_state.grade:
        st.session_state.grade = selected_grade
        st.session_state.prob_a = MathEngine.generate(selected_grade)
        st.session_state.prob_b = MathEngine.generate(selected_grade)
        st.rerun()

    if st.button("🔄 Start New Round", use_container_width=True, type="primary"):
        st.session_state.rope_pos = 0
        st.session_state.prob_a = MathEngine.generate(st.session_state.grade)
        st.session_state.prob_b = MathEngine.generate(st.session_state.grade)
        st.rerun()

    st.divider()
    if st.session_state.logs:
        df_logs = pd.DataFrame(st.session_state.logs)
        st.download_button(
            "📊 Export Session Report (CSV)",
            df_logs.to_csv(index=False).encode("utf-8"),
            "classroom_maths_analytics.csv",
            "text/csv",
            use_container_width=True,
        )

render_arena(
    st.session_state.rope_pos,
    st.session_state.win_limit,
    st.session_state.team_a_name,
    st.session_state.team_b_name,
)

if abs(st.session_state.rope_pos) >= st.session_state.win_limit:
    winner = (
        st.session_state.team_a_name
        if st.session_state.rope_pos < 0
        else st.session_state.team_b_name
    )
    st.balloons()
    st.success(f"🏆 **{winner.upper()} WINS!** Click 'Start New Round' in the sidebar.")
    st.stop()


def handle_answer(team: str, chosen: str, problem, start_time: float):
    elapsed = round(time.time() - start_time, 2)
    is_correct = chosen == problem.answer
    st.session_state.logs.append({
        "Team": team,
        "Topic": problem.topic,
        "Question": problem.question,
        "Chosen": chosen,
        "Correct": is_correct,
        "Response_Time_Sec": elapsed,
        "Class": st.session_state.grade,
    })
    if is_correct:
        st.session_state.rope_pos += (
            -1 if team == st.session_state.team_a_name else 1
        )
        if team == st.session_state.team_a_name:
            st.session_state.prob_a = MathEngine.generate(
                st.session_state.grade
            )
            st.session_state.q_start_a = time.time()
        else:
            st.session_state.prob_b = MathEngine.generate(
                st.session_state.grade
            )
            st.session_state.q_start_b = time.time()
    else:
        st.toast(f"❌ {team}: Try again!", icon="⚠️")


col1, col_sep, col2 = st.columns([5, 0.5, 5])

with col1:
    st.markdown(f"### 🔵 {st.session_state.team_a_name}")
    st.markdown(f"## `{st.session_state.prob_a.question}`")
    btn_cols_a = st.columns(2)
    for idx, val in enumerate(st.session_state.prob_a.choices):
        if btn_cols_a[idx % 2].button(
            val, key=f"a_{idx}", use_container_width=True
        ):
            handle_answer(
                st.session_state.team_a_name,
                val,
                st.session_state.prob_a,
                st.session_state.q_start_a,
            )
            st.rerun()

with col2:
    st.markdown(f"### 🟠 {st.session_state.team_b_name}")
    st.markdown(f"## `{st.session_state.prob_b.question}`")
    btn_cols_b = st.columns(2)
    for idx, val in enumerate(st.session_state.prob_b.choices):
        if btn_cols_b[idx % 2].button(
            val, key=f"b_{idx}", use_container_width=True
        ):
            handle_answer(
                st.session_state.team_b_name,
                val,
                st.session_state.prob_b,
                st.session_state.q_start_b,
            )
            st.rerun()
