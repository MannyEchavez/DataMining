import streamlit as st # pip install streamlit
import pandas as pd
import csv
import matplotlib.pyplot as plt
from PIL import Image



st.title("""Alzheimer's Research""" )
st.markdown("[CSV in Google Sheets](https://docs.google.com/spreadsheets/d/155mUETVqN_IAsxMXwWSeJdDAFSAEgOX1kLGGJokHhVY/edit?usp=sharing)")

st.header("""Task 1""")
st.subheader("Description/Conceptual")
st.write('Lifestyle factors and conditions associated with cardiovascular disease can increase the risk of Alzheimers Disease. These include Smoking, Obesity, Diabetes, and Physical Activity. Objective is to create a line chart, Each Question will be its own chart, X axis = Year, Y axis = Percentage')
st.write('Goal: Discover if US is getting healthier or unhealthier over time in ways that could lead to Alzheimers disease')
st.subheader('Data Preprocessing')
st.write('1. Dropped Unnecessary rows from the dataset for this task: Rows used: YearEnded, Location, Question, Data_Value_Type_, Data_Value, Dropped year 2020 due to not all states being covered')
st.write('2. Create New Dataset Per Year')
st.write('3. Drop rows that contain null value at Data_Value column')
st.write('4. Drop rows that conatin Mean value type, only using percentage value type')
st.write('5. Create new dataset per Question and Year Combination')
st.subheader('Data Processing')
st.write('1. Find average Data_Value column in each dataset')
st.write('2. Create a new data set after all values have been averaged.')
st.write('3. Create dataframe with new dataset')
st.write('4. Create charts and graphs with new dataframe ')

df = pd.read_csv("Questions.csv")
option = st.selectbox('Select Topic', ('Smoking', 'Obesity', 'Diabetes', 'Physical Activity', 'Mental Distress'))

if option == 'Smoking':
    fig = plt.figure()
    x = df['Year']
    y = df['Smoking']
    plt.xlabel('Year')
    plt.ylabel('Percent of Adults who smoke > 100 cigerattes', fontsize = 7)
    plt.plot(x, y)
    st.info('Percentage of older adults who have smoked at least 100 cigarettes in their entire life and still smoke every day or some days')
    st.write(fig)
elif option == 'Obesity':
    fig = plt.figure()
    x = df['Year']
    y = df['Obesity']
    plt.xlabel('Year')
    plt.ylabel('%' + 'of older adults with a body mass index (BMI) of 30 or more', fontsize = 7)
    st.info('Percentage of older adults with a body mass index (BMI) of 30 or more')
    plt.plot(x, y)
    st.pyplot(fig)
elif option == 'Diabetes':
    fig = plt.figure()

    x = df['Year']
    y = df['Diabetes']
    plt.xlabel('Year')
    plt.ylabel('%'+ ' of older adults without diabetes who reported a blood sugar or diabetes test within 3 years', fontsize = 7)
    plt.plot(x, y)
    st.info('Percentage of older adults without diabetes who reported a blood sugar or diabetes test within 3 years')
    st.pyplot(fig)
elif option == 'Physical Activity':
    fig = plt.figure()
    x = df['Year']
    y = df['PhysicalActivity']
    plt.xlabel('Year')
    plt.ylabel('%'+ ' older adults without leisure time physical activity in the past month', fontsize = 7)
    plt.plot(x, y)
    st.info('Percentage of older adults who have not had any leisure time physical activity in the past month')
    st.pyplot(fig)
elif option == 'Mental Distress':
    fig = plt.figure()
    x = df['Year']
    y = df['MentalDistress']
    plt.xlabel('Year')
    plt.ylabel('Percentage of older adults who are experiencing frequent mental distress', fontsize = 7)
    plt.plot(x, y)
    st.info('Percentage of older adults who are experiencing frequent mental distress')
    st.pyplot(fig)
    
opt2 = st.selectbox('Charts with inconsistent years', ('Diagnosed with High Blood Pressure', 'Take Medication for High Blood Pressure', 'Sleep Health'))
if opt2 == 'Diagnosed with High Blood Pressure':
    fig = plt.figure()
    x = df['Year']
    y = df['DiagBP']
    plt.xlabel('Year')
    plt.ylabel('Percentage of adults diagnosed with High Blood Pressure', fontsize = 7)
    plt.plot(x, y)
    st.info('Percentage of adults diagnosed with High Blood Pressure(2015, 2017, 2019)')
    st.pyplot(fig)
