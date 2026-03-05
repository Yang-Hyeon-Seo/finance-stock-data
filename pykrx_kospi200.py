"""
pykrx 라이브러리를 활용하여 kospi200에 포함되는 주식의 주식 코드 찾기
"""

from pykrx import stock, bond
import datetime

date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
print(date)
tickers = stock.get_index_portfolio_deposit_file("1028", date)
print(tickers)

tickers = stock.get_market_ticker_list("20190225")
print(tickers)

tickers = stock.get_market_ticker_list(date)
print(tickers)
for ticker in tickers[:5]:
    name = stock.get_market_ticker_name(ticker)
    print(f'{ticker}: {name}')