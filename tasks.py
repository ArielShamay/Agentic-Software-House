from crewai import Task
from agents import product_manager, architect, senior_developer, qa_engineer

# =============================================================================
# 🏢 VALUEINVESTOR PRO - PREMIUM FINANCIAL DASHBOARD
# =============================================================================
# A Bloomberg-grade financial analysis tool for Value Investors
# Built with: Streamlit, yfinance, Plotly
# Design Philosophy: Apple-like minimalism meets high-end Fintech
# =============================================================================

# -----------------------------------------------------------------------------
# 📋 TASK 1: PRODUCT MANAGER - Define ValueInvestor Pro Requirements
# -----------------------------------------------------------------------------
task_define_requirements = Task(
    description="""
    You are the Product Manager for "ValueInvestor Pro" - a PREMIUM financial dashboard
    for Value Investors. This app must feel like a Bloomberg terminal meets Apple design.

    ## YOUR MISSION: Create a comprehensive Product Requirements Document (PRD)

    ### 🎨 VISUAL IDENTITY REQUIREMENTS

    **Design Philosophy:**
    - Ultra-modern, minimalist design inspired by Apple products
    - DARK MODE by default with high contrast elements
    - No "walls of text" - use Dashboard grid system
    - Generous whitespace between all elements
    - Clean, distraction-free interface

    **Color Scheme:**
    - Background: Deep dark (#0E1117 or similar)
    - Cards/Containers: Slightly lighter dark (#1E2130)
    - Primary Accent: Teal/Cyan (#00D4AA) for positive values
    - Secondary: Purple (#7B61FF) for secondary metrics
    - Positive Changes: Green (#00FF88)
    - Negative Changes: Red (#FF4B4B)
    - Text: White (#FFFFFF) and Gray (#8B949E)

    ### 🏗️ LAYOUT STRUCTURE

    **Sidebar (Control Center):**
    - Prominent Search Bar: "Enter Stock Ticker (e.g., AAPL, NVDA)"
    - Large, stylish "🔍 Analyze" button
    - Timeframe Selector: "Last 5 Years", "Last 10 Years", "Max History"
    - The sidebar should feel like a sleek control panel

    **Main Dashboard (4 Tabs):**

    **Tab 1: 📊 Snapshot (At a Glance)**
    - Giant Company Name + Ticker header
    - Real-time price with Green/Red daily change indicator
    - 4-5 Key Metric Cards in a row:
      * Market Cap (formatted: $2.5T)
      * P/E Ratio
      * Dividend Yield (%)
      * Beta (Volatility)
      * 52-Week Range
    - Master Chart: Large Candlestick chart with Volume bars

    **Tab 2: 📈 Growth Engine (Profitability)**
    - Revenue vs Net Income: Grouped bar chart (side by side)
    - Margins Analysis: Multi-line chart (Gross, Operating, Net Margin %)
    - EPS Trend: Line chart showing Earnings Per Share growth

    **Tab 3: 🏰 Moat & Efficiency (Quality)**
    - ROIC Chart: Line chart - Return on Invested Capital (THE key metric)
    - Free Cash Flow: Bar chart showing actual cash generation
    - ROE Trend: Return on Equity over time

    **Tab 4: 💰 Valuation & Health (Price & Risk)**
    - Historical P/E: Line chart showing valuation trend
    - Shares Outstanding: Line chart with color coding:
      * Green if trending DOWN (buybacks = good)
      * Red if trending UP (dilution = bad)
    - Debt vs Cash: Stacked bar comparing Long-Term Debt vs Cash

    ### 📐 DATA FORMATTING RULES (CRITICAL)

    - NO scientific notation (never 1.5e9)
    - Billions: "$15.4B"
    - Millions: "$350M"  
    - Thousands: "$45K"
    - Percentages: "15.4%"
    - Ratios: "24.5x"
    - Missing data: Show "N/A" gracefully, don't break the app

    ### ✅ ACCEPTANCE CRITERIA

    1. App loads in under 3 seconds
    2. All charts are interactive (hover, zoom, toggle)
    3. No raw numbers displayed anywhere
    4. Professional dark theme throughout
    5. Responsive layout
    6. Graceful error handling for invalid tickers

    Document these requirements in detail for the Architect and Developer.
    """,
    expected_output="""A comprehensive PRD for ValueInvestor Pro containing:
    1. Complete visual identity specifications
    2. Detailed layout wireframes for all 4 tabs
    3. Exact metric definitions and data sources
    4. Number formatting rules with examples
    5. Color scheme specifications
    6. Interaction requirements for each chart
    7. Error handling requirements
    8. Acceptance criteria checklist""",
    agent=product_manager
)

