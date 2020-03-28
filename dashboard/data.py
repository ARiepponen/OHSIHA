from django.shortcuts import render, redirect
from alpha_vantage.timeseries import TimeSeries
import time

# pylint: disable-all

def get_data(id):

    api_key = 'G52RTNSQBOQ4FZZY'

    ts = TimeSeries(key = api_key, output_format='json')
    data = ts.get_daily(symbol=id, outputsize = 'compact')

   
    paivat = []
    kurssit = []
    counter = 0

    for keissi in data:
        counter = counter + 1
        if(counter <= 5):
            dict_list = keissi.keys()
            #for paiva in dict_list:

            paiva = dict_list[0]
            paivat.append(paiva)
            try:       
                arvo = keissi[paiva]["1. open"]
                    
                kurssit.append(arvo)
            except:
                pass

    pituus = len(paivat)
    uusi_pituus = pituus - 5
    del paivat[uusi_pituus:]

    return render(request, 'bonds-form.html',{'paivat':paivat,'kurssit':kurssit})




