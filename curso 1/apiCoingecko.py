#https://pypi.org/project/pycoingecko/
from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.graph_objects as go
from pprint import pprint as print
cg = CoinGeckoAPI()
#print(cg.get_coins_list())
bitcoin_data = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='usd', days=30)



bitcoin_price_data = bitcoin_data['prices']

#bitcoin_price_data[0:5]

data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')
candlestick_data = data.groupby(data.Date.dt.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})

fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()