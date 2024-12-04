import streamlit as st
from transformers import pipeline
import pandas as pd
import yfinance as yf
import plotly.express as px
import os

# Set theme colors for First Citizens Bank branding
primary_color = "#004B8D"  # First Citizens Bank blue
secondary_color = "#FF8200"  # Accent color for analytics focus

# Configure Streamlit page
st.set_page_config(
    page_title="First Citizens Bank Risk Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Configuring header with logo on the top left
t1, t2 = st.columns((0.1, 0.8))
t1.image("index_0.jpeg", width=200)  # Replace 'index_0.png' with your logo file path
t2.title("Understanding Risk Analytics at First Citizens Bank")
t2.markdown(
    "Explore insights into First Citizens Bank's risk management strategies, alongside stock performance trends. "
    "This dashboard highlights applications of Data Science and AI/ML in risk analytics."
)

# Overview metrics
m1, m2, m3, m4 = st.columns((1, 1, 1, 1))
m1.metric(label="Founded", value="1898", help="First Citizens Bank was founded in North Carolina.")
m2.metric(label="Headquarters", value="Raleigh, NC", help="First Citizens Bank is headquartered in Raleigh.")
m3.metric(label="Ticker Symbol", value="FCNCA", help="Publicly traded on the NASDAQ exchange.")
m4.metric(label="Industry", value="Banking", help="Specializes in personal, commercial banking, and risk management.")

# Tabs for additional insights
tab1, tab2, tab3 = st.tabs(["Q&A Tool", "Stock & Risk Data", "About First Citizens Bank"])

# Tab 1: Q&A Tool
with tab1:
    st.subheader("First Citizens Bank Q&A Tool")
    st.write("Ask a question about First Citizens Bank's risk management and get an answer based on the preloaded context.")

    # Expanded Context
    context = """
    First Citizens Bank, established in 1898, is known for its robust risk management framework and commitment to financial stability. 
    The bank employs advanced analytics and machine learning models to manage credit risk, operational risk, and market risk effectively. 
    Risk management strategies include:
    
    - Comprehensive credit underwriting practices to assess borrower risk.
    - Stress testing to measure resilience against economic downturns.
    - Fraud detection systems powered by AI for real-time monitoring.
    - Regulatory compliance to meet all federal and international standards.

    First Citizens Bank also focuses on portfolio diversification to mitigate systemic risk and provides transparency in its financial disclosures.
    """

    # User question input
    user_question = st.text_input("Enter your question about First Citizens Bank:")
    if user_question:
        qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
        answer = qa_pipeline(question=user_question, context=context)
        st.write(f"**Answer:** {answer['answer']}")

    # Suggested questions
    st.write("### Suggested Questions:")
    st.write("- What are First Citizens Bank's key risk management strategies?")
    st.write("- How does First Citizens Bank manage credit risk?")
    st.write("- What fraud detection technologies are used by the bank?")
    st.write("- How does First Citizens ensure compliance with regulations?")

# Tab 2: Stock & Risk Data
with tab2:
    st.subheader("Stock Performance and Risk Metrics")
    st.write("Explore First Citizens Bank's stock trends and key risk indicators.")

    # File paths
    stock_csv = "fcnca_stock_data.csv"

    # Check if CSV exists, if not, download and save it
    if not os.path.exists(stock_csv):
        stock_data = yf.download("FCNCA", start="2020-01-01", end="2024-12-31")
        stock_data.reset_index(inplace=True)
        stock_data.to_csv(stock_csv, index=False)
    else:
        stock_data = pd.read_csv(stock_csv)

    # Stock price visualization
    st.write("### FCNCA Stock Price Over Time")
    fig_stock = px.line(
        stock_data,
        x="Date",
        y="Close",
        title="First Citizens Bank (FCNCA) Stock Performance",
        line_shape="spline",
        color_discrete_sequence=[primary_color]
    )
    fig_stock.update_layout(
        title_font_color=primary_color,
        plot_bgcolor="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig_stock, use_container_width=True)

    # Mock risk data for demonstration
    risk_data = pd.DataFrame({
        "Metric": ["Credit Risk", "Operational Risk", "Market Risk"],
        "Risk Level (%)": [35, 25, 40]
    })

    # Risk level visualization
    st.write("### Risk Exposure Breakdown")
    fig_risk = px.pie(
        risk_data,
        names="Metric",
        values="Risk Level (%)",
        title="Risk Exposure at First Citizens Bank",
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    fig_risk.update_traces(textinfo="percent+label")
    st.plotly_chart(fig_risk, use_container_width=True)

# Tab 3: About First Citizens Bank
with tab3:
    st.subheader("About First Citizens Bank")
    st.write("""
    First Citizens Bank has a long history of financial innovation and stability. Known for its customer-first approach, the bank combines traditional values with modern analytics to provide personalized solutions.
    """)
    st.subheader("Core Values")
    st.write("""
    - **Resilience**: Adapts to changing economic conditions through proactive risk management.
    - **Transparency**: Upholds ethical practices and clear financial disclosures.
    - **Innovation**: Leverages technology to improve risk analytics and customer experience.
    """)

    st.subheader("Key Achievements")
    st.write("""
    - Acquired multiple regional banks, expanding its footprint across the U.S.
    - Developed AI-driven fraud detection systems to enhance operational efficiency.
    - Recognized for excellence in regulatory compliance and risk mitigation.
    """)
