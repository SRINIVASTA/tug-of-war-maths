import streamlit as st
import streamlit.components.v1 as components


def inject_smartboard_css():
    st.markdown(
        """
        <style>
        /* Hide Share, Star, Edit, GitHub icon, and Three-Dots Menu */
        [data-testid="stToolbar"] {
            visibility: hidden !important;
            display: none !important;
        }
        [data-testid="stDecoration"] {
            display: none !important;
        }
        #MainMenu {
            visibility: hidden !important;
            display: none !important;
        }
        footer {
            visibility: hidden !important;
            display: none !important;
        }
        header[data-testid="stHeader"] {
            background: transparent !important;
        }

        /* Hide Streamlit Cloud "Manage app" & Viewer Badges */
        [data-testid="manage-app-button"],
        .stAppDeployButton,
        div[class*="viewerBadge"],
        button[title="Manage app"] {
            visibility: hidden !important;
            display: none !important;
        }

        /* Keep sidebar open/close arrow visible for teachers */
        [data-testid="stSidebarCollapsedControl"] {
            visibility: visible !important;
            display: flex !important;
        }

        /* Large Smartboard Answer Buttons */
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
    team_b_offsets = [95, 145, 195]

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

def render_footer():
    footer_html = """
    <div style="margin-top: 40px; padding: 16px 0; border-top: 2px solid #e2e8f0; text-align: center; font-family: sans-serif;">
        <p style="color: #64748b; font-size: 0.95rem; margin-bottom: 10px; font-weight: 600;">
            Built by T A Srinivas • Connect & Explore More Projects
        </p>
        <div style="display: flex; justify-content: center; gap: 24px; align-items: center;">
            <a href="https://www.linkedin.com/in/srinivas-t-a-557637119/" target="_blank" title="LinkedIn Profile" style="text-decoration: none; color: #0a66c2; display: inline-flex; align-items: center; gap: 6px; font-weight: 700; font-size: 1rem;">
                <svg xmlns="http://w3.org" width="22" height="22" viewBox="0 0 24 24" fill="#0a66c2">
                    <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
                </svg>
                LinkedIn
            </a>
            <a href="mailto:tasrinivass@gmail.com" title="Send Email" style="text-decoration: none; color: #dc2626; display: inline-flex; align-items: center; gap: 6px; font-weight: 700; font-size: 1rem;">
                <svg xmlns="http://w3.org" width="22" height="22" viewBox="0 0 24 24" fill="#dc2626">
                    <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/>
                </svg>
                Email
            </a>
            <a href="https://srinivasta.github.io/" target="_blank" title="Portfolio Website" style="text-decoration: none; color: #2563eb; display: inline-flex; align-items: center; gap: 6px; font-weight: 700; font-size: 1rem;">
                <svg xmlns="http://w3.org" width="22" height="22" viewBox="0 0 24 24" fill="#2563eb">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
                </svg>
                Website
            </a>
        </div>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