elif opt2 == 'Take Medication for High Blood Pressure':
    fig = plt.figure()
    x = df['Year']
    y = df['MedBP']
    plt.xlabel('Year')
    plt.ylabel('Percentage of adults that take medication for High Blood Pressure', fontsize = 7)
    plt.plot(x, y)
    st.info('Percentage of older adults who have been told they have high blood pressure who report currently taking medication for their high blood pressure(2015, 2017, 2019)')
    st.pyplot(fig)
elif opt2 == 'Sleep Health':
    fig = plt.figure()
    x = df['Year']
    y = df['SleepHealth']
    plt.xlabel('Year')
    plt.ylabel('Percentage of older adults getting sufficient sleep (>6 hours)', fontsize = 7)
    plt.plot(x, y)
    st.info('Percentage of older adults getting sufficient sleep (>6 hours)(2016, 2018)')
    st.pyplot(fig)
    
st.header("""Task 2""")
st.subheader("Description/Conceptual")
st.write('The objective is to discover what lifestyle factors, and groups of people are most strongly associated with Alzheimer’s disease. Association mining is one approach to discovering the strongest correlations to Alzheimer’s disease. ')
st.write('By using the Apriori algorithm on the data, we generated the strongest factors associated with Alzheimer’s disease, generated a CSV file and bar graph of the associations. We were then prepared to conduct an analysis on our CSV file and bar graph.')
st.subheader('Data Preprocessing')
st.write('1. Find most relevant columns: LocationDesc, Topic, Stratification2(Patient Demographic)')
st.write('2. Clean up CSV File: remove unnecessary commas, quotation marks, and rows with missing data')
st.write('3. Create a two dimensonal array containing patient location, demographic, and topic')
st.subheader('Data Processing')
st.write('1. Create a pandas data frame that contains boolean equivalent of two dimensional matrix. Each value in the boolean data frame, a value of true would be contained if a patient had a certain demographic, location, or topic discussed. False if otherwise')
st.write('2. Apply Apriori algorithm to create a third Data frame that contained all frequent patterns with minimum support of .02')
st.write('3. Convert values of the data frame that contained the factors with highest association with Alzheimers disease to strings')
st.write('4. Create a bar graph of each lifetyle factor, demographic, and geographic locations and their support. X axis = factors, Y axis = Support ')

st.markdown("[Full documentation of Data Preprocessing and Processing](https://docs.google.com/document/d/1ZvkwOFCHKBaxqf9qET75GQmj2xColFeFtxfG7932Fw0/edit?usp=sharing)")
image = Image.open('Association.png')
st.image(image, caption = 'Lifestyle factors, demographics, and geographic locations associated with Alzheimers Disease Bar Graph')

st.header('Task 3')
st.subheader('Description/Conceptual')
st.write('We were curious about the possible outliers inside of the dataset. The data file of Alzheimer’s Disease patients contains a description of the topic the patient discussed with their healthcare provider, their demographic information, and location. One approach to outlier detection is to treat the description of the topic the patient discussed with their healthcare provider, their demographic information, and location as a representation of that person. In other words, we wanted to know what combinations of demographic information, location, and topic discussed are the least common in the dataset. It is important to note that several different people can have the same description. Several different people can live in the same area, have the same demographic information, and see their healthcare provider for the same reason.')
st.subheader('Data Preprocessing')
st.write('1. Clean up csv file: remove unnecessary commas')
st.write('2. Create list of relevant data to pass to a method that would generate strings that reperesent a generalization of a type of patient')
st.subheader('Data Processing')
st.write('1. Create data frame out of frequency of patient generalizations ')
st.write('2. Count instances of relevant generalizations of each person')
st.write('3. Sort in descending order of frequency to more easily detect outliers')
st.write('4. Plot data frame into bar chart to visualize frequency of generalizations')

st.markdown("[Full documentation of Data Preprocessing and Processing](https://docs.google.com/document/d/101nYFZ9dwIG-cV7asKkpjmTcbljEeiMFiReMaUhHtu0/edit?usp=sharing)")

image2 = Image.open('Frequency.png')
st.image(image2)