# -----------------------------------------------------------------------------
# 🏗️ TASK 2: SOFTWARE ARCHITECT - Technical Architecture Design
# -----------------------------------------------------------------------------
task_design_architecture = Task(
    description="""
    Design the complete technical architecture for "ValueInvestor Pro".
    This must be production-grade code that handles real financial data.

    ## TECHNOLOGY STACK (MANDATORY)

    ```python
    # Required Imports - USE EXACTLY THESE
    import streamlit as st
    import yfinance as yf
    import pandas as pd
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    from datetime import datetime, timedelta
    ```

    ## FORBIDDEN TECHNOLOGIES
    - ❌ st.bar_chart() - Too basic
    - ❌ st.line_chart() - Not interactive enough
    - ❌ matplotlib - Not interactive
    - ❌ altair - Not professional enough

    ## REQUIRED UTILITY FUNCTIONS

    Design these helper functions that MUST be implemented:

    ### 1. Number Formatting Suite
    ```python
    def format_large_number(value, prefix="$"):
        '''
        Converts numbers to human-readable format.
        1500000000 → "$1.50B"
        250000000 → "$250.00M"
        45000 → "$45.00K"
        None/NaN → "N/A"
        '''

    def format_percentage(value, decimals=2):
        '''
        Converts decimal to percentage.
        0.1545 → "15.45%"
        None → "N/A"
        '''

    def format_ratio(value, suffix="x"):
        '''
        Formats ratios like P/E.
        24.567 → "24.57x"
        '''

    def format_price_change(current, previous):
        '''
        Returns formatted change with color indicator.
        Returns: (formatted_string, color)
        Example: ("+$5.23 (+2.45%)", "green")
        '''
    ```

    ### 2. Data Fetching Architecture
    ```python
    @st.cache_data(ttl=3600, show_spinner=False)
    def fetch_stock_data(ticker: str) -> tuple[dict, str]:
        '''
        Fetches ALL required data for a ticker.
        Returns: (data_dict, error_message)
        
        Must fetch:
        - stock.info (company details, current price, ratios)
        - stock.financials (annual income statement)
        - stock.quarterly_financials
        - stock.balance_sheet (annual)
        - stock.quarterly_balance_sheet
        - stock.cashflow (annual)
        - stock.quarterly_cashflow
        - stock.history(period="max") (for candlestick chart)
        
        Implements try/except for EACH fetch operation.
        '''

    def safe_get(data, key, default="N/A"):
        '''
        Safely retrieves nested data from yfinance responses.
        Handles None, NaN, missing keys gracefully.
        '''
    ```

    ### 3. Chart Factory Functions
    Design chart creation functions for each visualization:

    ```python
    def create_candlestick_chart(history_df, ticker):
        '''Creates interactive candlestick with volume subplot'''

    def create_revenue_income_chart(financials_df, ticker):
        '''Creates grouped bar chart: Revenue vs Net Income'''

    def create_margins_chart(financials_df, ticker):
        '''Creates multi-line chart: Gross, Operating, Net Margins'''

    def create_fcf_chart(cashflow_df, ticker):
        '''Creates bar chart for Free Cash Flow'''

    def create_pe_history_chart(history_df, info, ticker):
        '''Creates P/E ratio trend line chart'''

    def create_shares_chart(balance_df, ticker):
        '''Creates shares outstanding with green/red coloring'''

    def create_debt_cash_chart(balance_df, ticker):
        '''Creates stacked bar: Debt vs Cash'''
    ```

    ### 4. Plotly Theme Configuration
    ```python
    CHART_THEME = {
        'template': 'plotly_dark',
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'font_color': '#FFFFFF',
        'primary_color': '#00D4AA',
        'secondary_color': '#7B61FF',
        'positive_color': '#00FF88',
        'negative_color': '#FF4B4B',
        'grid_color': 'rgba(128,128,128,0.2)',
        'height': 450
    }
    ```

    ### 5. Layout Architecture Blueprint
    ```
    app.py Structure:
    
    1. IMPORTS & CONFIG
       - All imports at top
       - st.set_page_config(layout="wide", page_title="ValueInvestor Pro")
       - Custom CSS for dark theme
    
    2. UTILITY FUNCTIONS
       - All formatting functions
       - Data fetching functions
       - Chart creation functions
    
    3. SIDEBAR
       - st.sidebar.title("ValueInvestor Pro")
       - Ticker input
       - Timeframe selector
       - Analyze button
    
    4. MAIN CONTENT
       - Company header (name, price, change)
       - st.tabs() with 4 tabs
       - Each tab contains its specific charts
    
    5. ERROR HANDLING
       - Invalid ticker message
       - Missing data handling
       - Network error handling
    ```

    ## DATA SOURCES MAPPING
    
    | Metric | yfinance Source |
    |--------|-----------------|
    | Market Cap | info['marketCap'] |
    | P/E Ratio | info['trailingPE'] |
    | Dividend Yield | info['dividendYield'] |
    | Beta | info['beta'] |
    | Revenue | financials.loc['Total Revenue'] |
    | Net Income | financials.loc['Net Income'] |
    | Gross Profit | financials.loc['Gross Profit'] |
    | Operating Income | financials.loc['Operating Income'] |
    | Free Cash Flow | cashflow.loc['Free Cash Flow'] |
    | Total Debt | balance_sheet.loc['Long Term Debt'] |
    | Cash | balance_sheet.loc['Cash And Cash Equivalents'] |
    | Shares Outstanding | info['sharesOutstanding'] |

    Provide the complete technical specification for the developer.
    """,
    expected_output="""A Technical Design Document containing:
    1. Complete import list and configuration
    2. All utility function signatures with docstrings
    3. Data fetching patterns with error handling
    4. Chart creation patterns for each visualization type
    5. Plotly theme configuration
    6. Layout structure blueprint
    7. Data source mapping table
    8. CSS styling recommendations for dark theme""",
    agent=architect
)

