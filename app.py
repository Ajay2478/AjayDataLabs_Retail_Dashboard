import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AjayDataLabs | Sales Insights", layout="wide")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("sales_data.csv")

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Results")
region = st.sidebar.multiselect("Select Region:", options=df["Region"].unique(), default=df["Region"].unique())
category = st.sidebar.multiselect("Select Category:", options=df["Product_Category"].unique(), default=df["Product_Category"].unique())

df_selection = df.query("Region == @region & Product_Category == @category")

# Main Page
st.title("📈 Retail Performance Dashboard")
st.markdown("##")

# Top Metrics
total_sales = int(df_selection["Sales"].sum())
avg_profit = round(df_selection["Profit"].mean(), 2)

left_col, right_col = st.columns(2)
with left_col:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with right_col:
    st.subheader("Average Profit per Sale:")
    st.subheader(f"US $ {avg_profit}")

st.markdown("---")

# Charts
sales_by_category = df_selection.groupby(by=["Product_Category"]).sum()[["Sales"]]
fig_sales = px.bar(sales_by_category, x=sales_by_category.index, y="Sales", title="Sales by Category", template="plotly_white")

sales_by_date = df_selection.groupby(by=["Date"]).sum()[["Sales"]]
fig_time = px.line(sales_by_date, x=sales_by_date.index, y="Sales", title="Revenue Trend Over Time")

c1, c2 = st.columns(2)
c1.plotly_chart(fig_sales, use_container_width=True)
c2.plotly_chart(fig_time, use_container_width=True)