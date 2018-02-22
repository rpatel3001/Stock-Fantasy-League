from requests import get

_AV_URL = "https://www.alphavantage.co/query"

def getCurrentPrice(ticker):
	args = {"function" : "BATCH_STOCK_QUOTES",
			"symbols" : [ticker.upper()],
			"apikey" : "DEDSQFY460FDRASD"}
	data_json = get(_AV_URL, params=args).json()
	if list(data_json.keys())[0] == 'Error Message':
		return data_json
	else:
		data = list(data_json['Stock Quotes'])[0]
		return data['2. price']

def getCurrentPrices(tickers):
	pass

def getPriceHistory(ticker, start, end, resolution):
	pass

def getTechnicalIndicator(ticker, indicator, resolution, period):
	pass