import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Human Development Index 2021 (HDI)")
st.write("Oleh Watermelon group")
st.write("# Introduction")

"""
pendahuluan
"""

#reading the data
df = pd.read_csv("data/HDI.csv")
#df = pd.read_csv('data file HDI dataset')

#Getting an overview of the data.
st.write("## 5 data pertama")
st.write( df.head() )

