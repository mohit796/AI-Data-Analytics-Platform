import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from sklearn.ensemble import RandomForestRegressor, IsolationForest


def generate_report(df):

    styles = getSampleStyleSheet()

    elements = []

    numeric = df.select_dtypes(include=['int64','float64']).columns
    cat = df.select_dtypes(include=['object']).columns




    elements.append(Paragraph("AI Business Analytics Report",styles['Title']))
    elements.append(Spacer(1,20))

    elements.append(
        Paragraph(
        "This report presents a comprehensive analysis of the uploaded dataset "
        "including statistical analysis, business insights, machine learning "
        "prediction and anomaly detection.",
        styles['Normal']
        )
    )

    elements.append(PageBreak())




    elements.append(Paragraph("Dataset Summary",styles['Heading1']))

    elements.append(
        Paragraph(f"Total Rows: {df.shape[0]}",styles['Normal'])
    )

    elements.append(
        Paragraph(f"Total Columns: {df.shape[1]}",styles['Normal'])
    )

    elements.append(
        Paragraph(
        "Dataset contains both numerical and categorical variables "
        "representing business related data.",
        styles['Normal']
        )
    )

    elements.append(PageBreak())





    if len(numeric)>0:

        fig = px.histogram(
            df,
            x=numeric[0],
            color_discrete_sequence=["#636EFA"],
            title="Data Distribution"
        )

        img = pio.to_image(fig,format="png")

        with open("charts/hist.png","wb") as f:
            f.write(img)

        elements.append(Paragraph("Distribution Analysis",styles['Heading2']))
        elements.append(Image("charts/hist.png",width=450,height=300))

        elements.append(
            Paragraph(
            "Histogram shows how numeric values are distributed in the dataset.",
            styles['Normal']
            )
        )

        elements.append(PageBreak())




    if len(cat)>0:

        counts = df[cat[0]].value_counts()

        fig = px.pie(
            names=counts.index,
            values=counts.values,
            title="Category Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3
        )

        img = pio.to_image(fig,format="png")

        with open("charts/pie.png","wb") as f:
            f.write(img)

        elements.append(Paragraph("Category Analysis",styles['Heading2']))
        elements.append(Image("charts/pie.png",width=450,height=300))

        elements.append(
            Paragraph(
            "Pie chart represents contribution of different categories.",
            styles['Normal']
            )
        )

        elements.append(PageBreak())




    if len(numeric)>1:

        fig = px.scatter(
            df,
            x=numeric[0],
            y=numeric[1],
            color_discrete_sequence=["#EF553B"],
            title="Variable Relationship"
        )

        img = pio.to_image(fig,format="png")

        with open("charts/scatter.png","wb") as f:
            f.write(img)

        elements.append(Paragraph("Correlation Analysis",styles['Heading2']))
        elements.append(Image("charts/scatter.png",width=450,height=300))

        elements.append(PageBreak())



    if len(numeric)>1:

        X = df[numeric[:-1]]
        y = df[numeric[-1]]

        model = RandomForestRegressor()

        model.fit(X,y)

        pred = model.predict(X)

        fig = px.line(
            pred,
            title="Machine Learning Prediction",
            color_discrete_sequence=["#00CC96"]
        )

        img = pio.to_image(fig,format="png")

        with open("charts/prediction.png","wb") as f:
            f.write(img)

        elements.append(Paragraph("Machine Learning Prediction",styles['Heading1']))
        elements.append(Image("charts/prediction.png",width=450,height=300))

        elements.append(
            Paragraph(
            "Random Forest regression model predicts expected trend "
            "based on historical patterns.",
            styles['Normal']
            )
        )

        elements.append(PageBreak())




    if len(numeric)>1:

        iso = IsolationForest()

        df["anomaly"] = iso.fit_predict(df[numeric])

        fig = px.scatter(
            df,
            x=numeric[0],
            y=numeric[1],
            color=df["anomaly"],
            title="Anomaly Detection",
            color_continuous_scale="RdYlGn"
        )

        img = pio.to_image(fig,format="png")

        with open("charts/anomaly.png","wb") as f:
            f.write(img)

        elements.append(Paragraph("Anomaly Detection",styles['Heading1']))
        elements.append(Image("charts/anomaly.png",width=450,height=300))

        elements.append(
            Paragraph(
            "Isolation Forest algorithm detects unusual observations "
            "that deviate from normal data patterns.",
            styles['Normal']
            )
        )

        elements.append(PageBreak())



    elements.append(Paragraph("Business Insights",styles['Heading1']))

    if len(numeric)>0:

        avg = df[numeric[0]].mean()

        elements.append(
            Paragraph(
            f"Average value of {numeric[0]} is {round(avg,2)}",
            styles['Normal']
            )
        )

    if len(cat)>0:

        top = df[cat[0]].value_counts().idxmax()

        elements.append(
            Paragraph(
            f"Most frequent category is {top}",
            styles['Normal']
            )
        )

    elements.append(
        Paragraph(
        "The dataset shows overall stable performance trend "
        "with potential business growth opportunities.",
        styles['Normal']
        )
    )



# CREATE PDF


    pdf = SimpleDocTemplate("reports/AI_Analytics_Report.pdf")

    pdf.build(elements)


    with open("reports/AI_Analytics_Report.pdf","rb") as f:

        st.download_button(
            "Download Professional Report",
            f,
            file_name="AI_Analytics_Report.pdf"
        )