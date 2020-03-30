from django.shortcuts import render, redirect
from alpha_vantage.timeseries import TimeSeries
import time

# pylint: disable-all

def get_data(id):

    api_key = 'G52RTNSQBOQ4FZZY'

    ts = TimeSeries(key = api_key, output_format='json')
    data = ts.get_daily(symbol=id, outputsize = 'compact')
    print(data)
   
    #paivat = []
    kurssit = []
    counter = 0

    for rivi in data:
        kurssit.append(rivi.values())


    for alkio in kurssit:
        print(alkio)





















    