# -----------------------------------------------------------------------------
# 💻 TASK 3: SENIOR DEVELOPER - Complete Implementation
# -----------------------------------------------------------------------------
task_write_code = Task(
    description="""
    Build "ValueInvestor Pro" - a PREMIUM financial dashboard for Value Investors.
    Write the COMPLETE production code and save it to 'app.py'.

    ⚠️ THIS IS A HIGH-END FINTECH APPLICATION. Quality is NON-NEGOTIABLE.

    ## 📁 FILE OUTPUT
    OVERWRITE 'app.py' with your complete implementation.
    The file must run perfectly with: `streamlit run app.py`

    ## 🚫 ABSOLUTELY FORBIDDEN
    - st.bar_chart() - BANNED
    - st.line_chart() - BANNED
    - matplotlib - BANNED
    - Raw numbers like 15300000000 - BANNED
    - Scientific notation - BANNED
    - Ugly default colors - BANNED

    ## ✅ REQUIRED IMPLEMENTATION

    ### STEP 1: Page Configuration & Custom CSS
    ```python
    import streamlit as st
    import yfinance as yf
    import pandas as pd
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    from datetime import datetime, timedelta

    st.set_page_config(
        page_title="ValueInvestor Pro",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS for premium dark theme
    st.markdown('''
    <style>
        .stApp {
            background-color: #0E1117;
        }
        .metric-card {
            background-color: #1E2130;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .big-price {
            font-size: 48px;
            font-weight: bold;
        }
        .price-up { color: #00FF88; }
        .price-down { color: #FF4B4B; }
    </style>
    ''', unsafe_allow_html=True)
    ```

    ### STEP 2: Utility Functions (MUST IMPLEMENT ALL)
    ```python
    def format_large_number(value, prefix="$"):
        if value is None or pd.isna(value):
            return "N/A"
        
        abs_val = abs(float(value))
        sign = "-" if value < 0 else ""
        
        if abs_val >= 1_000_000_000_000:
            return f"{sign}{prefix}{abs_val/1_000_000_000_000:.2f}T"
        elif abs_val >= 1_000_000_000:
            return f"{sign}{prefix}{abs_val/1_000_000_000:.2f}B"
        elif abs_val >= 1_000_000:
            return f"{sign}{prefix}{abs_val/1_000_000:.2f}M"
        elif abs_val >= 1_000:
            return f"{sign}{prefix}{abs_val/1_000:.2f}K"
        else:
            return f"{sign}{prefix}{abs_val:,.2f}"

    def format_percentage(value):
        if value is None or pd.isna(value):
            return "N/A"
        return f"{float(value) * 100:.2f}%"

    def safe_get(data, key, default="N/A"):
        try:
            val = data.get(key)
            if val is None or (isinstance(val, float) and pd.isna(val)):
                return default
            return val
        except:
            return default
    ```

    ### STEP 3: Data Fetching with Error Handling
    ```python
    @st.cache_data(ttl=3600, show_spinner=False)
    def fetch_stock_data(ticker):
        try:
            stock = yf.Ticker(ticker)
            
            data = {
                'info': stock.info,
                'history': stock.history(period="max"),
                'financials': stock.financials,
                'quarterly_financials': stock.quarterly_financials,
                'balance_sheet': stock.balance_sheet,
                'quarterly_balance_sheet': stock.quarterly_balance_sheet,
                'cashflow': stock.cashflow,
                'quarterly_cashflow': stock.quarterly_cashflow
            }
            
            # Validate we got real data
            if not data['info'].get('shortName'):
                return None, "Invalid ticker or no data available"
            
            return data, None
            
        except Exception as e:
            return None, f"Error fetching data: {str(e)}"
    ```

    ### STEP 4: Sidebar Implementation
    ```python
    with st.sidebar:
        st.title("📈 ValueInvestor Pro")
        st.markdown("---")
        
        ticker = st.text_input(
            "Enter Stock Ticker",
            value="AAPL",
            placeholder="e.g., AAPL, MSFT, NVDA"
        ).upper()
        
        timeframe = st.selectbox(
            "Timeframe",
            ["Last 5 Years", "Last 10 Years", "Max History"]
        )
        
        analyze_btn = st.button("🔍 Analyze", type="primary", use_container_width=True)
        
        st.markdown("---")
        st.caption("Built for Value Investors")
    ```

    ### STEP 5: Main Content with 4 Tabs
    
    **Header Section:**
    - Display company name in large font
    - Show current price with change (green/red)
    - 4-5 metric cards using st.columns(5)

    **Tab 1: Snapshot**
    - Candlestick chart with volume (use make_subplots)
    - Chart config: dark theme, height=500

    **Tab 2: Growth Engine**
    - Revenue vs Net Income grouped bar chart
    - Margins line chart (Gross, Operating, Net)

    **Tab 3: Moat & Efficiency**  
    - Free Cash Flow bar chart
    - ROIC/ROE trend lines (if data available)

    **Tab 4: Valuation & Health**
    - P/E ratio trend
    - Shares outstanding (green if decreasing, red if increasing)
    - Debt vs Cash stacked bars

    ### STEP 6: Plotly Chart Standards
    
    ALL charts must follow this pattern:
    ```python
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=dates,
        y=values,
        name='Revenue',
        marker_color='#00D4AA',
        hovertemplate='<b>%{x}</b><br>Revenue: %{y:$,.0f}<extra></extra>'
    ))
    
    fig.update_layout(
        title=dict(text=f'{ticker} - Revenue Trend', font=dict(size=20)),
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=450,
        margin=dict(l=50, r=50, t=80, b=50),
        legend=dict(orientation='h', yanchor='bottom', y=1.02),
        xaxis=dict(showgrid=True, gridcolor='rgba(128,128,128,0.2)'),
        yaxis=dict(showgrid=True, gridcolor='rgba(128,128,128,0.2)')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    ```

    ### STEP 7: Color Scheme Constants
    ```python
    COLORS = {
        'primary': '#00D4AA',      # Teal - primary accent
        'secondary': '#7B61FF',    # Purple - secondary
        'positive': '#00FF88',     # Green - gains
        'negative': '#FF4B4B',     # Red - losses
        'neutral': '#8B949E',      # Gray - neutral
        'revenue': '#00D4AA',      # Revenue bars
        'income': '#7B61FF',       # Net income bars
        'gross_margin': '#00D4AA',
        'operating_margin': '#7B61FF', 
        'net_margin': '#FF6B6B'
    }
    ```

    ### STEP 8: Final Checklist Before Saving
    
    ✅ Page config with wide layout and dark theme
    ✅ Custom CSS for premium look
    ✅ All formatting functions implemented
    ✅ Data fetching with try/except
    ✅ @st.cache_data decorator on fetch function
    ✅ Sidebar with ticker input and timeframe
    ✅ 4 tabs implemented (Snapshot, Growth, Moat, Valuation)
    ✅ All charts use plotly.graph_objects
    ✅ All charts have template='plotly_dark'
    ✅ All numbers use format_large_number()
    ✅ Metric cards use st.columns() layout
    ✅ Error handling for invalid tickers
    ✅ No forbidden elements (st.bar_chart, matplotlib, etc.)

    ## 🎯 DELIVERABLE
    A complete, production-ready 'app.py' file that creates a Bloomberg-grade
    financial dashboard with all 4 tabs fully functional.

    Write the COMPLETE code now. Do not skip any sections.
    """,
    expected_output="""A complete 'app.py' file (300+ lines) containing:
    1. All imports and page configuration
    2. Custom CSS for dark premium theme
    3. All utility functions (format_large_number, format_percentage, safe_get)
    4. Data fetching function with caching and error handling
    5. Sidebar with ticker input and controls
    6. Company header with formatted price and metrics
    7. 4 fully implemented tabs:
       - Tab 1: Snapshot with candlestick chart
       - Tab 2: Growth Engine with revenue/margins charts
       - Tab 3: Moat & Efficiency with FCF chart
       - Tab 4: Valuation with P/E, shares, debt charts
    8. All charts using Plotly with dark theme
    9. Professional error handling throughout""",
    agent=senior_developer
)

