import streamlit as st

def generate_insight(df, question):

    question = question.lower()

    if "column" in question:
        return f"The dataset contains {df.shape[1]} columns."

    elif "row" in question:
        return f"The dataset contains {df.shape[0]} rows."

    elif "columns name" in question or "column names" in question:
        return f"Columns are: {list(df.columns)}"

    elif "missing" in question:
        return f"Missing values:\n{df.isnull().sum()}"

    elif "mean" in question:
        return f"Mean values:\n{df.mean(numeric_only=True)}"

    else:
        return "This dataset contains valuable information. You can analyze trends, patterns, and predictions from it."



def show_insights(df):

    st.header("🤖 AI Data Assistant (Smart System)")

    question = st.text_input("Ask anything about your dataset")

    if question:
        answer = generate_insight(df, question)
        st.success(answer)