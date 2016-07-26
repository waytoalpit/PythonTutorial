# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 00:36:10 2016

@author: waytoalpit
"""

import pandas as pd
import numpy as np

#create a series using list of values, Pandas creates default integer indexing
s = pd.Series([1,3,5,np.nan,6,8])
print (s)

#Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns
dates = pd.date_range('20130101', periods=6)
print (dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print (df)

#show index
print (df.index)

#show columns
print (df.columns)

#show values
print (df.values)

#show quick statistics of your data
print (df.describe())

#tranposing of data
print (df.T)

#sort index by axis
print (df.sort_index(axis=1, ascending=False))

#sort by column B
print (df.sort_values(by='B'))

#getting column A
print (df['A'])

#getting the sliced row records
print (df[0:3])

#getting range records
print (df['20130102':'20130104'])

#row and column slicing
print (df.iloc[[1,2,4],[0,2]])

#access particular value
print (df.iloc[1,1])

#where operation to get positive values
print (df[df > 0])

#Add a new column
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
print (df2)

#records with E= two or four
print (df2[df2['E'].isin(['two','four'])])

#set positive values to negative
df2 = df.copy()
df2[df2 > 0] = -df2
print (df2)

#diff of max-min
print (df.apply(lambda x: x.max() - x.min()))

#merge and concat examples
df = pd.DataFrame(np.random.randn(10, 4))
print (df)

#break it into pieces, row wise
pieces = [df[:3], df[3:7], df[7:]]
print (pieces[0])
print (pieces[1])
print (pieces[2])

#merge them together
df=pd.concat(pieces)
print (df)

#pivot table examples
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
  'B' : ['A', 'B', 'C'] * 4,
  'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
  'D' : np.random.randn(12),
  'E' : np.random.randn(12)})
print (df)

#spreadheet like pivot table representation
print (pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))


