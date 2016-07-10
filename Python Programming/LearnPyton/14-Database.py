# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 01:02:27 2016

@author: waytoalpit
"""

import pymssql
conn = pymssql.connect(host='SQL01', user='user', password='password', database='mydatabase', as_dict=True)
cur = conn.cursor()

cur.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
for row in cur:
    print ("ID=%d, Name=%s" % (row['id'], row['name']))

conn.close()