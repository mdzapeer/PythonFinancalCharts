
import pandas
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from bokeh.plotting import figure, show , output_file

cc = CryptoCurrencies(key='K53QQNRE6X9S2YCI', output_format='pandas')

data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='USD')

data["Date"]=pandas.to_datetime(data.index)
data1=data[-50:]

p=figure(x_axis_type='datetime', width=1000, height=300)
p.title.text="Candlestick Chart"

w = 12*60*60*1000 # half day in ms




#df=pandas.read_json("https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol=BTC&market=USD&apikey=K53QQNRE6X9S2YCI", )



data1["Date"]=pandas.to_datetime(data1.index)

increase=data1["4a. close (USD)"] > data1["1a. open (USD)"]
decrease=data1["4a. close (USD)"] < data1["1a. open (USD)"]

p.segment(data1.Date,data1["2b. high (USD)"],data1.Date,data1["3b. low (USD)"],color="black")

p.vbar(data1.Date[increase],w,data1["1a. open (USD)"][increase],data1['4b. close (USD)'][increase],fill_color="green", line_color="black")
p.vbar(data1.Date[decrease],w,data1["1a. open (USD)"][decrease],data1['4b. close (USD)'][decrease],fill_color="red", line_color="black")

output_file("test.html", title="sampletest")
show(p)
