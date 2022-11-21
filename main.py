import streamlit as st
import pandas as pd
import csv

st.title("""Alzheimer's Research""" )
st.markdown("[CSV in Google Sheets](https://docs.google.com/spreadsheets/d/155mUETVqN_IAsxMXwWSeJdDAFSAEgOX1kLGGJokHhVY/edit?usp=sharing)")

st.header("""Chosen Research Questions""")

st.write(""" 2)	Learning about the number of people who developed Alzheimer's at an unusually young age through outlier detection. Through outlier detection methodologies such as clustering, we can learn what could contributing factors could have potentially caused a small percentage of people from a younger age group to develop Alzheimer's. """)
st.write(""" 6)	For each year, we can create a plot of the data by gender, disease, race, or geographic location. By doing this, we can demonstrate how the rate of developing Alzheimer's disease for each group changes over time. If the rate for a particular group is positive, can predict that more people in that group will develop Alzheimer's disease in the future. On the contrary, if the rate for a particular group is negative, can predict that fewer people in that age group will develop Alzheimer's disease in the future.""")
st.info("""Choose One:""")
st.write(""" 7)	Creating a decision tree of the data to discover the non-intuitive relationships between Alzheimer’s disease, the different groups of patients based on their demographic information, and the different health conditions of the patients.""")
st.write(""" 3)	Predicting how likely it is for individuals with certain underlying conditions to develop Alzheimer’s disease by using association analysis. From the data, it can be calculated how likely it is for someone with Alzheimer’s to also suffer from other health problems. We can compare and contrast how mental health, diet, smoking, drugs and alcohol, obesity, cancer, and diabetes influence the development of Alzheimer’s disease and determine the correlation between them. The association rules that are uncovered can then be visualized. """)

df = pd.read_csv("alz.csv", usecols = ["Class", "Topic", "Question", "High_Confidence_Limit", "Stratification1"], low_memory=False)
list1 = []
topicList =[]
questionList = []
classList = (df['Class'].unique())
topicList = (df['Topic'].unique())
questionList = (df['Question'].unique())
overall = []
fifty64 = []
sixtyFiveOlder = []
listAllAgeGroups = []
listAllHighConfidenceLimit = []
listAllHighConfidenceLimit = (df["High_Confidence_Limit"])
listAllAgeGroups = (df["Stratification1"])

# sort list of all high confidence into their respective age group list
for i in range(len(listAllHighConfidenceLimit)): 
    if listAllAgeGroups[i] == 'Overall':
        overall.append(listAllHighConfidenceLimit[i])
    
    if listAllAgeGroups[i] == '50-64 years':
        fifty64.append(listAllHighConfidenceLimit[i])
        
    if listAllAgeGroups[i] == '65 years or older':
        sixtyFiveOlder.append(listAllHighConfidenceLimit[i])
        

# puts all lists into a dataframe, drops all null values
df1 = pd.DataFrame(list(zip(overall, fifty64, sixtyFiveOlder)), columns= ['Overall', "50-64", "65 or older"])
# to do: fix not dropping null values
df1.dropna()
print(df1)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Class")
    st.write(classList)

with col2:
    st.header("Topics")
    st.write(topicList)

with col3:
    st.header("Questions")
    st.write(questionList)
