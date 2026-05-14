import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def show_prediction(df):

    st.header("📈 Prediction Analysis (AI Story Mode)")

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns

    if len(numeric_cols) < 2:
        st.warning("Not enough numeric data for prediction")
        return

    x_col = st.selectbox("Select Feature (X)", numeric_cols)
    y_col = st.selectbox("Select Target (Y)", numeric_cols)

    X = df[[x_col]]
    y = df[y_col]

    model = LinearRegression()
    model.fit(X, y)

    preds = model.predict(X)

    # GRAPH
    fig, ax = plt.subplots()
    ax.scatter(X, y)
    ax.plot(X, preds)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

    # STORY (IMPORTANT )
    st.subheader("📖 Business Insight Story")

    st.write(f"""
      As {x_col} increases, the {y_col} also changes based on a learned pattern.

      The model identified a relationship between these variables, meaning:
    - Higher {x_col} values tend to impact {y_col}
    - This can be used for forecasting future trends

      Business Benefit:
    - Helps in decision making
    - Predict future performance
    - Optimize strategy based on data trends

      Conclusion:
    This prediction model gives a clear understanding of how {x_col} influences {y_col}.
    """)