# Additional tabs for Stock and Risk Data
tab_stock, tab_risk = st.tabs(["Stock Performance", "Risk Exposure"])

# Tab: Stock Performance
with tab_stock:
    st.subheader("Stock Performance")
    st.write("Explore First Citizens Bank's stock trends.")

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

# Tab: Risk Exposure
with tab_risk:
    st.subheader("Risk Exposure")
    st.write(
        "Gain insights into First Citizens Bank's financial and regulatory risk exposures. "
        "This breakdown highlights key areas impacting the bank's operations."
    )

    # Updated risk data for financial and regulatory risks
    risk_data = pd.DataFrame({
        "Category": ["Financial Risk", "Financial Risk", "Regulatory Risk", "Regulatory Risk"],
        "Subcategory": ["Credit Risk", "Market Risk", "Compliance Risk", "Operational Risk"],
        "Risk Level (%)": [30, 25, 25, 20]
    })

    # Sunburst visualization for Risk Exposure
    st.write("### Risk Exposure Breakdown")
    fig_risk_sunburst = px.sunburst(
        risk_data,
        path=["Category", "Subcategory"],
        values="Risk Level (%)",
        title="Financial and Regulatory Risk Exposure at First Citizens Bank",
        color="Risk Level (%)",
        color_continuous_scale=px.colors.sequential.RdBu,
        hover_data={"Risk Level (%)": True}
    )
    fig_risk_sunburst.update_layout(margin=dict(t=30, l=0, r=0, b=0))
    st.plotly_chart(fig_risk_sunburst, use_container_width=True)
