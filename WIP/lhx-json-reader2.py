#!/usr/bin/env python3
import json
import csv

lhjson = open ('test-fl.json',)

data = json.load(lhjson)

# WORKING, WHAT I NEED:
#for info in (data['audits']['metrics']['details']['items']):
#    print(info)

correct = data['audits']['metrics']['details']['items'][0]

print(correct)

# WRITE TO JSON:
emp_data = data['audits']['metrics']['details']['items']

# open a file for writing
employ_data = open('test14.csv', 'a')

# create the csv writer object
csvwriter = csv.writer(employ_data)

# count = 0

for info in (data['audits']['metrics']['details']['items'][0]):
#      if count == 0:
#             header = info.keys()
#             csvwriter.writerow(header)
#             count += 1

        csvwriter.writerow(correct.values())

employ_data.close()

lhjson.close()


#
# STILL NEED TO CREATE THE BASE FILE, probably should just save the headers in github as a template instead of trying to create them? Unless creating them as part of the original install.
# 



'''
# WORKING, WHAT I NEED:

# This will print all of the nested data
for info in (data['audits']['metrics']['details']['items']):
    print(info)
# This will print just the first nested data:
print(data['audits']['metrics']['details']['items'][0])


'''



'''
#WORKING
json_dictionary = json.load(lhjson)
for key in json_dictionary:
	    print(key, ":", json_dictionary[key])

# ALSO WORKS
print (data['audits']['speed-index']['displayValue'])
'''

'''
What really helped was looking deepr into nested data {} vs values []. Once I removed one of the subdirectories, it worked. 
'''


'''
Troublshooting:
https://stackoverflow.com/questions/24708634/python-and-json-typeerror-list-indices-must-be-integers-not-str 
https://stackoverflow.com/questions/25855276/parsing-json-with-python-typeerror-list-indices-must-be-integers-not-str
https://kite.com/python/answers/how-to-iterate-through-a-json-string-in-python
https://stackoverflow.com/questions/34951448/issues-iterating-through-json-list-in-python

'''


'''
Worth recording and measuring:
- Date
- Tested UrL
- Page Size
- Load Time
- Network Requests
- Time to First Byte
- Time to Interactive
- First Contentful Paint
- First Meaningful Paint
- Final Screenshot
- Network Server Latency


firstContentfulPaint	3479
firstMeaningfulPaint	8160
firstCPUIdle	10793
interactive	11311
speedIndex	6553
estimatedInputLatency	87
totalBlockingTime	1644
observedNavigationStart	0
observedNavigationStartTs	25440453439
observedFirstPaint	1022
observedFirstPaintTs	25441475862
observedFirstContentfulPaint	1022
observedFirstContentfulPaintTs	25441475862
observedFirstMeaningfulPaint	2172
observedFirstMeaningfulPaintTs	25442625051
observedLargestContentfulPaint	2188
observedLargestContentfulPaintTs	25442641688
observedTraceEnd	4174
observedTraceEndTs	25444627883
observedLoad	1638
observedLoadTs	25442091270
observedDomContentLoaded	1194
observedDomContentLoadedTs	25441647482
observedFirstVisualChange	1321
observedFirstVisualChangeTs	25441774439
observedLastVisualChange	3088
observedLastVisualChangeTs	25443541439
observedSpeedIndex	1848
observedSpeedIndexTs	25442301765
'''