import streamlit as st
import plotly.express as px

def show_dashboard(df):

    st.header("📊 Smart Dashboard")

    numeric = df.select_dtypes(include=['int64','float64']).columns
    cat = df.select_dtypes(include=['object']).columns

    c1,c2,c3 = st.columns(3)

    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])

    if len(numeric)>0:
        c3.metric("Average", round(df[numeric[0]].mean(),2))

    r1 = st.columns(3)
    r2 = st.columns(3)

    if len(numeric)>0:
        fig = px.histogram(df,x=numeric[0],title="Distribution")
        r1[0].plotly_chart(fig,use_container_width=True)

    if len(cat)>0:
        counts=df[cat[0]].value_counts()
        fig=px.pie(names=counts.index,values=counts.values)
        r1[1].plotly_chart(fig,use_container_width=True)

    if len(cat)>0:
        counts=df[cat[0]].value_counts()
        fig=px.bar(x=counts.index,y=counts.values)
        r1[2].plotly_chart(fig,use_container_width=True)

    if len(numeric)>1:
        fig=px.scatter(df,x=numeric[0],y=numeric[1])
        r2[0].plotly_chart(fig,use_container_width=True)

    if len(numeric)>0:
        fig=px.line(df,y=numeric[0])
        r2[1].plotly_chart(fig,use_container_width=True)

    if len(numeric)>0:
        fig=px.box(df,y=numeric[0])
        r2[2].plotly_chart(fig,use_container_width=True)