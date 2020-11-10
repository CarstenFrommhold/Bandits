import streamlit as st
import numpy as np
import pandas as pd

st.header("Expected Distributions of Bandits")
st.sidebar.subheader("Select Image")


prediction = st.sidebar.selectbox(
    "Model", options=["Image Similarity", 'Color Similarity']
)
td_no = st.sidebar.number_input(
    min_value=1710, max_value=150525, value=96782, label="TD No"
)
go = st.sidebar.button("GO")

# slider_options = st.select_slider(1,10)
counter = 0
if go & (prediction == "Image Similarity"):
    counter += 1
    st.subheader('works like a charm')
    st.text(str(counter))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)