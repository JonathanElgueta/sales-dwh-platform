# ==================================================
# COLORS
# ==================================================

PRIMARY_BG = "#0B1120"

SECONDARY_BG = "#1C1F26"

CARD_BG = "#1E293B"

SIDEBAR_BG = "#161B26"

BORDER_COLOR = "#334155"

TEXT_PRIMARY = "white"

TEXT_SECONDARY = "#94A3B8"

SUCCESS_COLOR = "#00FF99"

ERROR_COLOR = "#FF4B4B"

WARNING_COLOR = "#FACC15"

INFO_COLOR = "#38BDF8"

# ==================================================
# CHART THEME
# ==================================================

CHART_THEME = {

    "paper_bgcolor": PRIMARY_BG,

    "plot_bgcolor": SECONDARY_BG,

    "font": {

        "color": TEXT_PRIMARY

    }

}

# ==================================================
# KPI CARD STYLE
# ==================================================

KPI_CARD_STYLE = f"""

background: linear-gradient(
    145deg,
    {CARD_BG},
    #111827
);

padding: 28px;

border-radius: 18px;

border: 1px solid {BORDER_COLOR};

box-shadow:
    0px 10px 30px rgba(0,0,0,0.35);

min-height: 180px;

"""

# ==================================================
# SIDEBAR STYLE
# ==================================================

SIDEBAR_STYLE = f"""

background: linear-gradient(
    180deg,
    {SIDEBAR_BG} 0%,
    #0F172A 100%
);

border-right: 1px solid {BORDER_COLOR};

"""