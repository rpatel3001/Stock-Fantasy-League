from requests import get

_AV_URL = "https://www.alphavantage.co/query"

def getCurrentPrice(ticker):
	args = {"function" : "TIME_SERIES_INTRADAY",
			"symbol" : ticker.upper(),
			"interval" : "1min",
			"apikey" : "DEDSQFY460FDRASD"}
	data_json = get(_AV_URL, params=args).json()
	if list(data_json.keys())[0] == 'Error Message':
		return data_json
	else:
		data = data_json['Time Series (1min)']
		return data[list(data.keys())[0]]['4. close']

def getCurrentPrices(tickers):
	pass

def getPriceHistory(ticker, start, end, resolution):
	pass

def getTechnicalIndicator(ticker, indicator, resolution, period):
	pass