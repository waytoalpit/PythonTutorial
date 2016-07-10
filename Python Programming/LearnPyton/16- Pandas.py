# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 09:22:19 2016

@author: waytoalpit
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

# Pandas create default index if not present, 
#else you can create/change indices
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df = pd.DataFrame(web_stats)
print(df.tail(5))

#define index to organize your data
df.set_index('Day', inplace=True)

# list down last 5 records
print(df.tail(5))

#select some particular column
print(df.Visitors)

#plot selected column
df['Visitors'].plot()
plt.show()


#plot entire data frame
df.plot()
plt.show()

print(df[['Visitors','Bounce Rate']])