# ============================================================
# AI PERSONALIZED FASHION SHOPPING ASSISTANT
# COMPLETE STREAMLIT APPLICATION - 5 PAGES
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

from sentence_transformers import SentenceTransformer
import faiss


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Personalized Fashion Shopping Assistant",
    page_icon="👗",
    layout="wide"
)


# ============================================================
# FILE PATHS
# ============================================================

CURRENT_FOLDER = Path(__file__).parent

FASHION_FILE = CURRENT_FOLDER / "fashion_sales.csv"
PRODUCT_FILE = CURRENT_FOLDER / "product_data.csv"
RAG_FILE = CURRENT_FOLDER / "rag_product_data.csv"
FAISS_FILE = CURRENT_FOLDER / "faiss_index.index"


# If files are not inside Ecommerce_Dashboard,
# also check the parent folder

if not PRODUCT_FILE.exists():
    PRODUCT_FILE = CURRENT_FOLDER.parent / "product_data.csv"

if not RAG_FILE.exists():
    RAG_FILE = CURRENT_FOLDER.parent / "rag_product_data.csv"

if not FAISS_FILE.exists():
    FAISS_FILE = CURRENT_FOLDER.parent / "faiss_index.index"


# ============================================================
# LOAD FASHION SALES DATA
# ============================================================

@st.cache_data
def load_fashion_data():

    return pd.read_csv(FASHION_FILE)


fashion_sales = load_fashion_data()


# Convert order date

fashion_sales["order_date"] = pd.to_datetime(
    fashion_sales["order_date"],
    errors="coerce"
)


# ============================================================
# CREATE PRICE RANGE IF NEEDED
# ============================================================

if "price_range" not in fashion_sales.columns:

    fashion_sales["price_range"] = pd.cut(
        fashion_sales["item_price"],
        bins=[0, 50, 200, 500, float("inf")],
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

    return None


product_data = load_product_data()


# ============================================================
# LOAD RAG DATA
# ============================================================

@st.cache_data
def load_rag_data():

    if RAG_FILE.exists():

        return pd.read_csv(RAG_FILE)

    return None


# ============================================================
# LOAD SENTENCE TRANSFORMER MODEL
# ============================================================

@st.cache_resource
def load_embedding_model():

    return SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )


# ============================================================
# LOAD FAISS VECTOR DATABASE
# ============================================================

@st.cache_resource
def load_vector_index():

    if FAISS_FILE.exists():

        return faiss.read_index(
            str(FAISS_FILE)
        )

    return None


# ============================================================
# RAG RETRIEVAL FUNCTION
# ============================================================

def retrieve_products(
    query,
    embedding_model,
    vector_index,
    rag_product_data,
    k=3
):

    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, indices = vector_index.search(
        query_embedding.astype("float32"),
        k=k
    )

    retrieved_products = rag_product_data.iloc[
        indices[0]
    ].copy()

    return retrieved_products


# ============================================================
# RAG ANSWER FUNCTION
# ============================================================

