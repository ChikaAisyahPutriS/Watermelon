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
dfhdi = pd.read_csv( 'data/HDI_dataset.csv' )
#df = pd.read_csv('data file HDI_dataset')

#Getting an overview of the data. 
dfhdi.head()