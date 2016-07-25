# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 22:47:55 2016

@author: waytoalpit
"""

import pandas as pd
import numpy as np
import glob

#filter selected file among numerous files
print (glob.glob("sales*.xlsx"))

#initialize a blank DataFrame then append all of the individual files into the all_data DataFrame
all_data = pd.DataFrame()
for f in glob.glob("sales*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)


#describe to view the meta data of all_data
print (all_data.describe())

#glimpse of your all_data
print (all_data.head())

#don't forget to date column to datetime object
all_data['date'] = pd.to_datetime(all_data['date'])

#load customer status data
status = pd.read_excel("customer-status.xlsx")
print (status.head())

#combining data
#merge using left join, similar to excel vlookup function
all_data_st = pd.merge(all_data, status, how='left')
print (all_data_st.head())

#look for particular account info
print (all_data_st[all_data_st["account number"]==737550].head())

#Oops this account has status as NaN, fix this by assigning to Bronze
all_data_st['status'].fillna('bronze',inplace=True)
print (all_data_st[all_data_st["account number"]==737550].head())

#check your Pandas version
print (pd.__version__)

#create category as datatype to columns which takes fixed, limited values like gender, color etc.
all_data_st["status"] = all_data_st["status"].astype("category")

#verify the status data type
print (all_data_st.dtypes)

#normal alphabetical sort on status
print (all_data_st.sort(columns=["status"]).head())

#set ordering on status to decide the ordering
all_data_st["status"].cat.set_categories([ "gold","silver","bronze"],inplace=True)
print (all_data_st.sort(columns=["status"]).head())


#Analyze the data- status
print (all_data_st["status"].describe())

#how top tier customers are performaing compared to the bottom
print (all_data_st.groupby(["status"])["quantity","unit price","ext price"].mean())

#run multiple aggregate function for deeper insight
print (all_data_st.groupby(["status"])["quantity","unit price","ext price"].agg([np.sum,np.mean, np.std]))

#filter out the unique accounts and see how many gold, silver and bronze customers there are
print (all_data_st.drop_duplicates(subset=["account number","name"]).ix[:,[0,1,7]].groupby(["status"])["name"].count())

#example completed