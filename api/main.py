from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
   return 'Welcome to the stock API 📈'

@app.route('/api/stock/<string:ticker>')
def get_stock(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    return jsonify(stock_info)

@app.route('/api/stock/<string:ticker>/history')
def get_stock_history(ticker):
    stock = yf.Ticker(ticker)
    stock_history = stock.history(period='1d')
    return stock_history.to_json()

@app.route('/api/stock/<string:ticker>/recommendations')
def get_stock_recommendations(ticker):
    stock = yf.Ticker(ticker)
    stock_recommendations = stock.recommendations
    return stock_recommendations.to_json()


if __name__ == '__main__':
    app.run(debug=True, port=5001)