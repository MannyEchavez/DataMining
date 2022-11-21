import csv
import pandas as pd

# Age to low confidence,  High Confidence, Stratification1 = age group
# only 3, Overall, 50-64, 65 years or older
df = pd.read_csv("alz.csv",  usecols = ["High_Confidence_Limit", "Stratification1"], low_memory=False)

# create a list for each age group, list contains an entry of each high confidence limit
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
        

    
        


