import requests

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url).json()
    # print(r)
    price = response['ticker']['last']
    return str(price) + ' usd'


print(get_btc())