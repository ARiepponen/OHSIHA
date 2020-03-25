import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
api_key = 'G52RTNSQBOQ4FZZY'

ts = TimeSeries(key = api_key, output_format='pandas')
data = ts.get_daily(symbol='MSFT', outputsize = 'full')
print(data)