def create_rag_answer(
    query,
    retrieved_products
):

    results = retrieved_products.copy()

    question = query.lower()

    # --------------------------------------------------------
    # PRODUCT TYPE FILTERING
    # --------------------------------------------------------

    product_types = [
        "jeans",
        "jacket",
        "jackets",
        "shirt",
        "shirts",
        "t-shirt",
        "t-shirts",
        "dress",
        "dresses",
        "hoodie",
        "hoodies"
    ]

    for product_type in product_types:

        if product_type in question:

            matching = results[
                results["product_type"]
                .astype(str)
                .str.lower()
                .str.contains(
                    product_type.replace("s", ""),
                    na=False
                )
            ]

            if not matching.empty:

                results = matching

            break


    # --------------------------------------------------------
    # AFFORDABLE / BUDGET
    # --------------------------------------------------------

    if (
        "affordable" in question
        or "cheap" in question
        or "budget" in question
    ):

        budget_results = results[
            results["item_price"] <= 100
        ]

        if not budget_results.empty:

            results = budget_results


    # --------------------------------------------------------
    # HIGH RATINGS / GOOD REVIEWS
    # --------------------------------------------------------

    if (
        "high rating" in question
        or "highly rated" in question
        or "best rated" in question
        or "good reviews" in question
        or "best reviews" in question
    ):

        results = results.sort_values(
            [
                "product_rating",
                "positive_review_percentage"
            ],
            ascending=False
        )


    # --------------------------------------------------------
    # POSITIVE SENTIMENT
    # --------------------------------------------------------

    if (
        "positive sentiment" in question
        or "positive customer sentiment" in question
        or "positive reviews" in question
    ):

        results = results.sort_values(
            "average_sentiment_score",
            ascending=False
        )


    # --------------------------------------------------------
    # FINAL SORT
    # --------------------------------------------------------

    results = results.sort_values(
        [
            "product_rating",
            "positive_review_percentage",
            "average_sentiment_score"
        ],
        ascending=False
    )


    best_product = results.iloc[0]


    answer = f"""
### Recommended Product

Based on your request, I recommend:

**Product ID:** {best_product['product_id']}

**Brand:** {best_product['brand']}

**Product Type:** {best_product['product_type']}

**Price:** ${best_product['item_price']:.2f}

**Price Range:** {best_product['price_range']}

**Product Rating:** {best_product['product_rating']:.2f}

**Positive Review Percentage:** {best_product['positive_review_percentage']:.1f}%

**Average Customer Sentiment Score:** {best_product['average_sentiment_score']:.2f}

This product was selected from the products retrieved
from the vector database based on its relevance to your question
and its product, rating, sentiment, and review information.
"""

    return answer


# ============================================================
# MAIN TITLE
# ============================================================

st.title("👗 AI Personalized Fashion Shopping Assistant")

st.markdown("""
This application combines **Fashion Business Analytics,
Transformer-Based Sentiment Analysis, Machine Learning,
K-Means Clustering, AI Product Recommendations,
LLM-based interaction, and Retrieval-Augmented Generation (RAG)**.
""")


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("🧭 Navigation")


