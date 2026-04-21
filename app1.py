import streamlit as st
import pandas as pd
#import plotly.express as px


st.title("Cric Info App")


def load_data(file_path):
    df=pd.read_csv(file_path)
    return df

data_path=("./Newcricinfo.csv")    

df=load_data(data_path)

#st.dataframe(df)

country_match=df.groupby("country")["Matches"].sum().sort_values().reset_index()

st.sidebar.header("Filters")
country=st.sidebar.multiselect("Select  country",options=df["country"].unique(),default=df["country"].unique())
duration=st.sidebar.slider("Select Range",df["Duration"].min(),df["Duration"].max())
#player=st.sidebar.multiselect()

filtered_df=df[
    (df["country"].isin(country))
]
st.dataframe(filtered_df)

#Metric is a key performance indidcator
total_runs=filtered_df["Runs"].sum()
total_matches=filtered_df["Matches"].sum()
total_hundreds=filtered_df["100"].sum()
total_sixes=filtered_df["6s"].sum()
total_player=filtered_df["Player"].nunique()

col1,col2,col3,col4,col5=st.columns(5)
with col1:
    st.metric(label="Total Runs",value=total_runs)
with col2:    
    st.metric(label="Matches",value=total_matches)
with col3:    
    st.metric(label="Total Hundreds",value=total_hundreds)
with col4:    
    st.metric(label="Total Sixes",value=total_sixes)
with col5:    
    st.metric(label="Total Players",value=total_player)





#fig_country=px.pie(
    country_match,
    names="country",
    values="Matches",
    title="Country Wise Matches"
)

#st.plotly_chart(fig_country)

bar_country=px.bar(
country_match,
x="country",
y="Matches",
title="Country Wise MAtches In Bar"

)

#st.plotly_chart(bar_country)
