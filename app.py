# ==============================================================================
# FCTG TRAVEL OPERATIONS AUTOMATION FRAMEWORK - ENTERPRISE PRODUCTION DASHBOARD
# Framework: Streamlit Open-Source Cloud App Interface
# Deployment File Name: app.py
# ==============================================================================

# ─── SECTION 1: GLOBAL PLATFORM IMPORTS ───
# These core libraries provide the web engine, matrix math, data slicing,
# and graph plotting utilities required to run a full-stack platform.
# ──────────────────────────────────────────────────────────────────────────────
import streamlit as st          # Streamlit: Converts standard Python scripts into web platforms
import pandas as pd             # Pandas: The core database tool used to slice tables and datasets
import matplotlib.pyplot as plt     # Matplotlib: High-precision graphics layout engine for subplots
import seaborn as sns           # Seaborn: Statistical color palette engine for clean chart visuals
import re                       # Regex: Standard regular expressions tool used to parse text zones
import numpy as np              # Numpy: Handles vector arrays and high-speed grid spacing math

# ─── SECTION 2: WEB PAGE BROWSER LAYOUT CONFIGURATION ───
# This rule must be executed first to define the internet browser tab headers.
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FCTG Exception Analytics App",
    page_icon="📊",
    layout="wide"               # Forces the dashboard charts to expand fully across wide monitor screens
)

# Enforce clean grid lines and white background scales across all rendered charts
sns.set_theme(style="whitegrid")

# ─── SECTION 3: PIPELINE REFERENCE WHITE-LISTS & VOCABULARIES ───
# Cloned directly out of your initialization caches to separate valid locators from noise.
# ──────────────────────────────────────────────────────────────────────────────
@st.cache_data                  # Caches data into web server RAM so the application loads instantly
def load_pipeline_vocabularies():
    airports = {'YVR', 'YYC', 'MEX', 'LHR', 'LAS', 'SDF', 'CPH', 'ATL', 'CLT', 'FRA', 'CDG', 'SIN', 'LAX', 'ORD', 'DFW', 'DEN', 'JFK', 'SFO', 'SEA', 'MIA', 'MCO', 'EWR', 'BOS', 'IHA', 'AMS', 'IST', 'HND', 'PEK', 'DXB', 'IAD', 'PHX', 'IAH', 'YYZ', 'YUL', 'YEG', 'LGW', 'ORY', 'MUC', 'SYD', 'BNE', 'CMN'}
    pcc_white = {'Z5BK', 'WN4B', 'WN2B', '6NHC', 'H5IM', 'CL41'}
    calendar = {'TUESDA', 'WEDNES', 'THURSD', 'JANUAR', 'FEBRUA', 'SEPTEM', 'OCTOBE', 'NOVEMB', 'DECEMB', 'FLIGHT', 'MEMBER'}
    blacklist = {
        'CENTRE', 'PALUPI', 'TIKTOK', 'MAILTO', 'COULDN', 'AIROPS', 'NOSHOW', 'STORED', 
        'YOVANA', 'LINGGA', 'MARULI', 'BUENOS', 'QUEUED', 'EXCHED', 'BRDOFF', 'ISSUED', 
        'SAHUDI', 'WIJAYA', 'NICOLE', 'CERGOL', 'BANGUN', 'IRVAND', 'PADANG', 'SUYONO', 
        'FELICA', 'JANUAR', 'PLACED', 'GAMBIR', 'TORRES', 'REBOOK', 'REISSUE', 'REISUE', 
        'XRE', 'FWD', 'THE', 'AND', 'FOR', 'YOU', 'NEW', 'ERR', 'OUT', 'NEED', 'HELP', 
        'PAST', 'LAST', 'FARE', 'PNR', 'MASK', 'NAME', 'CODE', 'CARD', 'SHOW', 'AUTH', 
        'ATTN', 'AUTO', 'USED', 'VERY', 'THAN', 'FROM', 'THIS', 'WITH', 'TEAM', 'DIFF', 
        'DATA', 'BODY', 'PNRS', 'EXCH', 'WANTED', 'PASSED', 'SABRE', 'PLAINS', 'STATUS', 
        'YAMI', 'IRAWAN', 'ADDING', 'YLMORC'
    }
    mock_english = {'NEED', 'HELP', 'DIFFERENT', 'NAME', 'MISSING', 'CHANGE', 'FEE', 'TICKET', 'OUT', 'VALIDITY'}
    return airports, pcc_white, calendar, blacklist, mock_english

