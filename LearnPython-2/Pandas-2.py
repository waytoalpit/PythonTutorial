# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 20:19:18 2016

@author: waytoalpit
"""

import pandas as pd

df = pd.read_excel("sample-salesv3.xlsx")
print (df.head())

#verify datatypes as expected
print (df.dtypes)

#correct datatime from simple object to datetime type
df['date'] = pd.to_datetime(df['date'])
print (df.dtypes)

#filer data by particular account number
print (df[df["account number"]==307599].head())

#filter by some relational operator
print (df[df["quantity"] > 22].head())

#select items in which sku's starts B1
print (df[df["sku"].map(lambda x: x.startswith('B1'))].head())

#merge two or more criteria together
print (df[df["sku"].map(lambda x: x.startswith('B1')) & (df["quantity"] > 22)].head())

#define list of criteria values using isin function
print (df[df["account number"].isin([714466,218895])].head())

#filter with list of names
print (df.query('name == ["Kulas Inc","Barton LLC"]').head())

#sorting date for better clarity/visualization
df = df.sort_values(by='date')
print (df.head())

#select records with greater than some date
print (df[df['date'] >='20140905'].head())

#select records latest to speciifc month
print (df[df['date'] >='2014-03'].head())

#chaining of multiple criteria with dates
print (df[(df['date'] >='20140701') & (df['date'] <= '20140715')].head())

#whatever you like, Pandas will understand
print (df[df['date'] >= 'Oct-2014'].head())

#Another filter style
print (df[df['date'] >= '10-10-2014'].head())

#create date as an index to do some smart filtering
df2 = df.set_index(['date'])
print (df2.head())

#slice the data with dates
print (df2["20140101":"20140201"].head())

#believe me, try anything
print (df2["2014-Jan-1":"2014-Feb-1"].head())

#agree?
print (df2["2014"].head())

#u have to :)
print (df2["2014-Dec"].head())

#filter frecords with name containing LLU
print (df[df['name'].str.contains('LLC')].head())

#filter frecords with sku containing B1
print (df[df['sku'].str.contains('B1')].head())

#filter sorted records with sku containing B1-531 and quantity>40
print (df[(df['sku'].str.contains('B1-531')) & (df['quantity']>40)].sort_values(by=['quantity','name'],ascending=[0,1]))

#list of unique names
print (df["name"].unique())

#include account number but drop duplicates
print (df.drop_duplicates(subset=["account number","name"]).head())

# I just want account number and name
print (df.drop_duplicates(subset=["account number","name"]).ix[:,[0,1]])

#example completed