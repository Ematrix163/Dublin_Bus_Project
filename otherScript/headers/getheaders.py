# -*- coding: utf-8 -*-
# @Author: Ematrix163
# @Date:   2018-07-23 14:26:44
# @Last Modified by:   Ematrix163
# @Last Modified time: 2018-07-24 12:43:28


import json, csv


result = {}

with open('headers_25_1.csv','r') as f:
	a = f.read()
	a = a.split('\n')
	

result = {"25_1": a}


with open('headers.json', 'w') as outfile:
	json.dump(result, outfile)
