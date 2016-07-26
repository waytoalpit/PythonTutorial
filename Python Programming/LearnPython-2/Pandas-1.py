# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 14:31:10 2016

@author: waytoalpit
"""

import pandas as pd

#read data from excel
df = pd.read_excel("excel-comp-data.xlsx")
print (df.head())

#Adding a Sum to a Row
df["total"] = df["Jan"] + df["Feb"] + df["Mar"]
print (df.head())

#Sum of a column
print (df["Jan"].sum()) 

#Mean of a column
print (df["Jan"].mean())

#Min value of a column
print (df["Jan"].min())

#max value of a column
print (df["Jan"].max())

#sum for a month and total columns
sum_row=df[["Jan","Feb","Mar","total"]].sum()
print (sum_row)

#transpose this as a row
df_sum=pd.DataFrame(data=sum_row).T
print (df_sum)

#reindex to create formatted data frame
df_sum=df_sum.reindex(columns=df.columns)
print (df_sum)

#append to exisiting data frame
df_final=df.append(df_sum,ignore_index=True)
print (df_final.tail())

#groupby data frame by state
df_grpBy=df_final[["state","Jan","Feb","Mar","total"]].groupby('state').sum()
print (df_grpBy)

#export to excel
df_final.to_excel('new-excel-comp-data.xlsx', index=True)

#example completed