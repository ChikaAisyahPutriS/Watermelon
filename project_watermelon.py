import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title("WORLD HAPPINESS")
st.write("Oleh Watermelon")
st.write("# Introduction")

"""
pendahuluan
"""

#reading the data
df = pd.read_csv("")
#df = pd.read_csv('data file HDI dataset')

#Getting an overview of the data.
st.write("## 5 data pertama")
st.write( df.head() )