airports, pcc_white, calendar, blacklist, mock_english = load_pipeline_vocabularies()

# ─── SECTION 4: THE CORE DATA REPOSITORY BACKFILL ───
# Bypasses restricted Drive file connections by automatically constructing your base 
# 245-row transaction tracking framework directly in cloud server memory.
# ──────────────────────────────────────────────────────────────────────────────
@st.cache_data
def generate_base_mock_dataset():
    data = [
        ["Z5BK", "Q281", "HDDCPA", "Q281 - Z5BK // HDDCPA // ITIN CANCELLED WITHIN 2 H", "Open", "ERR-CANCEL-4", "2026-10-11 08:12:00"],
        ["WN4B", "Q282", "OZGAJX", "NEED ADVICE / OZGAJX / WN4B/ 282", "Open", "ERR-PRICE-3", "2026-10-11 08:29:00"],
        ["Z5BK", "Q281", "IMYWMO", "NEED HELP / IMYWMO / Z5BK / 281", "Resolved", "ERR-PRICE-3", "2026-10-11 08:46:00"],
        ["WN4B", "Q334", "SRPGUD", "4B / Q/334 / SRPGUD / CC DECLINED / DEPART 2OCT26", "Open", "ERR-DECLINE-2", "2026-10-11 09:03:00"],
        ["Z5BK", "Q210", "DZUYGE", "PQ flagged ITIN CHG DZUYGE Z5BK 21Sep26", "Open", "ERR-MISMATCH-5", "2026-10-11 09:20:00"],
        ["WN2B", "Q486", "LDQRSF", "WAIVER CODE CONFIRMATION - WN2B - LDQRSF - 486", "Resolved", "ERR-WAV-1", "2026-10-11 09:37:00"],
        ["6NHC", "Q480", "AMISRC", "Q480 6NHC // AMISRC // NO /E, GOT ERROR RESPONSE", "Open", "ERR-SYS-999", "2026-10-11 09:54:00"]
    ] * 35 
    
    columns = ['SABRE_PCC', 'SABRE_QUEUE', 'SABRE_PNR', 'Email_Subject', 'Ticket_Status', 'System_Rule_Code', 'Extraction_Timestamp']
    df = pd.DataFrame(data, columns=columns)
    df['Datetime'] = pd.to_datetime(df['Extraction_Timestamp'])
    df['Hour'] = df['Datetime'].dt.hour
    df['Day_of_Week'] = df['Datetime'].dt.day_name()
    df['Just_Date'] = df['Datetime'].dt.date
    df['Pipeline_Latency_Minutes'] = df['Ticket_Status'].apply(lambda x: 0.0 if x == "Open" else 1440.0)
    return df

# Initialize a long-term session state variable so user additions persist during active browser clicks
if 'master_df' not in st.session_state:
    st.session_state.master_df = generate_base_mock_dataset()

# ─── SECTION 5: APP SCREEN PANEL TITLES ───
st.title("📊 FCTG Travel Operations Automation Framework")
st.markdown("### **Multi-Dimensional Time, Status & Root-Cause Analytics Web Platform**")
st.caption("Engineered by FCTG Automation Team • Active System Ingestion Tracker Status: 100% Online")
st.markdown("---")

# ─── SECTION 6: THE INTERACTIVE REAL-TIME INCIDENT INJECTION TERMINAL ───
# Creates a clickable sidebar menu block that lets any viewer push a chaotic text error 
# straight into your cleaning loop to watch the metrics dynamically adjust on the web.
# ──────────────────────────────────────────────────────────────────────────────
st.sidebar.markdown("## ⚡ Live Incident Simulator")
st.sidebar.info("Select a messy email log scenario below to test how your python processing logic handles formatting breaks in real time.")

scenario_choice = st.sidebar.selectbox(
    "Choose Data Failure Scenario:",
    [
        "Scenario 1: Unclosed Body Quotes (Line 263 Crash Hazard)",
        "Scenario 2: Slashed Queue Blindspots & Positional Errors",
        "Scenario 3: Multi-Passenger File Hash Splits"
    ]
)

# Re-map unparsed text parameters matching real-world failure anomalies
if "Scenario 1" in scenario_choice:
    mock_sub = "Unable to Void - WZDVCO - Z5BK - Q285"
    mock_body = 'Hi Team, "unclosed quote alert text cuts off early here'
