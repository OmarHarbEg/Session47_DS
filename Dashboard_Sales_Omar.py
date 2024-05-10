
import streamlit as st 
import pandas as pd
import plotly.express as px

df = pd. read_csv("Sales_Store_Preprocessed.csv" )
df ["Year"] = df[ "Year"].astype(str)
st. title("Sales_Store_Analysis")

c1, c2 , c3 = st. columns (3)
with c1 :
    st.metric(label="Total Sales in M$" , value=(df["Sales"]. sum() / 1000000). round (3))
with c2:
    st. metric(label="Total Profit in K$" , value=(df[ "Profit"]. sum() / 1000). round (3))
with c3:
    st.metric(label="Avg Discount Percentage Per Year %" , value=(15.5) , delta="2%")

coll, col2 = st. columns (2)
with coll:
    st. header ("Sales By Categories")
    fig = px.histogram(data_frame=df , y ="Sales", x="Category" , histfunc='sum',width=450 ,text_auto=True)
    st. plotly_chart(fig)
with col2:
    st. header ("Sales By Year")
    fig_2 = px. histogram(data_frame=df, x ="Year", y ="Sales" , histfunc='sum' ,width=550, text_auto=True)
    st. plotly_chart(fig_2)

st.header ("Profit Per Month")
df_month = df.groupby ("Month").sum()[["Profit", "Sales" ]]. reset_index()
fig_3 = px.line(data_frame= df_month,x= "Month", y=["Profit","Sales"] ,width=900)
st.plotly_chart(fig_3)
