"""
E-commerce Market Intelligence & Recommendation System
Enhanced UI with Modern Design, Animations, and Professional Styling
"""

import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import random

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="E-commerce Market Intelligence",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# ENHANCED CSS STYLING
# ============================================================================

st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main Container */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Custom Header */
    .main-header {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: fadeInDown 1s ease-in-out;
    }
    
    .sub-header {
        font-size: 1.2rem;
        color: #6c757d;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 500;
        animation: fadeInUp 1s ease-in-out;
    }
    
    /* Animated Gradient Metric Box */
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        animation: scaleIn 0.5s ease-in-out;
        position: relative;
        overflow: hidden;
    }
    
    .metric-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: rgba(255, 255, 255, 0.1);
        transform: rotate(45deg);
        transition: all 0.5s ease;
    }
    
    .metric-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
    }
    
    .metric-box:hover::before {
        left: 100%;
    }
    
    .metric-value {
        font-size: 3rem;
        font-weight: 800;
        margin: 0.5rem 0;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    .metric-label {
        font-size: 1.1rem;
        font-weight: 600;
        opacity: 0.95;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .metric-description {
        font-size: 0.9rem;
        opacity: 0.85;
        margin-top: 0.5rem;
    }
    
    /* Insight Box */
    .insight-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .insight-box:hover {
        transform: translateX(5px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }
    
    .insight-box h4 {
        color: #2c3e50;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    .insight-box p {
        color: #495057;
        margin: 0.3rem 0;
        line-height: 1.6;
    }
    
    /* Recommendation Card */
    .recommendation-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
        margin: 1.5rem 0;
        border: 1px solid #e9ecef;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .recommendation-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 5px;
        height: 100%;
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .recommendation-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
    }
    
    .recommendation-card h4 {
        color: #2c3e50;
        font-weight: 700;
        font-size: 1.3rem;
        margin-bottom: 1rem;
        padding-left: 0.5rem;
    }
    
    /* Product Badge */
    .product-badge {
        display: inline-block;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.3rem;
    }
    
    .badge-success {
        background: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }
    
    .badge-warning {
        background: #fff3cd;
        color: #856404;
        border: 1px solid #ffeaa7;
    }
    
    .badge-info {
        background: #d1ecf1;
        color: #0c5460;
        border: 1px solid #bee5eb;
    }
    
    .badge-danger {
        background: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
    
    /* Profile Card */
    .profile-card {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border: 2px solid #667eea30;
        height: 100%;
        transition: all 0.3s ease;
    }
    
    .profile-card:hover {
        border-color: #667eea;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.2);
    }
    
    .profile-card h4 {
        color: #667eea;
        font-weight: 700;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .profile-item {
        display: flex;
        justify-content: space-between;
        padding: 0.5rem 0;
        border-bottom: 1px solid #e9ecef;
    }
    
    .profile-label {
        color: #6c757d;
        font-weight: 500;
    }
    
    .profile-value {
        color: #2c3e50;
        font-weight: 600;
    }
    
    /* Stats Card */
    .stats-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        text-align: center;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .stats-card:hover {
        border-color: #667eea;
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
    }
    
    .stats-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    .stats-number {
        font-size: 2rem;
        font-weight: 800;
        color: #2c3e50;
        margin: 0.5rem 0;
    }
    
    .stats-label {
        color: #6c757d;
        font-weight: 600;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stats-delta {
        color: #28a745;
        font-size: 0.9rem;
        font-weight: 600;
        margin-top: 0.3rem;
    }
    
    /* Progress Bar */
    .progress-bar-container {
        background: #e9ecef;
        border-radius: 10px;
        height: 30px;
        overflow: hidden;
        margin: 1rem 0;
        box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        transition: width 1s ease;
        box-shadow: 0 2px 5px rgba(102, 126, 234, 0.5);
    }
    
    /* Section Title */
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: #2c3e50;
        margin: 2rem 0 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .section-title::before {
        content: '';
        width: 5px;
        height: 2rem;
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        border-radius: 3px;
    }
    
    /* Divider */
    .custom-divider {
        height: 3px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, transparent 100%);
        margin: 2rem 0;
        border-radius: 3px;
    }
    
    /* Alert Boxes */
    .alert-success {
        background: #d4edda;
        color: #155724;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        animation: slideInRight 0.5s ease;
    }
    
    .alert-warning {
        background: #fff3cd;
        color: #856404;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        animation: slideInRight 0.5s ease;
    }
    
    .alert-info {
        background: #d1ecf1;
        color: #0c5460;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #17a2b8;
        margin: 1rem 0;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        animation: slideInRight 0.5s ease;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes scaleIn {
        from {
            opacity: 0;
            transform: scale(0.9);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Plotly Chart Styling */
    .js-plotly-plot {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
    }
    
    /* Dataframe Styling */
    .dataframe {
        border-radius: 10px !important;
        overflow: hidden;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Selectbox Styling */
    .stSelectbox > div > div {
        border-radius: 10px;
        border: 2px solid #e9ecef;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Tooltip */
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: help;
    }
    
    .tooltip:hover::after {
        content: attr(data-tooltip);
        position: absolute;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        background: #2c3e50;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        white-space: nowrap;
        font-size: 0.85rem;
        z-index: 1000;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

@st.cache_data(ttl=3600)
def load_survey_data():
    """Load or generate survey data with enhanced features"""
    try:
        df = pd.read_csv('survey_static.csv')
        return df
    except:
        indian_cities = [
            'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 
            'Kolkata', 'Pune', 'Ahmedabad', 'Jaipur', 'Surat',
            'Lucknow', 'Kanpur', 'Nagpur', 'Indore', 'Thane'
        ]
        
        keywords = [
            'phone', 'smartphone', 'charger', 'earbuds', 'headphones',
            'laptop', 'tablet', 'smartwatch', 'speaker', 'powerbank',
            'mouse', 'keyboard', 'monitor', 'webcam', 'router'
        ]
        
        names = [
            'Rajesh Kumar', 'Priya Sharma', 'Amit Patel', 'Sneha Gupta',
            'Vikram Singh', 'Anita Reddy', 'Rahul Mehta', 'Deepa Iyer',
            'Suresh Nair', 'Kavita Desai', 'Arun Kumar', 'Pooja Singh'
        ]
        
        data = []
        for i in range(200):
            price_low = random.choice([1000, 2000, 5000, 10000, 15000, 20000])
            data.append({
                'user_id': f'USER_{i+1:04d}',
                'name': random.choice(names),
                'age': random.randint(18, 65),
                'city': random.choice(indian_cities),
                'preferred_category': 'electronics',
                'expected_price_low': price_low,
                'expected_price_high': price_low + random.randint(2000, 15000),
                'favorite_keyword': random.choice(keywords)
            })
        return pd.DataFrame(data)

@st.cache_data(ttl=3600)
def fetch_api_products():
    """Fetch and expand products from API with error handling"""
    try:
        response = requests.get("https://fakestoreapi.com/products", timeout=10)
        products = response.json()
        
        electronics = [p for p in products if p.get('category') == 'electronics']
        
        expanded = []
        for product in electronics:
            expanded.append(product)
            for i in range(1, 35):
                variant = product.copy()
                variant['price'] = round(product['price'] * random.uniform(0.7, 1.5) * 83, 2)
                variant['id'] = f"{product['id']}_V{i}"
                variant['title'] = f"{product['title']} - Variant {i}"
                if 'rating' in variant:
                    variant['rating'] = variant['rating'].copy()
                    variant['rating']['rate'] = round(random.uniform(3.5, 5.0), 1)
                    variant['rating']['count'] = random.randint(50, 1000)
                expanded.append(variant)
        
        products_data = []
        for p in expanded:
            products_data.append({
                'product_id': str(p['id']),
                'title': p['title'],
                'price': p.get('price', 0),
                'category': p.get('category', 'electronics'),
                'rating': p.get('rating', {}).get('rate', 0),
                'rating_count': p.get('rating', {}).get('count', 0),
                'description': p.get('description', '')[:100]
            })
        
        return pd.DataFrame(products_data)
    
    except Exception as e:
        st.error(f"⚠️ Error fetching API data: {e}")
        return pd.DataFrame()

def calculate_score(price, rating, rating_count, user_price_low, user_price_high):
    """Calculate recommendation score with enhanced algorithm"""
    mid_price = (user_price_low + user_price_high) / 2
    price_distance = abs(price - mid_price) / mid_price if mid_price > 0 else 0
    price_penalty = price_distance * 2
    score = (rating * np.log1p(rating_count)) - price_penalty
    return score

def get_recommendations(user_row, df_products, top_n=5):
    """Get top N recommendations for a user"""
    if len(df_products) == 0:
        return pd.DataFrame()
    
    buffer = 0.2
    price_low = user_row['expected_price_low'] * (1 - buffer)
    price_high = user_row['expected_price_high'] * (1 + buffer)
    
    candidates = df_products[
        (df_products['price'] >= price_low) & 
        (df_products['price'] <= price_high)
    ].copy()
    
    if len(candidates) == 0:
        candidates = df_products.copy()
    
    candidates['score'] = candidates.apply(
        lambda row: calculate_score(
            row['price'], row['rating'], row['rating_count'],
            user_row['expected_price_low'], user_row['expected_price_high']
        ),
        axis=1
    )
    
    return candidates.nlargest(min(top_n, len(candidates)), 'score')

def calculate_metrics(df_survey, df_products):
    """Calculate all metrics with enhanced precision"""
    category_coverage = (df_survey['preferred_category'] == 'electronics').mean() * 100
    
    def check_price_match(row):
        matches = df_products[
            (df_products['price'] >= row['expected_price_low']) & 
            (df_products['price'] <= row['expected_price_high'])
        ]
        return len(matches) > 0
    
    df_survey['price_match'] = df_survey.apply(check_price_match, axis=1)
    price_accuracy = df_survey['price_match'].mean() * 100
    
    precision_1_keyword = []
    precision_3_keyword = []
    precision_1_price = []
    precision_3_price = []
    
    for _, user in df_survey.head(50).iterrows():
        recs = get_recommendations(user, df_products, 3)
        if len(recs) == 0:
            continue
        
        keyword = user['favorite_keyword'].lower()
        
        top_1 = int(keyword in recs.iloc[0]['title'].lower())
        precision_1_keyword.append(top_1)
        
        top_3 = sum([keyword in r['title'].lower() for _, r in recs.iterrows()])
        precision_3_keyword.append(top_3 / min(3, len(recs)))
        
        top_1_price = int(
            user['expected_price_low'] <= recs.iloc[0]['price'] <= user['expected_price_high']
        )
        precision_1_price.append(top_1_price)
        
        price_matches = sum([
            user['expected_price_low'] <= r['price'] <= user['expected_price_high']
            for _, r in recs.iterrows()
        ])
        precision_3_price.append(price_matches / min(3, len(recs)))
    
    return {
        'category_coverage': category_coverage,
        'price_accuracy': price_accuracy,
        'precision_1_keyword': np.mean(precision_1_keyword) * 100 if precision_1_keyword else 0,
        'precision_3_keyword': np.mean(precision_3_keyword) * 100 if precision_3_keyword else 0,
        'precision_1_price': np.mean(precision_1_price) * 100 if precision_1_price else 0,
        'precision_3_price': np.mean(precision_3_price) * 100 if precision_3_price else 0
    }

# ============================================================================
# LOAD DATA
# ============================================================================

with st.spinner("🔄 Loading data..."):
    df_survey = load_survey_data()
    df_products = fetch_api_products()
    
    if len(df_products) == 0:
        st.error("⚠️ Failed to load product data. Please refresh the page.")
        st.stop()
    
    metrics = calculate_metrics(df_survey, df_products)

# ============================================================================
# HEADER
# ============================================================================

st.markdown('<div class="main-header">🛒 E-commerce Market Intelligence System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">📊 Demand vs Supply Analysis | 🌐 Real-time API Integration | 🎯 Smart Recommendations</div>', unsafe_allow_html=True)

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.markdown("## 📊 Dashboard Controls")
    st.markdown("---")
    
    st.markdown("### 📈 Quick Stats")
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #667eea15, #764ba215); padding: 1rem; border-radius: 10px; margin-bottom: 1rem;'>
        <div style='display: flex; justify-content: space-between; margin: 0.5rem 0;'>
            <span style='color: #6c757d;'>📊 Survey Records:</span>
            <span style='font-weight: 700; color: #2c3e50;'>{len(df_survey)}</span>
        </div>
        <div style='display: flex; justify-content: space-between; margin: 0.5rem 0;'>
            <span style='color: #6c757d;'>📦 Market Products:</span>
            <span style='font-weight: 700; color: #2c3e50;'>{len(df_products)}</span>
        </div>
        <div style='display: flex; justify-content: space-between; margin: 0.5rem 0;'>
            <span style='color: #6c757d;'>🕐 Last Updated:</span>
            <span style='font-weight: 700; color: #2c3e50; font-size: 0.8rem;'>{datetime.now().strftime('%I:%M %p')}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🎯 Navigation")
    
    page = st.radio(
        "",
        ["📊 Overview", "📈 Metrics Dashboard", "🎁 Recommendations", "💼 Business Insights", "📋 Data Explorer"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("""
    <div style='font-size: 0.85rem; color: #6c757d; line-height: 1.6;'>
    This intelligent system analyzes customer demand from surveys and compares it with real-time market supply to generate actionable business insights and personalized recommendations.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔗 Quick Links")
    st.markdown("""
    <div style='font-size: 0.85rem;'>
    <a href='#' style='color: #667eea; text-decoration: none;'>📖 Documentation</a><br>
    <a href='#' style='color: #667eea; text-decoration: none;'>🐙 GitHub Repo</a><br>
    <a href='#' style='color: #667eea; text-decoration: none;'>📧 Support</a>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PAGE: OVERVIEW
# ============================================================================

if page == "📊 Overview":
    st.markdown('<div class="section-title">📊 System Overview</div>', unsafe_allow_html=True)
    
    # Enhanced Metric Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-icon">👥</div>
            <div class="stats-number">{len(df_survey)}</div>
            <div class="stats-label">Total Customers</div>
            <div class="stats-delta">▲ +200 Records</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-icon">📦</div>
            <div class="stats-number">{len(df_products)}</div>
            <div class="stats-label">Market Products</div>
            <div class="stats-delta">▲ +{len(df_products)} Variants</div>
        </div>
        """, unsafe_allow_html=True)


    with col3:
        avg_budget = df_survey['expected_price_high'].mean()
        st.markdown(f"""
        <div class="stats-card">
            <div class="stats-icon">💰</div>
            <div class="stats-number">₹{avg_budget:,.0f}</div>
            <div class="stats-label">Avg Budget</div>
            <div class="stats-delta">▲ Stable Trends</div>
        </div>
        """, unsafe_allow_html=True)

        
        
    