page = st.sidebar.radio(

    "Choose a Page",

    [
        "📊 Business Analytics",
        "🧠 NLP & Sentiment Analysis",
        "🤖 AI Recommendation System",
        "💬 AI Fashion Chatbot",
        "🔍 RAG Fashion Assistant"
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


    # --------------------------------------------------------
    # SIDEBAR FILTERS
    # --------------------------------------------------------

    st.sidebar.subheader("🔍 Filter Data")


    selected_brand = st.sidebar.selectbox(

        "Select Brand",

        ["All"] +
        sorted(
            fashion_sales["brand"]
            .dropna()
            .unique()
            .tolist()
        )
    )


    selected_gender = st.sidebar.selectbox(

        "Select Gender",

        ["All"] +
        sorted(
            fashion_sales["gender"]
            .dropna()
            .unique()
            .tolist()
        )
    )


    selected_product_type = st.sidebar.selectbox(

        "Select Product Type",

        ["All"] +
        sorted(
            fashion_sales["product_type"]
            .dropna()
            .unique()
            .tolist()
        )
    )


    # --------------------------------------------------------
    # APPLY FILTERS
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # KPI CALCULATIONS
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # KPI DISPLAY
    # --------------------------------------------------------

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


    st.markdown("---")


    # --------------------------------------------------------
    # REVENUE BY BRAND
    # --------------------------------------------------------

    brand_revenue = (
        filtered_data
        .groupby("brand")["item_total"]
        .sum()
        .reset_index()
        .sort_values(
            "item_total",
            ascending=False
        )
    )


    fig_brand = px.bar(

        brand_revenue,

        x="brand",

        y="item_total",

        title="Revenue by Brand"
    )


    st.plotly_chart(
        fig_brand,
        use_container_width=True
    )


    # --------------------------------------------------------
    # MONTHLY REVENUE
    # --------------------------------------------------------

    filtered_data["month"] = (
        filtered_data["order_date"]
        .dt
        .to_period("M")
        .astype(str)
    )


    monthly_revenue = (
        filtered_data
        .groupby("month")["item_total"]
        .sum()
        .reset_index()
    )


    fig_month = px.line(

        monthly_revenue,

        x="month",

        y="item_total",

        markers=True,

        title="Monthly Revenue Trend"
    )


    st.plotly_chart(
        fig_month,
        use_container_width=True
    )


    # --------------------------------------------------------
    # TOP PRODUCTS
    # --------------------------------------------------------

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

        title="Top 10 Best-Selling Products"
    )


    st.plotly_chart(
        fig_products,
        use_container_width=True
    )


    # --------------------------------------------------------
    # DOWNLOAD DATA
    # --------------------------------------------------------

    st.download_button(

        "📥 Download Filtered Data",

        filtered_data.to_csv(
            index=False
        ),

        "filtered_fashion_sales.csv",

        "text/csv"
    )


# ============================================================
# ============================================================
# PAGE 2
# NLP & SENTIMENT ANALYSIS
# ============================================================
# ============================================================

elif page == "🧠 NLP & Sentiment Analysis":

    st.header("🧠 AI & NLP Product Intelligence")


    if product_data is None:

        st.error(
            "product_data.csv was not found."
        )

    else:

        st.write("""
        This section combines Transformer-based sentiment analysis
        and K-Means clustering to provide AI-enhanced
        product intelligence.
        """)


        col1, col2, col3, col4 = st.columns(4)


        col1.metric(
            "📦 Products",
            len(product_data)
        )


        col2.metric(
            "⭐ Avg Rating",
            f"{product_data['product_rating'].mean():.2f}"
        )


        col3.metric(
            "😊 Avg Positive Reviews",
            f"{product_data['positive_review_percentage'].mean():.1f}%"
        )


        col4.metric(
            "🧩 Clusters",
            product_data["cluster"].nunique()
        )


        st.markdown("---")


        # ----------------------------------------------------
        # SENTIMENT VS RATING
        # ----------------------------------------------------

        fig_sentiment = px.scatter(

            product_data,

            x="average_sentiment_score",

            y="product_rating",

            color="cluster",

            size="total_reviews",

            hover_data=[
                "product_id",
                "brand",
                "product_type"
            ],

            title="Customer Sentiment vs Product Rating"
        )


        st.plotly_chart(
            fig_sentiment,
            use_container_width=True
        )


        # ----------------------------------------------------
        # POSITIVE REVIEW ANALYSIS
        # ----------------------------------------------------

        top_reviews = (
            product_data
            .sort_values(
                "positive_review_percentage",
                ascending=False
            )
            .head(10)
        )


        fig_reviews = px.bar(

            top_reviews,

            x="product_id",

            y="positive_review_percentage",

            color="brand",

            title="Top Products by Positive Review Percentage"
        )


        st.plotly_chart(
            fig_reviews,
            use_container_width=True
        )


        # ----------------------------------------------------
        # CLUSTER ANALYSIS
        # ----------------------------------------------------

        if "cluster" in product_data.columns:

            cluster_counts = (
                product_data["cluster"]
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

                title="Distribution of Products Across Clusters"
            )


            st.plotly_chart(
                fig_cluster,
                use_container_width=True
            )


        st.subheader(
            "📋 AI-Enhanced Product Data"
        )


        st.dataframe(
            product_data,
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
        "🤖 AI Personalized Fashion Recommendation System"
    )


    if product_data is None:

        st.error(
            "product_data.csv was not found."
        )

    else:

        st.write("""
        Select your preferences and receive AI-based fashion
        recommendations using product ratings, customer sentiment,
        positive reviews, and product information.
        """)


        col1, col2 = st.columns(2)


        with col1:

            selected_brand = st.selectbox(

                "Preferred Brand",

                ["All"] +
                sorted(
                    product_data["brand"]
                    .dropna()
                    .unique()
                    .tolist()
                ),

                key="recommendation_brand"
            )


        with col2:

            selected_type = st.selectbox(

                "Preferred Product Type",

                ["All"] +
                sorted(
                    product_data["product_type"]
                    .dropna()
                    .unique()
                    .tolist()
                ),

                key="recommendation_type"
            )


        selected_price = st.selectbox(

            "Preferred Price Range",

            ["All"] +
            sorted(
                product_data["price_range"]
                .dropna()
                .unique()
                .tolist()
            ),

            key="recommendation_price"
        )


        recommendations = product_data.copy()


        if selected_brand != "All":

            recommendations = recommendations[
                recommendations["brand"]
                == selected_brand
            ]


        if selected_type != "All":

            recommendations = recommendations[
                recommendations["product_type"]
                == selected_type
            ]


        if selected_price != "All":

            recommendations = recommendations[
                recommendations["price_range"]
                == selected_price
            ]


        # ----------------------------------------------------
        # HANDLE MISSING VALUES
        # ----------------------------------------------------

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


        # ----------------------------------------------------
        # AI RECOMMENDATION SCORE
        # ----------------------------------------------------

        recommendations["rating_score"] = (
            recommendations["product_rating"] / 5
        )


        recommendations["sentiment_score"] = (
            recommendations[
                "average_sentiment_score"
            ] + 1
        ) / 2


        recommendations["positive_score"] = (
            recommendations[
                "positive_review_percentage"
            ] / 100
        )


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


        st.subheader(
            "⭐ Top AI Product Recommendations"
        )


        top_recommendations = (
            recommendations.head(10)
        )


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


        fig_recommendation = px.bar(

            top_recommendations,

            x="product_id",

            y="recommendation_score",

            color="brand",

            title="Top AI Recommended Products"
        )


        st.plotly_chart(
            fig_recommendation,
            use_container_width=True
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


    st.write("""
    Ask questions about fashion products and receive
    recommendations based on the available product information.
    """)


    st.info("""
Examples:

• Recommend affordable jeans with good reviews

• Show highly rated jackets

• Recommend products with positive customer sentiment

• Which products have the best customer reviews?

• Recommend premium clothing with high ratings
""")


    user_question = st.text_area(
        "Ask your fashion question:",
        key="chatbot_question"
    )


    if st.button(
        "Ask AI Chatbot",
        key="chatbot_button"
    ):

        if user_question.strip():

            results = product_data.copy()

            question = user_question.lower()


            # PRODUCT TYPE DETECTION

            for product_type in [
                "jeans",
                "jacket",
                "shirt",
                "dress",
                "hoodie"
            ]:

                if product_type in question:

                    matching = results[
                        results["product_type"]
                        .astype(str)
                        .str.lower()
                        .str.contains(
                            product_type,
                            na=False
                        )
                    ]

                    if not matching.empty:

                        results = matching

                    break


            # AFFORDABLE

            if (
                "affordable" in question
                or "cheap" in question
                or "budget" in question
            ):

                affordable = results[
                    results["item_price"] <= 100
                ]

                if not affordable.empty:

                    results = affordable


            # PREMIUM

            if "premium" in question:

                premium = results[
                    results["item_price"] >= 200
                ]

                if not premium.empty:

                    results = premium


            # POSITIVE SENTIMENT

            if (
                "positive sentiment" in question
                or "positive reviews" in question
            ):

                results = results.sort_values(
                    "average_sentiment_score",
                    ascending=False
                )


            # BEST REVIEWS

            results = results.sort_values(

                [
                    "product_rating",
                    "positive_review_percentage",
                    "average_sentiment_score"
                ],

                ascending=False
            )


            results = results.head(5)


            best_product = results.iloc[0]


            st.subheader(
                "🤖 AI Fashion Assistant Response"
            )


            st.success(
                f"""
I recommend the following product based on your question:

**Product ID:** {best_product['product_id']}

**Brand:** {best_product['brand']}

**Product Type:** {best_product['product_type']}

**Price:** ${best_product['item_price']:.2f}

**Price Range:** {best_product['price_range']}

**Product Rating:** {best_product['product_rating']:.2f}

**Positive Review Percentage:** {best_product['positive_review_percentage']:.1f}%

**Average Customer Sentiment Score:** {best_product['average_sentiment_score']:.2f}

This recommendation was generated using product characteristics,
customer ratings, sentiment analysis, and review information.
"""
            )


            st.subheader(
                "📦 Related Product Recommendations"
            )


            st.dataframe(

                results[
                    [
                        "product_id",
                        "brand",
                        "product_type",
                        "price_range",
                        "item_price",
                        "product_rating",
                        "positive_review_percentage",
                        "average_sentiment_score"
                    ]
                ],

                use_container_width=True
            )


        else:

            st.warning(
                "Please enter a question."
            )


# ============================================================
# ============================================================
# PAGE 5
# RAG FASHION ASSISTANT
# ============================================================
# ============================================================

elif page == "🔍 RAG Fashion Assistant":

    st.header(
        "🔍 RAG-Powered Fashion Shopping Assistant"
    )


    st.write("""
    This page demonstrates a Retrieval-Augmented Generation (RAG)
    system using Sentence Transformer embeddings and a FAISS
    vector database.
    """)


    st.markdown("""

""")


    st.info("""
Example questions:

• Recommend affordable jeans with good customer reviews

• Show highly rated jackets

• Which products have the best customer sentiment?

• Recommend premium clothing with high ratings
""")


    user_question = st.text_area(
        "Ask the RAG Fashion Assistant:",
        key="rag_question"
    )


    if st.button(
        "🔍 Ask RAG Assistant",
        key="rag_button"
    ):

        if user_question.strip():

            rag_product_data = load_rag_data()


            if rag_product_data is None:

                st.error("""
rag_product_data.csv was not found.

Please make sure it is inside your
Ecommerce_Dashboard folder.
""")

            else:

                try:

                    with st.spinner(
                        "Searching the FAISS vector database..."
                    ):

                        embedding_model = (
                            load_embedding_model()
                        )


                        vector_index = (
                            load_vector_index()
                        )


                        if vector_index is None:

                            st.error("""
faiss_index.index was not found.

Please make sure the FAISS vector database
file is inside your Ecommerce_Dashboard folder.
""")

                        else:

                            retrieved_products = (
                                retrieve_products(

                                    user_question,

                                    embedding_model,

                                    vector_index,

                                    rag_product_data,

                                    k=3
                                )
                            )


                            answer = create_rag_answer(

                                user_question,

                                retrieved_products
                            )


                            st.subheader(
                                "🤖 RAG Fashion Assistant Response"
                            )


                            st.success(
                                answer
                            )


                            st.subheader(
                                "📦 Products Retrieved from Vector Database"
                            )


                            st.caption("""
These products were retrieved using semantic search
from the FAISS vector database.
""")


                            display_columns = [

                                "product_id",

                                "brand",

                                "product_type",

                                "price_range",

                                "item_price",

                                "product_rating",

                                "average_sentiment_score",

                                "positive_review_percentage",

                                "total_reviews",

                                "cluster"
                            ]


                            available_columns = [

                                column

                                for column in display_columns

                                if column
                                in retrieved_products.columns
                            ]


                            st.dataframe(

                                retrieved_products[
                                    available_columns
                                ],

                                use_container_width=True
                            )


                except Exception as e:

                    st.error(
                        f"RAG system error: {e}"
                    )


        else:

            st.warning(
                "Please enter a question."
            )