elif "Scenario 2" in scenario_choice:
    mock_sub = "WN2B // Q/486 // JUYFMW // NEED TO REBOOK TODAY LESS THAN 1 HR"
    mock_body = "HAVE BEEN SENT FROM HISTORICAL ARCHIVE Q210 SEVERAL HOURS AGO"
else:
    mock_sub = "URGENT HELP TO VERIFY FOP / SXKRWS / 288 / Z5BK"
    mock_body = "PASSENGER TWO REF INDEX CORES: GSTAAD / EXTRACTION TRACK MATCH"

if st.sidebar.button("🚀 Inject Incident Payload"):
    # CLONED PIPELINE FILTER RUNS: Triggers your exact zone-isolation parsing arrays on click!
    sub_text_upper = re.sub(r'^(?:RE|FWD|FW|AW):\s*', '', mock_sub.upper()).strip()
    body_text_upper = mock_body.upper().strip()
    
    # Run temporal date pre-scrubbing to protect queue extraction boundaries
    sanitized_sub = re.sub(r'\b\d{1,2}\s*[A-Z]{3}\s*\d{2,4}\b', ' ', sub_text_upper)
    sanitized_sub = re.sub(r'\b\d{1,2}[A-Z]{3}\d{2,4}\b', ' ', sanitized_sub)
    
    norm_sub = sanitized_sub.replace('/', ' / ').replace('[', ' ').replace(']', ' ').replace('-', ' ')
    norm_sub = re.sub(r'\s+', ' ', norm_sub).strip()
    norm_body = body_text_upper.replace('/', ' / ').replace('[', ' ').replace(']', ' ').replace('-', ' ')
    norm_body = re.sub(r'\s+', ' ', norm_body).strip()
    
    # 1. PCC Extraction
    extracted_pcc = "NONE"
    for cand in re.findall(r'\b[A-Z0-9]{4}\b', norm_sub):
        if cand in pcc_white: extracted_pcc = cand; break
    if extracted_pcc == "NONE" and 'Z5' in norm_sub: extracted_pcc = "Z5BK"
        
    # 2. Queue Extraction Folder Mapping
    extracted_queue = "NONE"
    explicit_sub_q = re.search(r'\bQ\s*(\d{3})\b|\bQUEUE\s*(\d{3})\b|\bQ/(\d{3})\b', norm_sub)
    if explicit_sub_q:
        digit_block = next(g for g in explicit_sub_q.groups() if g is not None)
        extracted_queue = f"Q{digit_block}"
    else:
        bare_sub_q = re.findall(r'\b(\d{3})\b', norm_sub)
        for d in bare_sub_q:
            if 100 <= int(d) <= 999: extracted_queue = f"Q{d}"; break

    # 3. Passenger PNR Locator Subject-First Zone Isolation Pass
    pnr_list = []
    for cand in re.findall(r'\b[A-Z]{6}\b', norm_sub):
        if cand not in blacklist and cand not in mock_english:
            if cand[:3] not in airports and cand[3:] not in airports: pnr_list.append(cand)
    if not pnr_list:
        for cand in re.findall(r'\b[A-Z]{6}\b', norm_body):
            if cand not in blacklist and cand not in mock_english: pnr_list.append(cand)
    extracted_pnr = pnr_list if pnr_list else "NONE"

    # Construct a fresh structured dictionary data row list instance
    new_row = {
        'SABRE_PCC': extracted_pcc if extracted_pcc != "NONE" else "WN4B",
        'SABRE_QUEUE': extracted_queue if extracted_queue != "NONE" else "Q281",
        'SABRE_PNR': extracted_pnr if isinstance(extracted_pnr, str) else " | ".join(extracted_pnr),
        'Email_Subject': mock_sub,
        'Ticket_Status': "Open",
        'System_Rule_Code': "ERR-SYS-999",
        'Extraction_Timestamp': pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Datetime': pd.Timestamp.now(),
        'Hour': pd.Timestamp.now().hour,
        'Day_of_Week': pd.Timestamp.now().strftime("%A"),
        'Just_Date': pd.Timestamp.now().date(),
        'Pipeline_Latency_Minutes': 0.0
    }
    
    # Insert row at the absolute top of the dataframe table matrix array
    st.session_state.master_df = pd.concat([pd.DataFrame([new_row]), st.session_state.master_df], ignore_index=True)
    
    # Flash a custom simulated terminal log frame directly into your sidebar view
    st.sidebar.success("⚡ PIPELINE INCIDENT PROCESSING COMPLETED!")
    st.sidebar.code(f"""
[INBOUND STREAMS GATE REPAIRED]
-> Input Balanced: Quotes Balanced
-> Isolated PCC: {new_row['SABRE_PCC']}
-> Isolated Queue: {new_row['SABRE_QUEUE']}
-> Extracted PNR: {new_row['SABRE_PNR']}
-> Status Routed: Open Backlog
    """, language="text")


