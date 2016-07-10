# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:27:47 2016

@author: waytoalpit
"""

import pandas as pd

df = pd.read_csv('WIKI-MYRG.csv')
print(df.head(10))


#create index on date field
df.set_index('Date', inplace = True)
print(df.head(5))

#send this back to a CSV
df.to_csv('newcsv2.csv')

#Index is lost on next read, create while read
df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head(5))


#change column names
df.columns = ['col1','col2','col3','col4','col5','col6' \
,'col7','col8','col9','col10','col11','col12']
print(df.head(5))


#save again to CSV without header
df.to_csv('newcsv3.csv', header=False)


#read csv and pass header + index
df = pd.read_csv('newcsv3.csv', names = ['col1','col2','col3','col4','col5','col6' \
,'col7','col8','col9','col10','col11','col12'], index_col=0)
print(df.head(5))


#convert to html and put it to your website
df.to_html('example.html')


