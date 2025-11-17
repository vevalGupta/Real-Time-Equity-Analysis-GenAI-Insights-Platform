import os;os.system('cls')
import pandas as pd
"""
Data cleaning
"""
# data cleaning include
read =pd.read_excel("Stocks_after_every_5min.xlsx")
print(read.head())
# first some information about dataframe
info =read.info()
print(f"some basic  information : {info}")
# 1)Handling missing value
null_check=read.isna()
print(f"Checking if the dataframe contain missing value :{null_check}")
# 2)Duplication removal
duplicate = read.duplicated()
print(f"checking if dataFrame contain duplicate: \n{duplicate}")
# 3)fixing Datatype 
# check data type 
print("checking for any data type has changed or not : \n")
numerical =["Open","High","Low","Close"]
if all(read[numerical].dtypes== float):print("correct data type")
else:print("Need to change")
if read["Volume"].dtype== int:print("correct data type")
else:print("Need to change")
# Standardizing Data
# Make names, formats, and units consistent.
print("convert the first letter of headers into capital.:\n")
read.columns = [col.capitalize() for col in read.columns]
str_cols = read.select_dtypes(include=['object']).columns
read[str_cols] = read[str_cols].apply(lambda s: s.where(s.isna(), s.astype(str).str.capitalize()))
print(read.head())
# making cleaned file
read.to_excel("cleaned_Stock_info.xlsx",index=False)
print("\n Successfully transform")