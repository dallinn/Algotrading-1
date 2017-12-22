from flask import Flask
from flask import jsonify
import quandl
from keys import QUANDL_API_KEY
quandl.ApiConfig.api_key = QUANDL_API_KEY

app = Flask(__name__)

@app.route('/')
def index():
    data = quandl.get('NSE/OIL', rows=5, returns='json')
    return jsonify(data)

if __name__ == "__main__":
    app.run()
