import streamlit as st


def inject_smartboard_css():
    st.markdown(
        """
        <style>
        div.stButton > button {
            height: 85px;
            font-size: 2.2rem !important;
            font-weight: 800 !important;
            border-radius: 14px !important;
            border: 2px solid #cbd5e1 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_arena(rope_pos: int, win_limit: int, team_a: str, team_b: str):
    percent = 50 + (rope_pos / win_limit) * 35

    svg_html = f"""
    <div style="width:100%; background:#f8fafc; border-radius:16px; padding:20px; border:2px solid #e2e8f0; margin-bottom:20px;">
        <div style="display:flex; justify-content:space-between; font-weight:800; font-size:1.5rem; margin-bottom:10px;">
            <span style="color:#2563eb;">⬅️ {team_a}</span>
            <span style="color:#64748b;">VICTORY LINE</span>
            <span style="color:#ea580c;">{team_b} ➡️</span>
        </div>
        <svg viewBox="0 0 800 100" style="width:100%; height:95px;">
            <rect x="0" y="10" width="120" height="80" rx="10" fill="#dbeafe" />
            <rect x="680" y="10" width="120" height="80" rx="10" fill="#ffedd5" />
            <line x1="400" y1="5" x2="400" y2="95" stroke="#94a3b8" stroke-width="4" stroke-dasharray="8,6" />
            <line x1="{percent*8 - 220}" y1="50" x2="{percent*8 + 220}" y2="50" stroke="#b45309" stroke-width="10" stroke-linecap="round" />
            <circle cx="{percent*8 - 220}" cy="50" r="18" fill="#2563eb" />
            <circle cx="{percent*8 + 220}" cy="50" r="18" fill="#ea580c" />
            <polygon points="{percent*8},50 {percent*8 + 22},32 {percent*8},20" fill="#dc2626" />
            <circle cx="{percent*8}" cy="50" r="10" fill="#dc2626" />
        </svg>
    </div>
    """
    st.markdown(svg_html, unsafe_allow_html=True)
