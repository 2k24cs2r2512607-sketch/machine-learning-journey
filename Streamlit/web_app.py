import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    layout="wide",
    page_title="Startup Funding Analysis",
    page_icon="📊"
)

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    data = pd.read_csv("D:\Machine_Learning_Journey\Streamlit\cleaned.csv")

    data["date"] = pd.to_datetime(
        data["date"],
        errors="coerce"
    )

    data["year"] = data["date"].dt.year
    data["month"] = data["date"].dt.month

    # Clean important text columns
    for col in ["startup", "vertical", "city", "round", "investors"]:
        if col in data.columns:
            data[col] = data[col].fillna("Unknown").astype(str).str.strip()

    data["amount"] = pd.to_numeric(
        data["amount"],
        errors="coerce"
    ).fillna(0)

    return data


df = load_data()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_amount(value):
    return f"{value:,.0f} Cr"


def plot_barh(series, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(10, 5))

    series.sort_values().plot(
        kind="barh",
        ax=ax
    )

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)


# ============================================================
# OVERALL ANALYSIS
# ============================================================

def overall_analysis():

    st.title("Overall Startup Funding Analysis")

    # --------------------------------------------------------
    # FILTERS
    # --------------------------------------------------------

    st.subheader("Filters")

    col1, col2, col3, col4 = st.columns(4)

    years = sorted(
        df["year"].dropna().unique().tolist()
    )

    cities = sorted(
        df["city"].dropna().unique().tolist()
    )

    verticals = sorted(
        df["vertical"].dropna().unique().tolist()
    )

    rounds = sorted(
        df["round"].dropna().unique().tolist()
    )

    with col1:
        selected_year = st.selectbox(
            "Year",
            ["All"] + years
        )

    with col2:
        selected_city = st.selectbox(
            "City",
            ["All"] + cities
        )

    with col3:
        selected_vertical = st.selectbox(
            "Sector",
            ["All"] + verticals
        )

    with col4:
        selected_round = st.selectbox(
            "Funding Round",
            ["All"] + rounds
        )

    filtered_df = df.copy()

    if selected_year != "All":
        filtered_df = filtered_df[
            filtered_df["year"] == selected_year
        ]

    if selected_city != "All":
        filtered_df = filtered_df[
            filtered_df["city"] == selected_city
        ]

    if selected_vertical != "All":
        filtered_df = filtered_df[
            filtered_df["vertical"] == selected_vertical
        ]

    if selected_round != "All":
        filtered_df = filtered_df[
            filtered_df["round"] == selected_round
        ]

    st.caption(
        f"Showing {len(filtered_df):,} funding records"
    )

    # --------------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------------

    total_funding = filtered_df["amount"].sum()

    average_funding = (
        filtered_df["amount"].mean()
        if len(filtered_df) > 0
        else 0
    )

    funded_startups = filtered_df["startup"].nunique()

    funding_rounds = len(filtered_df)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Funding",
            format_amount(total_funding)
        )

    with col2:
        st.metric(
            "Average Funding",
            format_amount(average_funding)
        )

    with col3:
        st.metric(
            "Funded Startups",
            funded_startups
        )

    with col4:
        st.metric(
            "Funding Records",
            funding_rounds
        )

    st.divider()

    # --------------------------------------------------------
    # YEAR-WISE FUNDING TREND
    # --------------------------------------------------------

    st.header("Year-wise Funding Trend")

    year_funding = (
        filtered_df
        .groupby("year")["amount"]
        .sum()
        .sort_index()
    )

    if not year_funding.empty:

        fig, ax = plt.subplots(figsize=(12, 4))

        ax.plot(
            year_funding.index,
            year_funding.values,
            marker="o"
        )

        ax.set_xlabel("Year")
        ax.set_ylabel("Funding (Cr)")
        ax.grid(
            axis="y",
            linestyle="--",
            alpha=0.3
        )

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    # --------------------------------------------------------
    # MONTH-ON-MONTH ANALYSIS
    # --------------------------------------------------------

    st.header("Month-on-Month Analysis")

    analysis_type = st.selectbox(
        "Select Metric",
        ["Total Funding", "Number of Funding Records"]
    )

    if analysis_type == "Total Funding":

        temp_df = (
            filtered_df
            .groupby(["year", "month"])["amount"]
            .sum()
            .reset_index()
        )

        y_column = "amount"

    else:

        temp_df = (
            filtered_df
            .groupby(["year", "month"])["startup"]
            .count()
            .reset_index()
        )

        y_column = "startup"

    if not temp_df.empty:

        temp_df["x_axis"] = (
            temp_df["month"].astype(int).astype(str)
            + "-"
            + temp_df["year"].astype(int).astype(str)
        )

        fig, ax = plt.subplots(figsize=(12, 4))

        ax.plot(
            temp_df["x_axis"],
            temp_df[y_column],
            marker="o"
        )

        ax.set_xlabel("Month-Year")
        ax.set_ylabel(analysis_type)
        plt.xticks(rotation=45)

        ax.grid(
            axis="y",
            linestyle="--",
            alpha=0.3
        )

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    # --------------------------------------------------------
    # TOP STARTUPS
    # --------------------------------------------------------

    st.header("Top 10 Startups by Funding")

    top_startups = (
        filtered_df
        .groupby("startup")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    if not top_startups.empty:
        plot_barh(
            top_startups,
            "Total Funding (Cr)",
            "Startup"
        )

    # --------------------------------------------------------
    # TOP SECTORS
    # --------------------------------------------------------

    st.header("Top 5 Sectors")

    top_sectors = (
        filtered_df
        .groupby("vertical")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    if not top_sectors.empty:
        plot_barh(
            top_sectors,
            "Total Funding (Cr)",
            "Sector"
        )

    # --------------------------------------------------------
    # CITY ANALYSIS
    # --------------------------------------------------------

    st.header("Top 10 Cities by Funding")

    city_funding = (
        filtered_df
        .groupby("city")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    if not city_funding.empty:
        plot_barh(
            city_funding,
            "Total Funding (Cr)",
            "City"
        )

    # --------------------------------------------------------
    # FUNDING HEATMAP
    # --------------------------------------------------------

    st.header("Funding Heatmap")

    heatmap_data = filtered_df.pivot_table(
        index="year",
        columns="vertical",
        values="amount",
        aggfunc="sum",
        fill_value=0
    )

    if not heatmap_data.empty:

        fig, ax = plt.subplots(
            figsize=(14, 6)
        )

        sns.heatmap(
            heatmap_data,
            annot=True,
            fmt=".0f",
            ax=ax
        )

        ax.set_xlabel("Sector")
        ax.set_ylabel("Year")

        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

    # --------------------------------------------------------
    # YEAR-WISE TOP STARTUP
    # --------------------------------------------------------

    st.header("Top Startup by Funding — Year Wise")

    start = (
        filtered_df
        .groupby(["year", "startup"])["amount"]
        .agg(Total_Funding="sum")
        .reset_index()
    )

    if not start.empty:

        year_wise_analysis = start.loc[
            start.groupby("year")["Total_Funding"].idxmax()
        ].reset_index(drop=True)

        st.dataframe(
            year_wise_analysis,
            use_container_width=True,
            hide_index=True
        )

    # --------------------------------------------------------
    # DOWNLOAD FILTERED DATA
    # --------------------------------------------------------

    st.divider()

    st.subheader("Download Data")

    csv = filtered_df.to_csv(index=False)

    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name="startup_funding_filtered.csv",
        mime="text/csv"
    )


# ============================================================
# STARTUP ANALYSIS
# ============================================================

def load_startup_details(startup):

    startup_df = df[
        df["startup"] == startup
    ].copy()

    st.title(startup)

    if startup_df.empty:
        st.warning("No data found for this startup.")
        return

    # --------------------------------------------------------
    # KPI
    # --------------------------------------------------------

    total_funding = startup_df["amount"].sum()
    funding_records = len(startup_df)
    investors = startup_df["investors"].nunique()
    sectors = startup_df["vertical"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Funding",
            format_amount(total_funding)
        )

    with col2:
        st.metric(
            "Funding Records",
            funding_records
        )

    with col3:
        st.metric(
            "Investors",
            investors
        )

    with col4:
        st.metric(
            "Sectors",
            sectors
        )

    st.divider()

    # --------------------------------------------------------
    # FUNDING HISTORY
    # --------------------------------------------------------

    st.subheader("Funding History")

    funding_history = (
        startup_df
        .groupby("year")["amount"]
        .sum()
        .sort_index()
    )

    if not funding_history.empty:

        fig, ax = plt.subplots(figsize=(10, 4))

        ax.plot(
            funding_history.index,
            funding_history.values,
            marker="o"
        )

        ax.set_xlabel("Year")
        ax.set_ylabel("Funding (Cr)")
        ax.grid(
            axis="y",
            linestyle="--",
            alpha=0.3
        )

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    # --------------------------------------------------------
    # TWO COLUMNS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Investors")

        investor_data = (
            startup_df["investors"]
            .dropna()
            .str.split(",")
            .explode()
            .str.strip()
            .value_counts()
            .head(10)
        )

        st.dataframe(
            investor_data.rename("Investment Records"),
            use_container_width=True,
            hide_index=True
        )

    with col2:

        st.subheader("Funding Rounds")

        round_data = (
            startup_df
            .groupby("round")["amount"]
            .sum()
            .sort_values(ascending=False)
        )

        if not round_data.empty:
            plot_barh(
                round_data,
                "Funding (Cr)",
                "Round"
            )

    # --------------------------------------------------------
    # FUNDING RECORDS
    # --------------------------------------------------------

    st.subheader("Funding Records")

    display_columns = [
        "date",
        "startup",
        "vertical",
        "city",
        "round",
        "amount",
        "investors"
    ]

    display_columns = [
        col for col in display_columns
        if col in startup_df.columns
    ]

    st.dataframe(
        startup_df
        .sort_values("date", ascending=False)[display_columns],
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# INVESTOR ANALYSIS
# ============================================================

def load_investor_details(investor):

    investor_df = df[
        df["investors"].str.contains(
            investor,
            na=False,
            regex=False
        )
    ].copy()

    st.title(investor)

    if investor_df.empty:
        st.warning("No investment data found.")
        return

    # --------------------------------------------------------
    # KPI
    # --------------------------------------------------------

    total_investment = investor_df["amount"].sum()
    startups = investor_df["startup"].nunique()
    investment_records = len(investor_df)
    sectors = investor_df["vertical"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Investment",
            format_amount(total_investment)
        )

    with col2:
        st.metric(
            "Startups",
            startups
        )

    with col3:
        st.metric(
            "Investments",
            investment_records
        )

    with col4:
        st.metric(
            "Sectors",
            sectors
        )

    st.divider()

    # --------------------------------------------------------
    # RECENT 5 INVESTMENTS
    # --------------------------------------------------------

    st.subheader("Most Recent Investments")

    last5_df = (
        investor_df
        .sort_values("date", ascending=False)
        .head(5)
    )

    recent_columns = [
        "date",
        "startup",
        "vertical",
        "city",
        "round",
        "amount"
    ]

    recent_columns = [
        col for col in recent_columns
        if col in last5_df.columns
    ]

    st.dataframe(
        last5_df[recent_columns],
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------------
    # BIGGEST INVESTMENTS
    # --------------------------------------------------------

    st.subheader("Biggest Investments")

    big_series = (
        investor_df
        .groupby("startup")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    if not big_series.empty:
        plot_barh(
            big_series,
            "Investment Amount (Cr)",
            "Startup"
        )

    # --------------------------------------------------------
    # SECTOR / ROUND
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    vertical_series = (
        investor_df
        .groupby("vertical")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    round_series = (
        investor_df
        .groupby("round")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    with col1:

        st.subheader("Sectors Invested In")

        if not vertical_series.empty:

            fig, ax = plt.subplots(
                figsize=(6, 5)
            )

            ax.pie(
                vertical_series,
                labels=vertical_series.index,
                autopct="%0.1f%%",
                startangle=90,
                wedgeprops=dict(width=0.45)
            )

            ax.set_title("Investment by Sector")

            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)

    with col2:

        st.subheader("Rounds Invested In")

        if not round_series.empty:

            fig, ax = plt.subplots(
                figsize=(6, 5)
            )

            ax.pie(
                round_series,
                labels=round_series.index,
                autopct="%0.1f%%",
                startangle=90,
                wedgeprops=dict(width=0.45)
            )

            ax.set_title("Investment by Round")

            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)

    # --------------------------------------------------------
    # CITIES
    # --------------------------------------------------------

    st.subheader("Cities Invested In")

    city_series = (
        investor_df
        .groupby("city")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    if not city_series.empty:
        plot_barh(
            city_series,
            "Investment Amount (Cr)",
            "City"
        )

    # --------------------------------------------------------
    # YOY INVESTMENT
    # --------------------------------------------------------

    st.subheader("YOY Investment")

    year_series = (
        investor_df
        .groupby("year")["amount"]
        .sum()
        .sort_index()
    )

    if not year_series.empty:

        fig, ax = plt.subplots(figsize=(10, 4))

        ax.plot(
            year_series.index,
            year_series.values,
            marker="o"
        )

        ax.set_xlabel("Year")
        ax.set_ylabel("Investment (Cr)")
        ax.grid(
            axis="y",
            linestyle="--",
            alpha=0.3
        )

        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📊 Startup Funding Analysis")

st.sidebar.caption(
    "Explore startup funding, sectors, cities and investors."
)

option = st.sidebar.selectbox(
    "Select Analysis",
    [
        "Overall Analysis",
        "Startup",
        "Investor"
    ]
)

st.sidebar.divider()


# ============================================================
# OVERALL
# ============================================================

if option == "Overall Analysis":

    overall_analysis()


# ============================================================
# STARTUP
# ============================================================

elif option == "Startup":

    st.sidebar.subheader("Startup Selection")

    selected_startup = st.sidebar.selectbox(
        "Select Startup",
        sorted(
            df["startup"]
            .dropna()
            .unique()
            .tolist()
        )
    )

    btn1 = st.sidebar.button(
        "Find Startup Details"
    )

    if btn1:
        load_startup_details(
            selected_startup
        )

    else:
        st.title("Startup Analysis")
        st.info(
            "Select a startup from the sidebar "
            "and click 'Find Startup Details'."
        )


# ============================================================
# INVESTOR
# ============================================================

else:

    st.sidebar.subheader("Investor Selection")

    investor_list = (
        df["investors"]
        .dropna()
        .str.split(",")
        .explode()
        .str.strip()
    )

    investor_list = sorted(
        investor_list[
            investor_list != ""
        ].unique().tolist()
    )

    selected_investor = st.sidebar.selectbox(
        "Select Investor",
        investor_list
    )

    btn2 = st.sidebar.button(
        "Find Investor Details"
    )

    if btn2:
        load_investor_details(
            selected_investor
        )

    else:
        st.title("Investor Analysis")
        st.info(
            "Select an investor from the sidebar "
            "and click 'Find Investor Details'."
        )