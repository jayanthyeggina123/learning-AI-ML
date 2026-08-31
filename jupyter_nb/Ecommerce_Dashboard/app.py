# ============================================================
# AI PERSONALIZED FASHION SHOPPING ASSISTANT
# COMPLETE STREAMLIT APPLICATION
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Personalized Fashion Shopping Assistant",
    page_icon=" ",
    layout="wide"
)


# ============================================================
# FILE PATHS
# ============================================================

CURRENT_FOLDER = Path(__file__).parent

FASHION_FILE = CURRENT_FOLDER / "fashion_sales.csv"

PRODUCT_FILE = CURRENT_FOLDER / "product_data.csv"


# If product_data.csv is not inside Ecommerce_Dashboard,
# try the parent folder

if not PRODUCT_FILE.exists():
    PRODUCT_FILE = CURRENT_FOLDER.parent / "product_data.csv"


# ============================================================
# LOAD FASHION SALES DATA
# ============================================================

@st.cache_data
def load_fashion_data():

    return pd.read_csv(FASHION_FILE)


fashion_sales = load_fashion_data()


# Convert date

fashion_sales["order_date"] = pd.to_datetime(
    fashion_sales["order_date"],
    errors="coerce"
)


# ============================================================
# CREATE PRICE RANGE IF NEEDED
# ============================================================

if "price_range" not in fashion_sales.columns:

    price_column = "item_price"

    if "price" in fashion_sales.columns:
        price_column = "price"

    fashion_sales["price_range"] = pd.cut(
        fashion_sales[price_column],
        bins=[
            0,
            50,
            200,
            500,
            float("inf")
        ],
        labels=[
            "Budget ($0-$50)",
            "Mid Range ($50-$200)",
            "Premium ($200-$500)",
            "Luxury ($500+)"
        ]
    )


# ============================================================
# LOAD PRODUCT DATA
# ============================================================

@st.cache_data
def load_product_data():

    if PRODUCT_FILE.exists():

        return pd.read_csv(PRODUCT_FILE)

    else:

        return None


product_data = load_product_data()


# ============================================================
# MAIN TITLE
# ============================================================

st.title("👗 AI Personalized Fashion Shopping Assistant")

st.markdown(
    """
    This application combines Fashion Business Analytics,
    Transformer-Based Sentiment Analysis, AI Product Recommendation,
    and an Interactive Fashion Assistant.
    """
)


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("Navigation")


page = st.sidebar.radio(

    "Choose a Page",

    [
        "📊 Business Analytics",
        "🧠 NLP & Sentiment Analysis",
        "🤖 AI Recommendation System",
        "💬 AI Fashion Chatbot"
    ]
)


# ============================================================
# ============================================================
# PAGE 1
# BUSINESS ANALYTICS
# ============================================================
# ============================================================

