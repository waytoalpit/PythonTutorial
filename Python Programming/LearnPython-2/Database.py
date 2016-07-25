# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 01:02:27 2016

@author: waytoalpit
"""

import pymssql, pandas
cursor = pymssql.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass').cursor()
cursor.execute("select * from testtable")
rows = cursor.fetchall()

columns = [desc[0] for desc in cursor.description]
pandas.DataFrame(list(rows), columns=columns).to_excel('dbExcel.xls', index=True)