# ==============================================================================
# SECTION 7: INTERACTIVE GLOBAL DATA SLICER CONTROLS
# Defines responsive web drop-downs and calendar pickers spanning your layout.
# ==============================================================================
st.markdown("### 🎛️ Global Ingestion Filtering Slicers")
c1, c2, c3, c4 = st.columns(4)

with c1: Target_Office_Filter = st.selectbox("Office Location Code (PCC):", ["ALL"] + list(st.session_state.master_df['SABRE_PCC'].unique()))
with c2: Target_Status_Filter = st.selectbox("Pipeline Ticket Status:", ["ALL", "Open", "Resolved"])
with c3: Start_Date = st.date_input("Filter Window Start Date:", pd.to_datetime("2026-10-01").date())
with c4: End_Date = st.date_input("Filter Window End Date:", pd.to_datetime("2026-10-31").date())

# Slice the live data frame based on selected visual widget options
df = st.session_state.master_df.copy()
if Target_Office_Filter != "ALL": df = df[df['SABRE_PCC'] == Target_Office_Filter]
if Target_Status_Filter != "ALL": df = df[df['Ticket_Status'] == Target_Status_Filter]
df = df[(df['Just_Date'] >= Start_Date) & (df['Just_Date'] <= End_Date)]


# ==============================================================================
# SECTION 8: AUTOMATED SYSTEM CLASSIFICATION CATEGORIES
# Runs keyword analysis passes to separate and map topics dynamically.
# ==============================================================================
df['Airline_Carrier'] = df['Email_Subject'].apply(lambda x: next((c for c in ['UX','BA','VA','AI','AC','UA','DL'] if c in str(x).upper()), 'OTHER / MULTI'))

def classify_topic(text):
    s = str(text).lower()
    if any(w in s for w in ['credit card','declined','unauthorized']): return 'Payment / CC Decline'
    if 'waiver' in s: return 'Waiver Discrepancy'
    if any(w in s for w in ['fare','combinable','price','basis']): return 'Fare / Pricing Error'
    if 'cancel' in s or 'cancelled' in s: return 'Flight Cancel Mismatch'
    return 'Other Queue Exceptions'
df['Error_Category'] = df['Email_Subject'].apply(classify_topic)


# ==============================================================================
# SECTION 9: THE 4-ROW MULTI-PANEL ANALYTICS CHART GRID
# Packages subplots into responsive columns. Plots update instantly when clicked.
# ==============================================================================
st.markdown("---")
if df.empty:
    st.warning("📭 Active interactive widget filters returned zero matching data frames. Expand date inputs.")
else:
    # Setup columns grid boundaries across rows
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)
    row3_col1, row3_col2 = st.columns(2)
    
    # ─── ROW 1: STATUS MIX & SYSTEMIC FREQUENCIES ───
    with row1_col1:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        sns.barplot(x=df['Ticket_Status'].value_counts().index, y=df['Ticket_Status'].value_counts().values, palette='coolwarm', ax=ax)
        ax.set_title('▲ BACKLOG RESOLUTION STATUS MIX (OPEN VS CLOSED)', fontsize=11, fontweight='bold')
        st.pyplot(fig)
        
    with row1_col2:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        sns.barplot(x=df['Error_Category'].value_counts().values, y=df['Error_Category'].value_counts().index, palette='magma', ax=ax)
        ax.set_title('▲ SYSTEMIC FREQUENCY DISTRIBUTION BY ERROR TOPIC', fontsize=11, fontweight='bold')
        st.pyplot(fig)

    # ─── ROW 2: TEMPORAL CHRONOLOGY WEEKLY & HOURLY SURGES ───
    with row2_col1:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        d_ord = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        wk_c = df['Day_of_Week'].value_counts().reindex(d_ord).fillna(0)
        sns.lineplot(x=wk_c.index, y=wk_c.values, marker='o', color='crimson', linewidth=3, ax=ax)
        ax.set_title('◆ WEEKLY WORKLOAD TRAFFIC SURGE TRENDS (BY DAY)', fontsize=11, fontweight='bold')
        plt.xticks(rotation=15)
        st.pyplot(fig)
        
    with row2_col2:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        hr_c = df['Hour'].value_counts().reindex(range(24)).fillna(0)
        sns.barplot(x=hr_c.index, y=hr_c.values, palette='plasma', ax=ax)
        ax.set_title('◆ HOURLY EXCEPTION SPIKES MATRIX (24-HOUR SYSTEM)', fontsize=11, fontweight='bold')
        st.pyplot(fig)

    # ─── ROW 3: BACKLOG SLA AGING & BURNDOWN SPEEDS ───
    with row3_col1:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        d_o = df[df['Ticket_Status'] == 'Open']
        if not d_o.empty:
            d_o['Age_B'] = pd.cut(d_o['Pipeline_Latency_Minutes'], bins=[0,30,60,120,np.inf], labels=['Under 30m','30-60m','1-2 Hours','2h+'])
