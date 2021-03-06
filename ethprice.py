import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd%2Cbtc&include_market_cap=true&include_24hr_change=true"


def forgwei():
    data = requests.get(url).json()
    pusd = round(data["ethereum"]["usd"], 2)
    return pusd

def getprice():
    data = requests.get(url).json()
    pusd = round(data["ethereum"]["usd"], 2)
    pusd = format(pusd, ",")
    pbtc = round(data["ethereum"]["btc"], 8)
    pchange = round(data["ethereum"]["usd_24h_change"], 2)
    market = round(data["ethereum"]["usd_market_cap"])
    market = format(market, ",")
	
    price = f"""<b><ins><a href='https://coingecko.com/en/coins/ethereum/'>Ethereum | $ETH</a> Price:</ins></b>
<b>ð° USD:</b> ${pusd}
<b>ðŋ BTC:</b> āļŋ{pbtc}
<b>ð 24h change:</b> {pchange}%
<b>ð Market Cap:</b> ${market}
	"""
    
    return price
