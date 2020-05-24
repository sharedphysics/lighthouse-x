#!/usr/bin/env python3
import json
import csv
import time

now = time.strftime('%d-%m-%Y %H:%M:%S')

lhjson = open ('test-fl.json',)
data = json.load(lhjson)

# This will show the metrics in terminal:
lhmetrics = data['audits']['metrics']['details']['items'][0]
# print(lhmetrics) # Testing output
#print(lhmetrics.values()) # Testing output

lhmetrics.update({'timestamp' : now }) # add the timestamp dictionary

# WRITE TO JSON:
# open a file in append-only (so that it doesn't overwrite previous)
opencsvfunction = open('metrics.csv', 'a')

# create the csv writer object
csvwriter = csv.writer(opencsvfunction, delimiter = ',')
# write row
csvwriter.writerows([lhmetrics.values()])

#close the csv, close the json
opencsvfunction.close()
lhjson.close()

#
# STILL NEED TO CREATE THE BASE FILE, probably should just save the headers in github as a template instead of trying to create them? Unless creating them as part of the original install.
# 


# OLDER:

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
https://stackoverflow.com/questions/32835044/how-to-write-the-timestamp-when-exporting-to-csv-in-python
https://thispointer.com/python-add-a-column-to-an-existing-csv-file/

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