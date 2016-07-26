# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 20:31:03 2016

@author: waytoalpit
"""

#Large, persistent DataFrame in pandas
#process chunk by chunk in case of loading the entire lump at the same time

import pandas as pd

# gives TextFileReader, which is iterable with chunks of 1000 rows.
tp = pd.read_csv('jsonExcel.csv', iterator=True, chunksize=1000)  

# df is DataFrame. If errors, do `list(tp)` instead of `tp`
df = pd.concat(tp, ignore_index=True)  

print (df)
