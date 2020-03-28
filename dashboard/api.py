import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time


api_key = 'G52RTNSQBOQ4FZZY'

ts = TimeSeries(key = api_key, output_format='json')
data = ts.get_daily(symbol='MSFT', outputsize = 'compact')

paivat = []
kurssit = []
counter = 0

for key in data:
    counter = counter + 1
    if(counter <= 5):
        for paiva in key.keys():

            paivat.append(paiva)
            try:       
                arvo = key[paiva]["1. open"]
                
                kurssit.append(arvo)
            except:
                pass

pituus = len(paivat)
uusi_pituus = pituus - 5
del paivat[uusi_pituus:]


for kurssi in kurssit:
    print(kurssi)

for dagen in paivat:
    print(dagen)


print(len(paivat))
print(len(kurssit))