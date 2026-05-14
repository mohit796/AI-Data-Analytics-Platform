import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def show_technical(df):

    st.header(" Technical Analysis (Deep Insights)")

    numeric_cols = df.select_dtypes(include=['int64','float64']).columns

    # 1 Histogram
    st.subheader("1️⃣ Distribution Analysis")
    for col in numeric_cols[:3]:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)
        st.write(f"{col} shows how values are distributed. Helps detect skewness.")

    # 2 Correlation
    st.subheader("2️⃣ Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df[numeric_cols].corr(), annot=True, ax=ax)
    st.pyplot(fig)
    st.write("Shows relationship between variables. Strong correlation helps prediction.")

    # 3 Boxplot
    st.subheader("3️⃣ Outlier Detection")
    for col in numeric_cols[:3]:
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col], ax=ax)
        st.pyplot(fig)
        st.write(f"{col} may contain outliers affecting performance.")

    # 4 Pairplot
    st.subheader("4️⃣ Feature Relationships")
    sns.pairplot(df[numeric_cols[:4]])
    st.pyplot()
    st.write("Multiple variable relationships visualization.")

    # 5 Line Plot
    st.subheader("5️⃣ Trend Analysis")
    for col in numeric_cols[:2]:
        fig, ax = plt.subplots()
        ax.plot(df[col])
        st.pyplot(fig)
        st.write(f"{col} trend over index/time.")

    st.success(" Complete technical analysis with insights generated")