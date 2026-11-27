import streamlit as st
import streamlit.components.v1 as components


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


def _draw_player(x: float, color: str, facing_left: bool) -> str:
    lean = -14 if facing_left else 14
    arm_x = x + 16 if facing_left else x - 16
    return f"""
    <g transform="rotate({lean} {x} 85)">
        <circle cx="{x}" cy="36" r="10" fill="{color}" />
        <line x1="{x}" y1="46" x2="{x}" y2="74" stroke="{color}" stroke-width="6" stroke-linecap="round" />
        <line x1="{x}" y1="54" x2="{arm_x}" y2="62" stroke="{color}" stroke-width="5" stroke-linecap="round" />
        <line x1="{x}" y1="74" x2="{x - 10}" y2="96" stroke="{color}" stroke-width="5" stroke-linecap="round" />
        <line x1="{x}" y1="74" x2="{x + 12}" y2="96" stroke="{color}" stroke-width="5" stroke-linecap="round" />
    </g>
    """


def render_arena(rope_pos: int, win_limit: int, team_a: str, team_b: str):
    clamped_pos = max(-win_limit, min(win_limit, rope_pos))
    center_x = 450 + (clamped_pos / win_limit) * 180

    team_a_offsets = [-95, -145, -195]
    team_b_offsets =

    players_svg = ""
    for offset in team_a_offsets:
        players_svg += _draw_player(center_x + offset, "#2563eb", facing_left=True)
    for offset in team_b_offsets:
        players_svg += _draw_player(center_x + offset, "#ea580c", facing_left=False)

    rope_start = center_x - 215
    rope_end = center_x + 215

    full_html = f"""
    <div style="font-family: sans-serif; width:100%; box-sizing:border-box; background:#f8fafc; border-radius:16px; padding:16px; border:2px solid #e2e8f0;">
        <div style="display:flex; justify-content:space-between; font-weight:800; font-size:20px; margin-bottom:6px;">
            <span style="color:#2563eb;">⬅️ {team_a} (3 Players)</span>
            <span style="color:#64748b;">🏁 CENTER / VICTORY LINE</span>
            <span style="color:#ea580c;">(3 Players) {team_b} ➡️</span>
        </div>
        <svg viewBox="0 0 900 115" style="width:100%; height:120px; display:block;">
            <rect x="10" y="12" width="140" height="90" rx="10" fill="#dbeafe" />
            <text x="80" y="30" text-anchor="middle" fill="#1d4ed8" font-size="12" font-weight="bold">TEAM A WIN ZONE</text>
            <rect x="750" y="12" width="140" height="90" rx="10" fill="#ffedd5" />
            <text x="820" y="30" text-anchor="middle" fill="#c2410c" font-size="12" font-weight="bold">TEAM B WIN ZONE</text>
            <line x1="10" y1="98" x2="890" y2="98" stroke="#cbd5e1" stroke-width="3" />
            <line x1="450" y1="8" x2="450" y2="105" stroke="#94a3b8" stroke-width="4" stroke-dasharray="8,6" />
            <line x1="{rope_start}" y1="62" x2="{rope_end}" y2="62" stroke="#92400e" stroke-width="8" stroke-linecap="round" />
            {players_svg}
            <polygon points="{center_x},62 {center_x + 20},46 {center_x},36" fill="#dc2626" />
            <circle cx="{center_x}" cy="62" r="8" fill="#dc2626" />
        </svg>
    </div>
    """
    components.html(full_html, height=195)
