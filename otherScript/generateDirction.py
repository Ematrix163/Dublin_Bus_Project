# -*- coding: utf-8 -*-
# @Author: Ematrix163
# @Date:   2018-07-17 12:10:03
# @Last Modified by:   Ematrix163
# @Last Modified time: 2018-07-17 14:29:37


import json

with open('direction_raw.json') as f:
	data = json.load(f)['busNo']

newData = {}

for each in data:
	route = each['route']
	dir1 = each['destination']
	index = dir1.find('Towards')
	length = 7
	word = ' Towards '
	if index == -1:
		index = dir1.find('To')
		length = 2
		word = ' To '
	

	dir2 = 'From' + dir1[index+length:] + word + dir1[5:index]

	newData[route] = {"dir1": dir1, "dir2": dir2}


with open('directions.json', 'w') as fp:
    json.dump(newData, fp)