# -----------------------------------------------------------------------------
# 🔍 TASK 4: QA ENGINEER - Comprehensive Quality Assurance
# -----------------------------------------------------------------------------
task_review_code = Task(
    description="""
    Perform COMPREHENSIVE quality assurance on 'app.py' for ValueInvestor Pro.
    This is a premium financial application - quality standards are extremely high.

    ## 🔎 QA INSPECTION CHECKLIST

    ### A. IMPORT & CONFIGURATION AUDIT
    ```
    ✓ import streamlit as st
    ✓ import yfinance as yf  
    ✓ import pandas as pd
    ✓ import plotly.graph_objects as go
    ✓ st.set_page_config with layout="wide"
    ✗ FAIL if: import matplotlib, import altair
    ```

    ### B. FORBIDDEN PATTERNS SCAN
    Search the entire file for these BANNED patterns:
    ```
    ❌ st.bar_chart - INSTANT FAIL
    ❌ st.line_chart - INSTANT FAIL
    ❌ plt. (matplotlib) - INSTANT FAIL
    ❌ alt. (altair) - INSTANT FAIL
    ❌ 1000000000 (raw large numbers in display) - FAIL
    ❌ 1e9 or 1e10 (scientific notation) - FAIL
    ```

    ### C. REQUIRED PATTERNS VERIFICATION
    Confirm these patterns EXIST in the code:
    ```
    ✓ go.Figure() - Plotly figure creation
    ✓ go.Bar( or go.Scatter( or go.Candlestick( - Chart types
    ✓ st.plotly_chart( - Rendering Plotly charts
    ✓ st.tabs( - Tab navigation
    ✓ st.columns( - Multi-column layout
    ✓ st.metric( - Metric cards
    ✓ st.sidebar - Sidebar usage
    ✓ @st.cache_data - Data caching
    ✓ try: and except: - Error handling
    ✓ template='plotly_dark' or template="plotly_dark" - Dark theme
    ```

    ### D. NUMBER FORMATTING AUDIT
    ```
    ✓ Function exists: format_large_number or similar
    ✓ Function handles billions (B suffix)
    ✓ Function handles millions (M suffix)
    ✓ Function handles None/NaN gracefully
    ✓ All st.metric values use formatting function
    ✓ No raw integers > 1000 displayed to user
    ```

    ### E. UI/UX COMPLIANCE CHECK
    ```
    ✓ 4 tabs are implemented (Snapshot, Growth, Moat, Valuation)
    ✓ Sidebar contains ticker input
    ✓ At least 4 metric cards displayed
    ✓ Company name/header is displayed
    ✓ Charts have titles
    ✓ Dark theme is applied
    ```

    ### F. DATA HANDLING VERIFICATION
    ```
    ✓ yf.Ticker() is used correctly
    ✓ Multiple data types fetched (financials, balance_sheet, cashflow)
    ✓ history() is called for price data
    ✓ Error handling wraps yfinance calls
    ✓ Invalid ticker scenario is handled
    ```

    ### G. CHART QUALITY CHECK
    For each chart, verify:
    ```
    ✓ Uses Plotly (go.Figure or make_subplots)
    ✓ Has a title
    ✓ Has template='plotly_dark'
    ✓ Has reasonable height (400-600)
    ✓ Uses st.plotly_chart with use_container_width=True
    ```

    ## 📊 REPORT FORMAT

    Generate a detailed QA report structured as:

    ```
    ═══════════════════════════════════════════════════════
    📋 VALUEINVESTOR PRO - QA REPORT
    ═══════════════════════════════════════════════════════
    
    A. IMPORT AUDIT
       [PASS/FAIL] - Details...
    
    B. FORBIDDEN PATTERNS
       [PASS/FAIL] - Details...
    
    C. REQUIRED PATTERNS  
       [PASS/FAIL] - Details...
    
    D. NUMBER FORMATTING
       [PASS/FAIL] - Details...
    
    E. UI/UX COMPLIANCE
       [PASS/FAIL] - Details...
    
    F. DATA HANDLING
       [PASS/FAIL] - Details...
    
    G. CHART QUALITY
       [PASS/FAIL] - Details...
    
    ═══════════════════════════════════════════════════════
    ISSUES FOUND: X
    ═══════════════════════════════════════════════════════
    1. [Line XX] Issue description - Recommended fix
    2. ...
    
    ═══════════════════════════════════════════════════════
    FINAL VERDICT: ✅ APPROVED / ❌ REJECTED
    ═══════════════════════════════════════════════════════
    ```

    ## 🚨 CRITICAL FAILURES (Auto-Reject)
    If ANY of these are found, the code is REJECTED:
    1. st.bar_chart or st.line_chart used
    2. No Plotly imports
    3. No number formatting function
    4. No error handling
    5. Less than 4 tabs implemented

    ## ✅ APPROVAL CRITERIA
    The code is APPROVED only if:
    - All 7 sections pass
    - Zero critical failures
    - All 4 tabs are functional
    - Professional dark theme applied
    - All numbers properly formatted

    Read the 'app.py' file and generate the complete QA report.
    """,
    expected_output="""A comprehensive QA Report containing:
    1. Section-by-section PASS/FAIL results (A through G)
    2. Specific line numbers for any issues found
    3. Detailed description of each issue
    4. Recommended fix for each issue
    5. Total issue count
    6. Final verdict: APPROVED FOR PRODUCTION or REJECTED WITH REASONS
    7. If rejected, prioritized list of fixes needed""",
    agent=qa_engineer
)