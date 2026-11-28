import streamlit as st


def inject_kiosk_css() -> None:
    """Injects responsive dark-mode CSS for Mobile, Tablet, and Laptop/Smartboard."""
    st.markdown(
        """
        <style>
        /* --- BASE DARK THEME & RESET --- */
        .stApp {
            background-color: #0b0f19;
            color: #f8fafc;
        }
        header[data-testid="stHeader"], #MainMenu, footer {
            visibility: hidden;
            height: 0;
        }
        .block-container {
            padding-top: clamp(0.5rem, 1.5vh, 1.25rem) !important;
            padding-bottom: clamp(3.2rem, 6vh, 4.5rem) !important;
            padding-left: clamp(0.5rem, 2vw, 2rem) !important;
            padding-right: clamp(0.5rem, 2vw, 2rem) !important;
            max-width: 100% !important;
        }

        /* --- FORCE SIDE-BY-SIDE SPLIT SCREEN ON ALL DEVICES (MOBILE, TAB, LAPTOP) --- */
        [data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            gap: clamp(0.4rem, 1.5vw, 1.5rem) !important;
            align-items: stretch !important;
            width: 100% !important;
        }
        [data-testid="column"], [data-testid="stColumn"] {
            flex: 1 1 0% !important;
            min-width: 0 !important;
            width: auto !important;
        }

        /* --- RESPONSIVE QUESTION CARD --- */
        .question-box {
            background: linear-gradient(145deg, #131b2e, #1e293b);
            border: 1px solid #334155;
            border-radius: 12px;
            padding: clamp(0.6rem, 1.5vw, 1.25rem);
            text-align: center;
            font-size: clamp(0.95rem, 2.2vw, 1.75rem);
            font-weight: 700;
            color: #ffffff;
            margin-bottom: clamp(0.5rem, 1.2vh, 1rem);
            word-wrap: break-word;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.35);
        }

        /* --- RESPONSIVE TOUCH ANSWER BUTTONS --- */
        div.stButton > button {
            width: 100% !important;
            min-height: clamp(2.6rem, 6.5vh, 4.4rem) !important;
            font-size: clamp(0.85rem, 1.8vw, 1.45rem) !important;
            font-weight: 700 !important;
            border-radius: 10px !important;
            border: 1px solid #475569 !important;
            background-color: #1e293b !important;
            color: #f1f5f9 !important;
            padding: clamp(0.25rem, 0.8vw, 0.75rem) !important;
            transition: transform 0.1s ease, background-color 0.15s ease !important;
            white-space: normal !important;
            line-height: 1.2 !important;
        }
        div.stButton > button:hover {
            background-color: #334155 !important;
            border-color: #38bdf8 !important;
            color: #ffffff !important;
        }
        div.stButton > button:active {
            transform: scale(0.97) !important;
        }

        /* --- RESPONSIVE SVG ARENA CONTAINER --- */
        .arena-wrapper {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto clamp(0.4rem, 1vh, 0.9rem) auto;
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 14px;
            padding: clamp(0.25rem, 0.8vw, 0.6rem);
        }
        .arena-wrapper svg {
            width: 100%;
            height: auto;
            display: block;
            max-height: clamp(115px, 24vh, 230px);
        }

        /* --- MOBILE SPECIFIC (< 640px) --- */
        @media (max-width: 640px) {
            .stApp {
                overflow-y: auto !important;
            }
            .brand-footer {
                font-size: 0.68rem !important;
                padding: 4px 8px !important;
            }
        }

        /* --- TABLET SPECIFIC (641px - 1024px) --- */
        @media (min-width: 641px) and (max-width: 1024px) {
            div.stButton > button {
                min-height: 3.4rem !important;
                font-size: 1.1rem !important;
            }
        }

        /* --- LAPTOP / SMARTBOARD (> 1024px) --- */
        @media (min-width: 1025px) {
            .brand-footer {
                font-size: 0.85rem !important;
                padding: 7px 16px !important;
            }
        }

        /* --- FIXED BOTTOM BRANDING BAR --- */
        .brand-footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background: rgba(15, 23, 42, 0.95);
            border-top: 1px solid #1e293b;
            color: #94a3b8;
            text-align: center;
            z-index: 9999;
            backdrop-filter: blur(6px);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
def render_arena_svg(
    rope_pos: int = 0,
    win_threshold: int = 5,
    team_a_name: str = "TEAM ALPHA",
    team_b_name: str = "TEAM OMEGA",
) -> str:
    """Generates and renders a responsive 6-player SVG tug-of-war arena."""
    safe_threshold = max(1, win_threshold)
    clamped_pos = max(-safe_threshold, min(safe_threshold, rope_pos))
    # Map clamped rope position (-threshold to +threshold) to pixel shift (-150px to +150px)
    shift_x = int((clamped_pos / safe_threshold) * 150)
    center_x = 450 + shift_x

    svg_html = f"""
    <div class="arena-wrapper">
      <svg viewBox="0 0 900 210" xmlns="http://w3.org" preserveAspectRatio="xMidYMid meet">
        <!-- Ground & Center Victory Line -->
        <line x1="40" y1="175" x2="860" y2="175" stroke="#334155" stroke-width="4" stroke-linecap="round"/>
        <line x1="450" y1="35" x2="450" y2="185" stroke="#ef4444" stroke-width="3" stroke-dasharray="8,6"/>
        <text x="450" y="25" fill="#f87171" font-size="13" font-weight="bold" text-anchor="middle" font-family="sans-serif">
          VICTORY LINE
        </text>

        <!-- Team Labels -->
        <text x="140" y="30" fill="#38bdf8" font-size="16" font-weight="bold" text-anchor="middle" font-family="sans-serif">
          {team_a_name}
        </text>
        <text x="760" y="30" fill="#fbbf24" font-size="16" font-weight="bold" text-anchor="middle" font-family="sans-serif">
          {team_b_name}
        </text>

        <!-- Moving Rope & Players Group -->
        <g transform="translate({shift_x}, 0)">
          <!-- Main Tug Rope -->
          <line x1="150" y1="125" x2="750" y2="125" stroke="#d97706" stroke-width="7" stroke-linecap="round"/>
          <!-- Center Flag Marker -->
          <polygon points="450,125 440,152 460,152" fill="#ef4444"/>
          <circle cx="450" cy="125" r="7" fill="#ffffff" stroke="#ef4444" stroke-width="3"/>

          <!-- TEAM A (3 Leaning Players - Cyan) -->
          <g stroke="#38bdf8" stroke-width="5" stroke-linecap="round" fill="none">
            <!-- Player A1 -->
            <circle cx="210" cy="85" r="12" fill="#0ea5e9" stroke="none"/>
            <line x1="210" y1="97" x2="195" y2="138"/>
            <line x1="203" y1="112" x2="232" y2="125"/>
            <line x1="195" y1="138" x2="180" y2="173"/>
            <line x1="195" y1="138" x2="215" y2="173"/>

            <!-- Player A2 -->
            <circle cx="275" cy="85" r="12" fill="#0ea5e9" stroke="none"/>
            <line x1="275" y1="97" x2="260" y2="138"/>
            <line x1="268" y1="112" x2="297" y2="125"/>
            <line x1="260" y1="138" x2="245" y2="173"/>
            <line x1="260" y1="138" x2="280" y2="173"/>

            <!-- Player A3 -->
            <circle cx="340" cy="85" r="12" fill="#0ea5e9" stroke="none"/>
            <line x1="340" y1="97" x2="325" y2="138"/>
            <line x1="333" y1="112" x2="362" y2="125"/>
            <line x1="325" y1="138" x2="310" y2="173"/>
            <line x1="325" y1="138" x2="345" y2="173"/>
          </g>

          <!-- TEAM B (3 Leaning Players - Amber) -->
          <g stroke="#fbbf24" stroke-width="5" stroke-linecap="round" fill="none">
            <!-- Player B1 -->
            <circle cx="560" cy="85" r="12" fill="#f59e0b" stroke="none"/>
            <line x1="560" y1="97" x2="575" y2="138"/>
            <line x1="567" y1="112" x2="538" y2="125"/>
            <line x1="575" y1="138" x2="555" y2="173"/>
            <line x1="575" y1="138" x2="590" y2="173"/>

            <!-- Player B2 -->
            <circle cx="625" cy="85" r="12" fill="#f59e0b" stroke="none"/>
            <line x1="625" y1="97" x2="640" y2="138"/>
            <line x1="632" y1="112" x2="603" y2="125"/>
            <line x1="640" y1="138" x2="620" y2="173"/>
            <line x1="640" y1="138" x2="655" y2="173"/>

            <!-- Player B3 -->
            <circle cx="690" cy="85" r="12" fill="#f59e0b" stroke="none"/>
            <line x1="690" y1="97" x2="705" y2="138"/>
            <line x1="697" y1="112" x2="668" y2="125"/>
            <line x1="705" y1="138" x2="685" y2="173"/>
            <line x1="705" y1="138" x2="720" y2="173"/>
          </g>
        </g>
      </svg>
    </div>
    """
    st.markdown(svg_html, unsafe_allow_html=True)
    return svg_html


def render_footer() -> None:
    """Renders the fixed responsive bottom branding bar."""
    st.markdown(
        """
        <div class="brand-footer">
            🪢 <strong>Tug-of-War Maths &amp; Engineering Arena</strong> • Built by <strong>T A Srinivas (Srinivasta)</strong> • Tanakala AI Solutions
        </div>
        """,
        unsafe_allow_html=True,
    )
# Backward-compatible aliases for app.py and tests/test_engine.py
inject_smartboard_css = inject_kiosk_css
render_arena = render_arena_svg