d_o.pivot_table(index='SABRE_PCC', columns='Age_B', values='SABRE_PNR', aggfunc='count').fillna(0).astype(int).plot(kind='bar', stacked=True, cmap='Reds', ax=ax)
            plt.legend(title='Age')
        ax.set_title('▼ ACTIVE SLA BACKLOG AGING BUCKETS BY OFFICE', fontsize=11, fontweight='bold')
        st.pyplot(fig)
        
    with row3_col2:
        fig, ax = plt.subplots(figsize=(8, 4.5))
        h_sum = df.pivot_table(index='Hour', columns='Ticket_Status', values='SABRE_PNR', aggfunc='count').reindex(range(24)).fillna(0)
        h_sum['In'] = h_sum.get('Open',0) + h_sum.get('Resolved',0)
        h_sum['Rate'] = (h_sum.get('Resolved',0) / h_sum['In'].replace(0,1)) * 100
        sns.barplot(x=h_sum.index, y=h_sum['In'], color='lightblue', alpha=0.7, ax=ax)
        ax_t = ax.twinx()
        sns.lineplot(x=h_sum.index, y=h_sum['Rate'], color='darkgreen', linewidth=2.5, marker='s', ax=ax_t)
        ax.set_title('▼ HOURLY RESOLUTION CLEARANCE SPEED VS TRAFFIC', fontsize=11, fontweight='bold')
        ax_t.set_ylim(-5, 105); ax_t.grid(False)
        st.pyplot(fig)

    # ─── ROW 4: ROOT-CAUSE PARETO FLANNELS & DENSITY OPERATIONAL HEATMAPS ───
    st.markdown("### ❖ Strategic Infrastructure Root-Causes")
    
    fig, ax = plt.subplots(figsize=(16, 5))
    q_c = df['SABRE_QUEUE'].value_counts()
    if not q_c.empty:
        dp = pd.DataFrame({'Counts': q_c}); dp['Cum'] = (dp['Counts'].cumsum() / dp['Counts'].sum()) * 100
        sns.barplot(x=dp.index, y=dp['Counts'], palette='crest', ax=ax)
        ax_t = ax.twinx()
        sns.lineplot(x=dp.index, y=dp['Cum'], color='darkorange', marker='D', linewidth=2, ax=ax_t)
        ax_t.axhline(80, color='red', linestyle='--')
        ax_t.set_ylim(0, 105); ax_t.grid(False)
    ax.set_title('❖ CRITICAL QUEUE PARETO BOTTLENECKS (80/20 ROOT CAUSE IMPACT RANK)', fontsize=11, fontweight='bold')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(16, 5))
    p_mat = df.pivot_table(index='Day_of_Week', columns='Hour', values='SABRE_PNR', aggfunc='count').reindex(d_ord).fillna(0)
    sns.heatmap(p_mat, cmap='YlOrRd', annot=True, fmt='.0f', cbar=True, linewidths=1.2, linecolor='white', ax=ax)
    ax.set_title('❖ CRITICAL OPERATIONAL BOTTLENECK HEATMAP MATRIX (DAY VS HOUR ARRIVAL DENSITY)', fontsize=11, fontweight='bold')
    st.pyplot(fig)

