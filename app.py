import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="AI Data Quality & Governance Portal", layout="wide")

st.title("🛡️ AI-Assisted Data Quality & Governance Portal")
st.caption("Real-time monitoring across Bronze, Silver, and Gold Medallion layers")

# Top KPI Summary Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Pipeline Health", "98.4%", "+0.5%")
col2.metric("Schema Drift Auto-Resolved", "14 Fields", "COALESCE Active")
col3.metric("dbt Contracts Passed", "42 / 42", "100%")
col4.metric("AI Anomalies Detected", "2 Flagged", "-3 vs yesterday")

st.markdown("---")

# Tabbed Dashboard Sections
tab1, tab2, tab3 = st.tabs(["📊 Quality & Anomaly Metrics", "🔄 Schema Drift & Unification", "⛓️ Medallion Lineage Health"])

with tab1:
    st.subheader("Statistical Anomaly & Contract Assertions")
    
    # Mock anomaly data stream
    df_anomalies = pd.DataFrame({
        "Timestamp": pd.date_range(end=pd.Timestamp.now(), periods=6, freq="h"),
        "Table": ["bronze_receipts", "silver_transactions", "silver_transactions", "gold_sales_mart", "bronze_receipts", "silver_merchants"],
        "Test Type": ["Schema Drift", "dbt not_null", "Distribution Shift", "dbt Model Contract", "OCR Anomaly", "Fuzzy Matching"],
        "Severity": ["Medium", "High", "Low", "Critical", "Medium", "Low"],
        "Status": ["Auto-Resolved", "Passed", "Flagged for Review", "Passed", "Auto-Cleansed", "Auto-Resolved"],
        "Details": [
            "New key 'vendor_tax_id' auto-mapped via COALESCE",
            "Zero nulls found in primary key",
            "Revenue metric deviating by +2.3 standard deviations",
            "Data types strictly match expected schema.yml typing",
            "Cleaned non-standard currency symbols via dynamic cast",
            "Matched 'Acme Corp' to 'ACME Incorporated'"
        ]
    })
    st.dataframe(df_anomalies, use_container_width=True)
    
    # Anomaly distribution chart
    fig_anomaly = px.histogram(df_anomalies, x="Table", color="Severity", title="DQ Events by Model Tier", barmode="group")
    st.plotly_chart(fig_anomaly, use_container_width=True)

with tab2:
    st.subheader("Automated Schema Drift Engine (`union_by_name` & `COALESCE`)")
    st.markdown("Tracks semi-structured JSON attribute drift across raw ingestion and maps alternative keys into standardized Silver schemas.")
    
    drift_data = pd.DataFrame({
        "Raw Ingested Key": ["merchant_name", "vendor_title", "store_id", "trx_amount", "total_price", "tax_val"],
        "Target Silver Column": ["merchant_id", "merchant_id", "merchant_id", "transaction_amount", "transaction_amount", "tax_amount"],
        "Mapping Method": ["COALESCE", "COALESCE", "COALESCE", "COALESCE + CAST", "COALESCE + CAST", "Explicit Type Cast"],
        "Type Validation": ["VARCHAR", "VARCHAR", "VARCHAR", "DOUBLE", "DOUBLE", "DOUBLE"],
        "Contract Status": ["Valid", "Valid", "Valid", "Valid", "Valid", "Valid"]
    })
    st.table(drift_data)

with tab3:
    st.subheader("Medallion Architecture Health Status")
    
    col_b, col_s, col_g = st.columns(3)
    
    with col_b:
        st.markdown("### 🥉 Bronze Layer")
        st.write("**Source:** JSON / File Ingestion")
        st.write("**Engine:** DuckDB (`union_by_name=True`)")
        st.success("Ingestion Status: Operational")
        st.progress(0.99)
        
    with col_s:
        st.markdown("### 🥈 Silver Layer")
        st.write("**Engine:** dbt Core + DuckDB")
        st.write("**Quality:** Model Contracts & Assertions")
        st.success("Transformation Status: Operational")
        st.progress(0.98)
        
    with col_g:
        st.markdown("### 🥇 Gold Layer")
        st.write("**Engine:** Cube Semantic Brokerage")
        st.write("**Access:** REST API & BI Queries")
        st.success("Semantic Layer: Operational")
        st.progress(1.0)
