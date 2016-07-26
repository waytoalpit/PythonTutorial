# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 22:04:07 2016

@author: waytoalpit
"""

#pandas pivot table for data analysis

import pandas as pd
import numpy as np

df = pd.read_excel("sales-funnel.xlsx")
#print (df)

#set the status as category for our convenience
df["Status"] = df["Status"].astype("category")
df["Status"].cat.set_categories(["won","pending","presented","declined"],inplace=True)
#print (df.sort(columns=["Status"]))

#simplest pivot table must have a dataframe and an index
#let's create name as our index
#observe: unique names with their account, avg price and avg quantity 
print (pd.pivot_table(df,index=["Name"]))


#if needed, create multiple indexes
#diff between indexes and indices

#creating multiple indices
#observe: almost same as above, more info with reportee and manager
print (pd.pivot_table(df,index=["Name","Rep","Manager"]))

#make more interesting by changing index of Rep and Manager
#Rep with avg weighted account, avg price and avg quantity
#smart enough to agrregate data, Do you feel good?
print (pd.pivot_table(df,index=["Manager","Rep"]))

#remove unwanted columns by explicitly mentioning the needed ones
print (pd.pivot_table(df,index=["Manager","Rep"],values=["Price"]))

#price is default represented as average value, you can apply any 
#aggreate function like sum
print (pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],aggfunc=np.sum))

#like mean and count
print (pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],aggfunc=[np.mean,len]))

#difference between Columns and Values
#Columns are optional and used to segment the actual values we care about
#Values are used to apply aggregate functions
#sum of the prices for different products for a Rep
print (pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],
               columns=["Product"],aggfunc=[np.sum]))


#NaN irritates you, replace with 0
print (pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],
               columns=["Product"],aggfunc=[np.sum],fill_value=0))
               
#add quantity to the values list
print (pd.pivot_table(df,index=["Manager","Rep"],values=["Price","Quantity"],
               columns=["Product"],aggfunc=[np.sum],fill_value=0))
               
#play with data analysis by changing index and column values
               


























