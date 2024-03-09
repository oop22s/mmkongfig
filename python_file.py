import requests

def get_btc_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    btc_price = data['bitcoin']['usd']
    return btc_price

print("Current BTC Price in USD:", get_btc_price())
