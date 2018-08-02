# -*- coding: utf-8 -*-
# @Author: Ematrix163
# @Date:   2018-07-16 14:49:02
# @Last Modified by:   Ematrix163
# @Last Modified time: 2018-07-31 21:23:50


'''
This program is to scrapy the sequence of all stops of all bus routes
in different directions.
'''



import json
import requests

# with open('../backend/static/stopSeq/46A.json') as f:
# 	data = json.load(f)['info']
busroute = ['145', '9', '54A', '7', '39', '56A', '37', '11', '63', '122', 
       '39A', '70', '42', '40D', '32', '31A', '40', '67', '40B', '41C',
       '38A', '123', '14', '15', '76', '66A', '79A', '17A', '77A', '27A',
       '7B', '270', '140', '16', '66', '66X', '4', '25B', '25A', '38',
       '239', '49', '17', '27B', '65B', '15B', '84X', '185', '46A', '45A',
       '15A', '33X', '102', '18', '47', '33', '83A', '83', '66B', '114',
       '75', '27', '31', '120', '41', '130', '1', '150', '65', '13',
       '69X', '44', '69', '68', '26', '59', '61', '33B', '184', '43',
       '79', '238', '84', '53', '104', '151', '68A', '41X', '16C', '33A',
       '41B', '25', '25D', '29A', '38B', '67X', '31B', '84A', '220', '7D',
       '51D', '25X', '46E', '32X', '236', '8', '51X', '38D', '44B', '161',
       '27X', '76A', '142', '111', '116', '77X', '14C', '41A', '118',
       '757','7A']

url = 'http://localhost:8081/route/'


for route in busroute:
    route = route.lower()
    outStops = requests.get(url + route + '/O')
    inStops = requests.get(url + route + '/I')
    outStops = json.loads(outStops.text)
    inStops = json.loads(inStops.text)
    outData = outStops['info']
    inData = inStops['info']
    newData = {}
    count = 0
    for each in outData:
        count += 1
        stopid = each['stopNr']
        newData[stopid] = count
    with open('./data/' + route + '_1.json', 'w') as fp:
        json.dump(newData, fp)
    newData = {}
    count = 0
    for each in inData:
        count += 1
        stopid = each['stopNr']
        newData[stopid] = count
    with open('./data/' + route + '_2.json', 'w') as fp:
        json.dump(newData, fp)