import streamlit as st
import pandas as pd

st.title("""Alzheimer's Research""" )
st.header("""Chosen Research Questions""")

st.info(""" 2)	Learning about the number of people who developed Alzheimer's at an unusually young age through outlier detection. Through outlier detection methodologies such as clustering, we can learn what could contributing factors could have potentially caused a small percentage of people from a younger age group to develop Alzheimer's. """)
st.info(""" 6)	For each year, we can create a plot of the data by gender, disease, race, or geographic location. By doing this, we can demonstrate how the rate of developing Alzheimer's disease for each group changes over time. If the rate for a particular group is positive, can predict that more people in that group will develop Alzheimer's disease in the future. On the contrary, if the rate for a particular group is negative, can predict that fewer people in that age group will develop Alzheimer's disease in the future.""")
st.header("""Choose One:""")
st.info(""" 7)	Creating a decision tree of the data to discover the non-intuitive relationships between Alzheimer’s disease, the different groups of patients based on their demographic information, and the different health conditions of the patients.""")
st.info(""" 3)	Predicting how likely it is for individuals with certain underlying conditions to develop Alzheimer’s disease by using association analysis. From the data, it can be calculated how likely it is for someone with Alzheimer’s to also suffer from other health problems. We can compare and contrast how mental health, diet, smoking, drugs and alcohol, obesity, cancer, and diabetes influence the development of Alzheimer’s disease and determine the correlation between them. The association rules that are uncovered can then be visualized. """)