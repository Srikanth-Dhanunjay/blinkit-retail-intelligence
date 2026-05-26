import streamlit as st
import pandas as pd
import plotly.express as px

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Blinkit Executive Intelligence",
    page_icon="🛒",
    layout="wide"
)

# 2. LIGHT-THEME MAIN / DARK-THEME SIDEBAR CSS INJECTION
st.markdown("""
<style>
    /* Premium white cards with a very soft, modern drop-shadow */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        padding: 22px 28px;
        border-radius: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03), 0 0 0 1px rgba(0, 0, 0, 0.05);
        border: None;
        transition: all 0.2s ease-in-out;
    }
    /* Smooth hover lift and border accent */
    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.04);
    }
    /* Style the metrics labels for professional contrast */
    div[data-testid="stMetricLabel"] {
        color: #475569 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }
    /* Style the metric values */
    div[data-testid="stMetricValue"] {
        color: #0F172A !important;
        font-weight: 700 !important;
    }
    
    /* TARGETING THE DARK SIDEBAR TEXT READABILITY */
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] label {
        color: #E2E8F0 !important; /* Soft white/light gray text for filters and descriptions */
    }
    
    /* RE-ASSERT SIGNATURE ORANGE FOR THE HEADER (Enforcing Higher Specificity) */
    section[data-testid="stSidebar"] p.sidebar-header {
        font-size: 25px !important;
        font-weight: 700 !important;
        color: #F07030 !important; /* Forces your customized orange to stay locked in */
        margin-bottom: 2px;
    }

    
    /* Target all inner child elements (svg, paths, spans, text strings) */
    div[data-testid="collapsedControl"] *,
    button[data-testid="stSidebarCollapseButton"] *,
    button[aria-label="Close sidebar"] *,
    button[aria-label="Open sidebar"] *,
    button[data-testid="stBaseButton-headerNoPadding"] *,
    header[data-testid="stHeader"] button * {
        color: #F07030 !important;
    }
    
    /* Smooth interactive hover background glow */
    header[data-testid="stHeader"] button:hover,
    button[data-testid="stSidebarCollapseButton"]:hover,
    div[data-testid="collapsedControl"]:hover {
        background-color: rgba(240, 112, 48, 0.1) !important; 
        border-radius: 50%;
    }
</style>
""", unsafe_allow_html=True)

# 3. HIGH-PERFORMANCE DATA LOADING (CACHED)
@st.cache_data
def load_processed_data():
    return pd.read_csv("data/blinkit_processed.csv")

df = load_processed_data()

# 4. SIDEBAR NAVIGATION & CONTROL PANEL
st.sidebar.markdown('<p class="sidebar-header">Control Panel Filters</p>', unsafe_allow_html=True)
st.sidebar.markdown("Segment distribution views and financial performance aggregates live.")
st.sidebar.markdown("---")

selected_tiers = st.sidebar.multiselect(
    label="Filter by Location Tier:",
    options=list(df["Outlet Location Type"].unique()),
    default=list(df["Outlet Location Type"].unique())
)

selected_types = st.sidebar.multiselect(
    label="Filter by Outlet Operational Type:",
    options=list(df["Outlet Type"].unique()),
    default=list(df["Outlet Type"].unique())
)

# Apply runtime logical evaluations to filter rows safely
filtered_df = df[
    (df["Outlet Location Type"].isin(selected_tiers)) & 
    (df["Outlet Type"].isin(selected_types))
]

# -----------------------------------------------------------------------------
# MAIN DASHBOARD INTERFACE LAYOUT
# -----------------------------------------------------------------------------

st.title("Blinkit Retail Intelligence & Profit Simulator")
st.markdown("Monitor high-level operational health indicators and run simulated retail forecasting scenarios.")
st.markdown("---")

if filtered_df.empty:
    st.warning("⚠️ Warning: No records match your selected filter criteria. Please re-select locations or operational types in the sidebar control panel.")
else:
    # 5. FINANCIAL METRICS COMPONENT LAYER (LIGHT CARD DESIGN)
    total_sales = filtered_df["Sales"].sum()
    total_cost = filtered_df["Estimated_Cost"].sum()
    baseline_profit = filtered_df["Baseline_Profit"].sum()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="TOTAL REVENUE GENERATED", value=f"${total_sales:,.2f}")
    with col2:
        st.metric(label="WHOLESALE PROCUREMENT COST", value=f"${total_cost:,.2f}")
    with col3:
        st.metric(label="BASELINE NET PROFIT (30%)", value=f"${baseline_profit:,.2f}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 6. INTERACTIVE DATA VISUALIZATION LAYER
    st.subheader("Deep-Dive Departmental & Operational Analysis")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        category_sales = filtered_df.groupby("Item Type")["Sales"].sum().reset_index()
        category_sales = category_sales.sort_values(by="Sales", ascending=True)
        
        # Using a sophisticated corporate blue gradient for the bar chart
        fig_bars = px.bar(
            category_sales,
            x="Sales",
            y="Item Type",
            orientation="h",
            title="Revenue Distribution Across Product Categories",
            labels={"Sales": "Total Revenue ($)", "Item Type": "Department"},
            color="Sales",
            color_continuous_scale="Blugrn"
        )
        fig_bars.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", 
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#1E293B",
            height=520
        )
        st.plotly_chart(fig_bars, use_container_width=True)

    with chart_col2:
        size_distribution = filtered_df.groupby("Outlet Size")["Sales"].sum().reset_index()
        
        # Using a crisp, explicit discrete palette so sizes stand out clearly
        fig_pie = px.pie(
            size_distribution,
            values="Sales",
            names="Outlet Size",
            title="Revenue Contribution by Store Footprint Size",
            hole=0.4,
            color_discrete_sequence=["#0D6EFD", "#10B981", "#F59E0B"]  # Corporate Blue, Emerald Green, Warm Amber
        )
        fig_pie.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#1E293B",
            height=520
        )
        st.plotly_chart(fig_pie, use_container_width=True)