if page == "📊 Business Analytics":

    st.header("📊 Fashion Business Analytics Dashboard")


    # ========================================================
    # SIDEBAR FILTERS
    # ========================================================

    st.sidebar.subheader("🔍 Filter Data")


    selected_brand = st.sidebar.selectbox(

        "Select Brand",

        ["All"] + sorted(
            fashion_sales["brand"]
            .dropna()
            .unique()
            .tolist()
        )
    )


    selected_gender = st.sidebar.selectbox(

        "Select Gender",

        ["All"] + sorted(
            fashion_sales["gender"]
            .dropna()
            .unique()
            .tolist()
        )
    )


    selected_product_type = st.sidebar.selectbox(

        "Select Product Type",

        ["All"] + sorted(
            fashion_sales["product_type"]
            .dropna()
            .unique()
            .tolist()
        )
    )


    # ========================================================
    # APPLY FILTERS
    # ========================================================

    filtered_data = fashion_sales.copy()


    if selected_brand != "All":

        filtered_data = filtered_data[
            filtered_data["brand"] == selected_brand
        ]


    if selected_gender != "All":

        filtered_data = filtered_data[
            filtered_data["gender"] == selected_gender
        ]


    if selected_product_type != "All":

        filtered_data = filtered_data[
            filtered_data["product_type"]
            == selected_product_type
        ]


    # ========================================================
    # KPI CALCULATIONS
    # ========================================================

    total_revenue = (
        filtered_data["item_total"]
        .sum()
    )


    total_orders = (
        filtered_data["order_id"]
        .nunique()
    )


    total_customers = (
        filtered_data["user_id"]
        .nunique()
    )


    average_order_value = (

        filtered_data
        .groupby("order_id")["item_total"]
        .sum()
        .mean()
    )


    average_rating = (

        filtered_data["product_rating"]
        .mean()
    )


    # ========================================================
    # KPI DISPLAY
    # ========================================================

    st.subheader("📈 Key Performance Indicators")


    col1, col2, col3, col4, col5 = st.columns(5)


    col1.metric(
        "💰 Revenue",
        f"${total_revenue:,.2f}"
    )


    col2.metric(
        "🛒 Orders",
        total_orders
    )


    col3.metric(
        "👥 Customers",
        total_customers
    )


    col4.metric(
        "📦 Avg Order Value",
        f"${average_order_value:,.2f}"
    )


    col5.metric(
        "⭐ Avg Rating",
        f"{average_rating:.2f}"
    )


    # ========================================================
    # REVENUE BY BRAND
    # ========================================================

    st.subheader("💰 Revenue by Brand")


    brand_revenue = (

        filtered_data
        .groupby("brand")["item_total"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


    fig_brand = px.bar(

        brand_revenue,

        x="brand",

        y="item_total",

        title="Revenue by Brand",

        labels={
            "brand": "Brand",
            "item_total": "Revenue"
        }
    )


    st.plotly_chart(
        fig_brand,
        use_container_width=True,
        key="brand_revenue_chart"
    )


    # ========================================================
    # MONTHLY REVENUE
    # ========================================================

    st.subheader("📈 Monthly Revenue Trend")


    monthly_revenue = (

        filtered_data
        .groupby(
            filtered_data["order_date"]
            .dt
            .to_period("M")
        )["item_total"]

        .sum()

        .reset_index()
    )


    monthly_revenue["order_date"] = (

        monthly_revenue["order_date"]
        .astype(str)
    )


    fig_month = px.line(

        monthly_revenue,

        x="order_date",

        y="item_total",

        markers=True,

        title="Monthly Revenue Trend"
    )


    st.plotly_chart(
        fig_month,
        use_container_width=True,
        key="monthly_revenue_chart"
    )


    # ========================================================
    # TOP SELLING PRODUCTS
    # ========================================================

    st.subheader("🏆 Top 10 Best Selling Products")


    top_products = (

        filtered_data
        .groupby("product_name")["quantity"]
        .sum()

        .sort_values(
            ascending=False
        )

        .head(10)

        .reset_index()
    )


    fig_products = px.bar(

        top_products,

        x="product_name",

        y="quantity",

        title="Top 10 Best Selling Products"
    )


    st.plotly_chart(
        fig_products,
        use_container_width=True,
        key="top_products_chart"
    )


    # ========================================================
    # REVENUE BY GENDER
    # ========================================================

    st.subheader("👥 Revenue by Gender")


    gender_revenue = (

        filtered_data
        .groupby("gender")["item_total"]
        .sum()
        .reset_index()
    )


    fig_gender = px.pie(

        gender_revenue,

        names="gender",

        values="item_total",

        title="Revenue by Gender"
    )


    st.plotly_chart(
        fig_gender,
        use_container_width=True,
        key="gender_revenue_chart"
    )


    # ========================================================
    # SALES BY PRICE RANGE
    # ========================================================

    st.subheader("💵 Product Sales by Price Range")


    price_sales = (

        filtered_data
        .groupby(
            "price_range",
            observed=False
        )["quantity"]

        .sum()

        .reset_index()
    )


    fig_price = px.bar(

        price_sales,

        x="price_range",

        y="quantity",

        title="Product Sales by Price Range"
    )


    st.plotly_chart(
        fig_price,
        use_container_width=True,
        key="price_range_chart"
    )


    # ========================================================
    # CUSTOMER PREFERRED BRANDS
    # ========================================================

    st.subheader("❤️ Customer Preferred Brands")


    preferred_brands = (

        filtered_data
        .groupby("brand")["user_id"]

        .nunique()

        .sort_values(
            ascending=False
        )

        .head(10)

        .reset_index()
    )


    fig_preferred = px.bar(

        preferred_brands,

        x="brand",

        y="user_id",

        title="Top Brands Preferred by Customers"
    )


    st.plotly_chart(
        fig_preferred,
        use_container_width=True,
        key="preferred_brands_chart"
    )


    # ========================================================
    # CUSTOMER PURCHASE FREQUENCY
    # ========================================================

    st.subheader("🔁 Customer Purchase Frequency")


    purchase_frequency = (

        filtered_data
        .groupby("user_id")["order_id"]

        .nunique()

        .reset_index()
    )


    fig_frequency = px.histogram(

        purchase_frequency,

        x="order_id",

        nbins=10,

        title="Customer Purchase Frequency Distribution"
    )


    st.plotly_chart(
        fig_frequency,
        use_container_width=True,
        key="purchase_frequency_chart"
    )


    # ========================================================
    # TOP CUSTOMERS
    # ========================================================

    st.subheader("🏆 Top Customers by Spending")


    top_customers = (

        filtered_data
        .groupby("user_id")["item_total"]

        .sum()

        .sort_values(
            ascending=False
        )

        .head(10)

        .reset_index()
    )


    fig_customers = px.bar(

        top_customers,

        x="user_id",

        y="item_total",

        title="Top Customers by Spending"
    )


    st.plotly_chart(
        fig_customers,
        use_container_width=True,
        key="top_customers_chart"
    )


    # ========================================================
    # DOWNLOAD DATA
    # ========================================================

    st.subheader("📥 Download Filtered Data")


    csv = filtered_data.to_csv(
        index=False
    )


    st.download_button(

        label="Download Filtered Fashion Data",

        data=csv,

        file_name="filtered_fashion_sales.csv",

        mime="text/csv"
    )



# ============================================================
# ============================================================
# PAGE 2
# NLP & SENTIMENT ANALYSIS
# ============================================================
# ============================================================

elif page == "🧠 NLP & Sentiment Analysis":

    st.header("🧠 NLP & Transformer-Based Sentiment Analysis")


    st.write(
        """
        This page displays customer review sentiment analysis
        generated using a Transformer-based DistilBERT model.
        """
    )


    if product_data is None:

        st.error(
            "product_data.csv was not found."
        )

        st.stop()


    # ========================================================
    # SENTIMENT KPIs
    # ========================================================

    st.subheader("📊 Sentiment Overview")


    avg_sentiment = (

        product_data[
            "average_sentiment_score"
        ]
        .mean()
    )


    avg_positive = (

        product_data[
            "positive_review_percentage"
        ]
        .mean()
    )


    total_reviews = (

        product_data[
            "total_reviews"
        ]
        .sum()
    )


    sentiment_col1, sentiment_col2, sentiment_col3 = (
        st.columns(3)
    )


    sentiment_col1.metric(

        "😊 Average Sentiment",

        f"{avg_sentiment:.3f}"
    )


    sentiment_col2.metric(

        "👍 Positive Reviews",

        f"{avg_positive:.1f}%"
    )


    sentiment_col3.metric(

        "📝 Total Reviews",

        f"{total_reviews:,.0f}"
    )


    # ========================================================
    # SENTIMENT BY BRAND
    # ========================================================

    st.subheader(
        "😊 Average Sentiment by Brand"
    )


    brand_sentiment = (

        product_data
        .groupby("brand")[
            "average_sentiment_score"
        ]

        .mean()

        .sort_values(
            ascending=False
        )

        .reset_index()
    )


    fig_brand_sentiment = px.bar(

        brand_sentiment,

        x="brand",

        y="average_sentiment_score",

        title="Average Customer Sentiment by Brand"
    )


    st.plotly_chart(

        fig_brand_sentiment,

        use_container_width=True,

        key="brand_sentiment_chart"
    )


    # ========================================================
    # SENTIMENT BY PRODUCT TYPE
    # ========================================================

    st.subheader(
        "👕 Average Sentiment by Product Type"
    )


    product_type_sentiment = (

        product_data
        .groupby("product_type")[
            "average_sentiment_score"
        ]

        .mean()

        .sort_values(
            ascending=False
        )

        .reset_index()
    )


    fig_product_sentiment = px.bar(

        product_type_sentiment,

        x="product_type",

        y="average_sentiment_score",

        title="Customer Sentiment by Product Type"
    )


    st.plotly_chart(

        fig_product_sentiment,

        use_container_width=True,

        key="product_type_sentiment_chart"
    )


    # ========================================================
    # POSITIVE REVIEW PERCENTAGE
    # ========================================================

    st.subheader(
        "👍 Positive Review Percentage by Product"
    )


    positive_products = (

        product_data

        .sort_values(
            "positive_review_percentage",
            ascending=False
        )

        .head(10)
    )


    fig_positive = px.bar(

        positive_products,

        x="product_id",

        y="positive_review_percentage",

        color="brand",

        title="Top Products by Positive Review Percentage"
    )


    st.plotly_chart(

        fig_positive,

        use_container_width=True,

        key="positive_reviews_chart"
    )


    # ========================================================
    # PRODUCT SENTIMENT TABLE
    # ========================================================

    st.subheader(
        "📋 Product-Level Sentiment Data"
    )


    st.dataframe(

        product_data[
            [
                "product_id",
                "brand",
                "product_type",
                "item_price",
                "product_rating",
                "average_sentiment_score",
                "positive_review_percentage",
                "total_reviews"
            ]
        ],

        use_container_width=True
    )



# ============================================================
# ============================================================
# PAGE 3
# AI RECOMMENDATION SYSTEM
# ============================================================
# ============================================================

elif page == "🤖 AI Recommendation System":

    st.header(
        "🤖 AI-Enhanced Fashion Recommendation System"
    )


    st.write(
        """
        The recommendation system uses product features including
        brand, product type, price, product rating, customer sentiment,
        positive review percentage, and machine learning clusters
        to recommend similar fashion products.
        """
    )


    if product_data is None:

        st.error(
            "product_data.csv was not found."
        )

        st.stop()


    # ========================================================
    # USER FILTERS
    # ========================================================

    st.subheader(
        "🔍 Select Your Fashion Preferences"
    )


    selected_brand_ai = st.selectbox(

        "Preferred Brand",

        ["All"] + sorted(
            product_data[
                "brand"
            ]
            .dropna()
            .unique()
            .tolist()
        ),

        key="ai_brand"
    )


    selected_type_ai = st.selectbox(

        "Preferred Product Type",

        ["All"] + sorted(
            product_data[
                "product_type"
            ]
            .dropna()
            .unique()
            .tolist()
        ),

        key="ai_product_type"
    )


    selected_price_ai = st.selectbox(

        "Preferred Price Range",

        ["All"] + sorted(
            product_data[
                "price_range"
            ]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        ),

        key="ai_price_range"
    )


    # ========================================================
    # APPLY RECOMMENDATION FILTERS
    # ========================================================

    recommendations = product_data.copy()


    if selected_brand_ai != "All":

        recommendations = recommendations[
            recommendations["brand"]
            == selected_brand_ai
        ]


    if selected_type_ai != "All":

        recommendations = recommendations[
            recommendations["product_type"]
            == selected_type_ai
        ]


    if selected_price_ai != "All":

        recommendations = recommendations[
            recommendations["price_range"]
            .astype(str)
            == selected_price_ai
        ]


    # ========================================================
    # CREATE AI RECOMMENDATION SCORE
    # ========================================================

    recommendations = recommendations.copy()


    # Fill missing values

    recommendations[
        "average_sentiment_score"
    ] = (
        recommendations[
            "average_sentiment_score"
        ]
        .fillna(0)
    )


    recommendations[
        "positive_review_percentage"
    ] = (
        recommendations[
            "positive_review_percentage"
        ]
        .fillna(0)
    )


    recommendations[
        "product_rating"
    ] = (
        recommendations[
            "product_rating"
        ]
        .fillna(0)
    )


    # Normalize rating

    recommendations["rating_score"] = (

        recommendations[
            "product_rating"
        ] / 5
    )


    # Normalize sentiment

    recommendations["sentiment_score"] = (

        recommendations[
            "average_sentiment_score"
        ] + 1
    ) / 2


    # Normalize positive reviews

    recommendations["positive_score"] = (

        recommendations[
            "positive_review_percentage"
        ] / 100
    )


    # FINAL AI SCORE

    recommendations[
        "recommendation_score"
    ] = (

        0.40
        * recommendations["rating_score"]

        +

        0.35
        * recommendations["sentiment_score"]

        +

        0.25
        * recommendations["positive_score"]
    )


    recommendations = (

        recommendations

        .sort_values(
            "recommendation_score",
            ascending=False
        )
    )


    # ========================================================
    # DISPLAY TOP RECOMMENDATIONS
    # ========================================================

    st.subheader(
        "⭐ Top AI Product Recommendations"
    )


    top_recommendations = (

        recommendations
        .head(10)
    )


    if len(top_recommendations) == 0:

        st.warning(
            "No products found for the selected preferences."
        )

    else:

        st.dataframe(

            top_recommendations[
                [
                    "product_id",
                    "brand",
                    "product_type",
                    "price_range",
                    "item_price",
                    "product_rating",
                    "average_sentiment_score",
                    "positive_review_percentage",
                    "recommendation_score"
                ]
            ],

            use_container_width=True
        )


        # ====================================================
        # RECOMMENDATION VISUALIZATION
        # ====================================================

        fig_recommendation = px.bar(

            top_recommendations,

            x="product_id",

            y="recommendation_score",

            color="brand",

            title="Top AI Recommended Fashion Products"
        )


        st.plotly_chart(

            fig_recommendation,

            use_container_width=True,

            key="recommendation_chart"
        )


    # ========================================================
    # CLUSTER ANALYSIS
    # ========================================================

    if "cluster" in product_data.columns:


        st.subheader(
            "🧩 Machine Learning Product Clusters"
        )


        cluster_counts = (

            product_data[
                "cluster"
            ]
            .value_counts()
            .reset_index()
        )


        cluster_counts.columns = [

            "Cluster",

            "Number of Products"
        ]


        fig_cluster = px.bar(

            cluster_counts,

            x="Cluster",

            y="Number of Products",

            title="Distribution of Products Across AI Clusters"
        )


        st.plotly_chart(

            fig_cluster,

            use_container_width=True,

            key="cluster_chart"
        )



# ============================================================
# ============================================================
# PAGE 4
# AI FASHION CHATBOT
# ============================================================
# ============================================================

elif page == "💬 AI Fashion Chatbot":

    st.header(
        "💬 AI Fashion Shopping Assistant"
    )


    st.write(
        """
        Ask questions about fashion products, brands, product types,
        prices, ratings, customer sentiment, and recommendations.
        """
    )


    if product_data is None:

        st.error(
            "product_data.csv was not found."
        )

        st.stop()


    # ========================================================
    # INITIALIZE CHAT HISTORY
    # ========================================================

    if "messages" not in st.session_state:

        st.session_state.messages = []


    # ========================================================
    # DISPLAY CHAT HISTORY
    # ========================================================

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.write(
                message["content"]
            )


    # ========================================================
    # USER INPUT
    # ========================================================

    user_question = st.chat_input(
        "Ask about fashion products..."
    )


    if user_question:


        # Display user question

        with st.chat_message("user"):

            st.write(user_question)


        st.session_state.messages.append(

            {
                "role": "user",
                "content": user_question
            }
        )


        # ====================================================
        # BASIC DATA-DRIVEN CHATBOT LOGIC
        # ====================================================

        question = user_question.lower()


        response = ""


        # ----------------------------------------------------
        # BEST RATED PRODUCTS
        # ----------------------------------------------------

        if (
            "best rated" in question
            or "highest rated" in question
        ):

            best_products = (

                product_data

                .sort_values(
                    "product_rating",
                    ascending=False
                )

                .head(5)
            )


            response = (
                "Here are the highest-rated fashion products:\n\n"
            )


            for _, row in best_products.iterrows():

                response += (

                    f"• Product ID: {row['product_id']} | "
                    f"Brand: {row['brand']} | "
                    f"Type: {row['product_type']} | "
                    f"Rating: {row['product_rating']:.2f}\n"
                )


        # ----------------------------------------------------
        # POSITIVE SENTIMENT
        # ----------------------------------------------------

        elif (
            "positive" in question
            or "sentiment" in question
        ):

            best_sentiment = (

                product_data

                .sort_values(
                    "positive_review_percentage",
                    ascending=False
                )

                .head(5)
            )


            response = (
                "These products have strong positive customer sentiment:\n\n"
            )


            for _, row in best_sentiment.iterrows():

                response += (

                    f"• {row['product_id']} | "
                    f"{row['brand']} | "
                    f"{row['product_type']} | "
                    f"Positive Reviews: "
                    f"{row['positive_review_percentage']:.1f}%\n"
                )


        # ----------------------------------------------------
        # BRAND QUESTIONS
        # ----------------------------------------------------

        elif "brand" in question:

            brand_summary = (

                product_data
                .groupby("brand")[
                    "product_rating"
                ]

                .mean()

                .sort_values(
                    ascending=False
                )

                .head(5)
            )


            response = (
                "Top brands based on average product rating:\n\n"
            )


            for brand, rating in brand_summary.items():

                response += (

                    f"• {brand}: "
                    f"{rating:.2f} average rating\n"
                )


        # ----------------------------------------------------
        # PRODUCT RECOMMENDATION
        # ----------------------------------------------------

        elif (
            "recommend" in question
            or "recommendation" in question
        ):

            recommended = (

                product_data

                .sort_values(
                    [
                        "product_rating",
                        "positive_review_percentage"
                    ],

                    ascending=False
                )

                .head(5)
            )


            response = (
                "Based on ratings and customer sentiment, "
                "I recommend these products:\n\n"
            )


            for _, row in recommended.iterrows():

                response += (

                    f"• {row['product_id']} | "
                    f"{row['brand']} | "
                    f"{row['product_type']} | "
                    f"Rating: {row['product_rating']:.2f}\n"
                )


        # ----------------------------------------------------
        # DEFAULT RESPONSE
        # ----------------------------------------------------

        else:

            response = (
                "I can help you explore the fashion dataset. "
                "Try asking questions such as:\n\n"
                "• What are the best rated products?\n"
                "• Which products have positive sentiment?\n"
                "• Which brands perform best?\n"
                "• Recommend some fashion products.\n"
                "• Show me products with high customer ratings."
            )


        # ====================================================
        # DISPLAY AI RESPONSE
        # ====================================================

        with st.chat_message("assistant"):

            st.write(response)


        st.session_state.messages.append(

            {
                "role": "assistant",
                "content": response
            }
        )