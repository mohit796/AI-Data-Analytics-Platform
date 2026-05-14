import streamlit as st
import pandas as pd

#module
from modules.dashboard import show_dashboard
from modules.prediction import show_prediction
from modules.insights import show_insights
from modules.technical import show_technical
from modules.report import generate_report


# Page config
st.set_page_config(
    page_title="AI Analytics Platform",
    layout="wide"
)

# Title
st.title(" AI Business Intelligence Platform")

# File upload
file = st.file_uploader(" Upload CSV Dataset", type=["csv"])

if file is not None:

    # Read dataset
    try:
        df = pd.read_csv(file)
        st.success("Dataset Loaded Successfully")

    except Exception as e:
        st.error(f" Error loading file: {e}")
        st.stop()

    # Show basic info
    st.write(" Dataset Preview")
    st.dataframe(df.head())

    # Handle missing values (numeric only)
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Sidebar navigation
    mode = st.sidebar.radio(
        " Navigation",
        [
            "Dashboard",
            "Prediction",
            "Technical Analysis",
            "AI Insights",
            "Generate Report"
        ]
    )

    # Navigation routing
    if mode == "Dashboard":
        show_dashboard(df)

    elif mode == "Prediction":
        show_prediction(df)

    elif mode == "Technical Analysis":
        show_technical(df)

    elif mode == "AI Insights":
        show_insights(df)

    elif mode == "Generate Report":
        generate_report(df)

else:
    st.info(" Please upload a CSV file to get started.")