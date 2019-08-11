import numpy as np
import pandas as pd
import pandas_datareader as pdr
import datetime as datetime
import twstock

stock = int(input("what stock would you like to check: "))
print(twstock.codes[str(stock)])

time = int(input("From how many days before would you like to check or type 0 to skip: "))

def getDate(n):
    today = datetime.date.today()
    oneday = datetime.timedelta(n)
    date = today - oneday
    return date

if time != 0:
    print(getDate(time))
    start = getDate(time)

    df_stock = pdr.DataReader(str(stock) + ".TW", "yahoo", start = start)
    print(df_stock)
from_that_day = str(input("From what day would you like to check or type 0 to skip: "))
if from_that_day != "0":
    df_stock_day = pdr.DataReader(str(stock) + ".TW", "yahoo", from_that_day)
    print(df_stock_day)