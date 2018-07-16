# -*- coding: utf-8 -*-
# @Author: Ematrix163
# @Date:   2018-07-16 14:49:02
# @Last Modified by:   Ematrix163
# @Last Modified time: 2018-07-16 14:53:22


import json

with open('../backend/static/stopSeq/46A.json') as f:
	data = json.load(f)['info']


newData = {}

count = 0

for each in data:
	count += 1
	stopid = each['stopNr']
	newData[stopid] = count


with open('46A.json', 'w') as fp:
    json.dump(newData, fp)