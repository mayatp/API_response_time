#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:04:18 2017

@author: mayapetranova
"""
# Maya Petranova Student ID: 161059127

import datetime 
import time 
import requests
import numpy as np
#import pandas as pd # used to plot the results

print ('Time zone converter, please enter a zone')
from_zone = input('From zone (example "GMT"): ')
to_zone = input('To zone (example "MVT"): ')
zone = [from_zone, to_zone]
zones = zone

any_time = '02%3A31%3A00+am' # setting up an example time in the required format as a string
BASE_URL = 'http://timezoneconverter.directionalstar.com/convertToJSON?'
my_symbols = '&targetTimeZone='.join(zones)
exec_time = []
result = []
my_date = datetime.date.today()
cap = 180000 # number of requests
time_cap = 60000 # per millisecond
sleep_time = 1/(cap/time_cap)
         
for i in range(200):
    start = time.time()
    my_query_url = BASE_URL + 'fromDate={}&fromTime={}&fromTimeZone={}'.format(my_date, any_time, my_symbols)
    my_response = requests.get(my_query_url).json()
    rnd = (time.time() - start)*1000 # measuring one round of a received response
    exec_time.append(rnd)
    result.append(my_response)
    time.sleep(sleep_time) #sleep time between requests
# OR    
#    if rnd < time_cap/cap:
#       time.sleep((time_cap/cap)-rnd) #sleeps for the rest of the time that it ran
    
# plot below (commented out so it doesn't run every time), enable pandas above to get the plot
#plot = pd.Series(exec_time) # plot results
#plot.hist(bins=10) # in 10 bins    

answer = result[i]['targetUTC']
difference = 'The time difference between {} and {} is '.format(zones[0], zones[1]) + answer + ' hours'                           
print(difference)

avg = np.average(exec_time)
med = np.median(exec_time)
maximum = np.max(exec_time)
std = np.std(exec_time)

print ('EXECUTION TIME in milliseconds without sleep time')
print ('Average/Mean: %.4g' % avg)
print ('Median: %.4g' % med)
print ('Max: %.4g' % maximum)
print ('Standard deviation: %.4g' % std)
