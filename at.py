from flask import Flask
from flask import jsonify
import json
import requests

app = Flask(__name__)
gapi = lambda stockName: "https://finance.google.com/finance?q=" + stockName + "&output=json"

@app.route('/')
def index():
    url = gapi("GOOG")
    req = requests.get(url)
    res = json.loads(req.content[6:-2].decode('unicode_escape'))

    stock = {}

    stock['52wkHigh']               = res['hi52']
    stock['52wkLow']                = res['lo52']
    stock['beta']                   = res['beta']
    stock['change']                 = res['c']
    stock['dividendYield']          = res['dy']
    stock['eps']                    = res['eps']
    stock['exchange']               = res['e']
    stock['exchangeOpen']           = res['eo']
    stock['high']                   = res['hi']
    stock['institutionalOwnership'] = res['instown']
    stock['low']                    = res['lo']
    stock['name']                   = res['name']
    stock['open']                   = res['op']
    stock['pe']                     = res['pe']
    stock['percentChange']          = res['cp']
    stock['price']                  = res['l']
    stock['symbol']                 = res['t']

    return jsonify(stock)

if __name__ == "__main__":
    app.run()
