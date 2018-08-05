# -*- coding: utf-8 -*-
# @Author: Ematrix163
# @Date:   2018-08-04 10:47:54
# @Last Modified by:   Ematrix163
# @Last Modified time: 2018-08-04 10:51:30


import csv

with open('stop_time.csv') as f:
	csv_reader = csv.reader(f, delimiter=',')
	for row in csv_reader:
		print(row[4])