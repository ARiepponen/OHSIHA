import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
api_key = 'G52RTNSQBOQ4FZZY'

ts = TimeSeries(key = api_key, output_format='json')
data = ts.get_daily(symbol='MSFT', outputsize = 'compact')

paivat = []
kurssit = []

for key in data:
    counter = 0
    for paiva in key.keys():

        if(counter <=85):  
            paivat.append(paiva)

            arvo = key[paiva]["1. open"]
            print(arvo)
            kurssit.append(arvo)
            counter += 1







   # for arvo in key.values():
        #kurssi.append(arvo)

#for arvo in paivat:
   # print(arvo)

for kurssi in kurssit:
    print(kurssi)