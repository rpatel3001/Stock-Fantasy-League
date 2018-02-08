import requests
import json
import pprint

'''url = "https://www.alphavantage.co/query"

function = "TIME_SERIES_DAILY"
symbol = "MSFT"
api_key = "DEDSQFY460FDRASD"

webdata = { "function": function,
         "symbol": symbol,
         "apikey": api_key }
page = requests.get(url, params = webdata)

#pprint.pprint(page.json())

print (page.json()['1. open'])'''

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo" #need to find a way to change the parameters of request
json_data = requests.get(url).json() #grabs the data from the API in .json format
#print(json_data) #prints all data including BOTH meta data and daily values
daily_Values = json_data['Time Series (Daily)'] #grabs the data only about daily values
keylist = daily_Values.keys() #testing how keys work
print(keylist)

key = input("gimme a key: ")
for key in keylist:
    if key in daily_Values:
        data = daily_Values[key]
        break

print("heres the datadata")