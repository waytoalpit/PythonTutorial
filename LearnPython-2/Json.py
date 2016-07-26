# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 09:54:28 2016

@author: waytoalpit
"""

import requests, pandas
pandas.read_json(requests.get('http://jsonplaceholder.typicode.com/posts/1/comments').text).to_csv('jsonExcel.xls', index=True)