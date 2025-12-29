import yfinance as yf
import streamlit as st
import pandas as pd

# App configuration
st.set_page_config(layout="wide")

# Sidebar controls
with st.sidebar:
    ticker = st.text_input("Enter Ticker Symbol", "AAPL")
    timeframe = st.radio("Timeframe", ["Quarterly", "Annual"])
    metrics = st.multiselect(
        "Select Metrics",
        ["Revenue", "Margins", "Debt", "Valuation", "Buybacks"],
        default=["Revenue", "Margins"]
    )

# Main content
st.title(f"Fundamental Analysis: {ticker}")

# Data loading and processing
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_data(ticker):
    stock = yf.Ticker(ticker)
    data = {
        'income_stmt': stock.financials,
        'balance_sheet': stock.balance_sheet,
        'cash_flow': stock.cashflow,
        'quarterly_income_stmt': stock.quarterly_financials,
        'quarterly_balance_sheet': stock.quarterly_balance_sheet,
        'quarterly_cash_flow': stock.quarterly_cashflow,
        'info': stock.info  # Contains valuation metrics
    }
    return data

raw_data = load_data(ticker)

# Normalization layer
normalization_layer = {
    'Total Revenue': 'Total Revenue',
    'Gross Profit': 'Gross Profit',
    'Operating Income': 'Operating Income',
    'Net Income': 'Net Income',
    'Total Debt': 'Long Term Debt',
    'Shares Outstanding': 'Common Stock'
}

# Process raw yfinance data into standardized format
def process_financials(raw_data, frequency='annual'):
    if frequency == 'quarterly':
        income = raw_data['quarterly_income_stmt']
        balance = raw_data['quarterly_balance_sheet']
        cashflow = raw_data['quarterly_cash_flow']
    else:
        income = raw_data['income_stmt']
        balance = raw_data['balance_sheet']
        cashflow = raw_data['cash_flow']

    # Combine key metrics into single dataframe
    metrics = pd.DataFrame({
        'Revenue': income.loc[normalization_layer['Total Revenue']],
        'Gross Margin': income.loc[normalization_layer['Gross Profit']] / income.loc[normalization_layer['Total Revenue']],
        'Operating Margin': income.loc[normalization_layer['Operating Income']] / income.loc[normalization_layer['Total Revenue']],
        'Net Margin': income.loc[normalization_layer['Net Income']] / income.loc[normalization_layer['Total Revenue']],
        'Total Debt': balance.loc[normalization_layer['Total Debt']],
        'Shares Outstanding': balance.loc[normalization_layer['Shares Outstanding']]
    })

    return metrics

processed_data = process_financials(raw_data, timeframe.lower())

# Metric cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Current PE Ratio", raw_data['info'].get('trailingPE', 'N/A'))
with col2:
    st.metric("Market Cap", f"${raw_data['info'].get('marketCap', 0)/1e9:.2f}B")
with col3:
    st.metric("Debt/Equity", raw_data['info'].get('debtToEquity', 'N/A'))

# Interactive charts
if "Revenue" in metrics:
    st.subheader("Revenue Trend")
    st.bar_chart(processed_data['Revenue'])

if "Margins" in metrics:
    st.subheader("Margin Trends")
    margin_cols = st.columns(3)
    with margin_cols[0]:
        st.line_chart(processed_data['Gross Margin'], use_container_width=True)
    with margin_cols[1]:
        st.line_chart(processed_data['Operating Margin'], use_container_width=True)
    with margin_cols[2]:
        st.line_chart(processed_data['Net Margin'], use_container_width=True)