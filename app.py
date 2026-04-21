#pip install streamlit 
#pip plotly 
#pip pandas
# To run the app, use the command: streamlit run app.py

import streamlit as st
import pandas as pd
import plotly.express as px     
st.title("Ecommerce Sales Analysis Dashboard")

#st.dataframe(data)

def load_data(file_path):
    df=pd.read_csv(file_path)
    df["Date"]=pd.to_datetime(df["Date"],errors="coerce")
    df=df.dropna(subset=["Date"])
    df["Branch"]=df["Branch"].replace("A","Myammar")
    df["Branch"]=df["Branch"].replace("B","Singapore")
    df["Branch"]=df["Branch"].replace("C","Thailand")
    return df
data_path="./supermarket_sales.csv"

df = load_data(data_path) 
#st.dataframe(df) 

st.sidebar.header("Filters")

select_branch=st.sidebar.multiselect("Select Branch",options=df["Branch"].unique(),default=df["Branch"].unique())
select_city=st.sidebar.multiselect("Select City",options=df["City"].unique(),default=df["City"].unique())
select_gender=st.sidebar.multiselect("Select Gender",options=df["Gender"].unique(),default=df["Gender"].unique())
select_product_line=st.sidebar.multiselect("Select Product Line",options=df["Product line"].unique())

filtered_data=df[
    (df["Branch"].isin(select_branch)) &
    (df["City"].isin(select_city)) &
    (df["Gender"].isin(select_gender)) &
    (df["Product line"].isin(select_product_line)) 
]
st.dataframe(filtered_data)

total_sales=filtered_data["Total"].sum().round(3)
total_quantity=filtered_data["Quantity"].sum()
avg_cogs=filtered_data["cogs"].mean().round(3)
avg_rating=filtered_data["Rating"].mean()
n_customers=filtered_data["Invoice ID"].nunique()
st.metric(label="Total Sales", value=total_sales)
st.metric(label="Total Quantity", value=total_quantity)
st.metric(label="Average COGS", value=avg_cogs)
st.metric(label="Average Rating", value=avg_rating)
st.metric(label="Customer Count", value=n_customers)
