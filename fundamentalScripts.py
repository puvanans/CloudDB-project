import requests
import pickle
import pprint
import time
from datetime import datetime
import plotly.express as px
import plotly.graph_objs as go

def accessing_endpoints_loop(ticker:str):
    
    endpoints =[
      # {'name':'Balance_sheet','url':f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={ticker}&apikey=RQRA0RQ6ZZAVMA26'},
      {'name':'Stock_price','url': f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={ticker}&outputsize=full&apikey=RQRA0RQ6ZZAVMA26'}
        # ,{'name':'Income_statement','url':f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey=RQRA0RQ6ZZAVMA26'},
    ]
    
    raw_data = None
    
    for endpoint in endpoints:
        name = endpoint['name']
        url = endpoint['url']
        
    try:
        response = requests.get(url)
        response.raise_for_status()
        raw_data= response.json()
    
    except response.exceptions.HTTPError as err:
      return f'HTTP error with {name} endpoint :{err}'

    except response.exceptions.RequestExceptions as err:
      return f'Request error with {name} endpoint:{err}'

    return raw_data

def dataExtraction(data):
    
    company_symbol = data ['Meta Data']['2. Symbol']
    company_monthly_data = data['Monthly Time Series']
    
    dateString = list(company_monthly_data.keys())
    
    monthly_closing_price = []
    
    monthly_trading_volume = []
    
    for date in dateString:
        
        value = company_monthly_data[date]
        
        closing_price = float(value['4. close'])
        
        stock_Volume = int(value['5. volume'])
        
        monthly_closing_price.append(closing_price)
        
        monthly_trading_volume.append(stock_Volume)
        
    return dateString,monthly_closing_price,monthly_trading_volume, company_symbol
   
def percent_Change(data):
    i = 0
    percent_Change = []
    while i < len(data)-1:    
        start = data[i]
        end =data[i+1]
        difference = end - start
        change = round((difference/start)*100,2)
        percent_Change.append(change)
        i = i+1
    return percent_Change

def dataTransformation(data):
    
    dateString, stock_Price, stock_Volume, company_symbol = data
    
    date = [datetime.strptime(date_str,'%Y-%m-%d') for date_str in dateString]
    
    stock_Price_Change = percent_Change(stock_Price)
    
    stock_Volume_Change = percent_Change(stock_Volume)
    
    stock_Price_Change.insert(0,0)
    
    stock_Volume_Change.insert(0,0)
    
    
    return dateString,date, stock_Price, stock_Volume, stock_Price_Change, stock_Volume_Change, company_symbol


def stockViz(data_for_visualization):
    date = data_for_visualization[1]
    stock_Price = data_for_visualization[2]
    stock_Volume_Change = data_for_visualization[5]
    stock_Volume_Change_abs = [abs(change) for change in stock_Volume_Change]
    company_symbol = data_for_visualization[6]
    
    priceTracker = px.line(x = date, y = stock_Price, title = f"{company_symbol} Stock Price over time" )

    priceTracker.update_layout(
        yaxis_tickformat='$',
        yaxis_title='Price',
        xaxis_title='Time',
        xaxis_showgrid=False,   # Set the x-axis grid lines to show
        # yaxis_showgrid=False,   # Set the y-axis grid lines to show
        xaxis_gridcolor='lightgray',  # Set the x-axis grid color
        yaxis_gridcolor='lightgray',  # Set the y-axis grid color
        plot_bgcolor='rgb(255, 255, 255)',  # Set the background color to white
        hovermode='x unified',
        xaxis={
        'showspikes': True,
        'spikemode': 'toaxis',
        'title': 'Time'
        },
        yaxis={
        'showspikes': True,
        'spikemode': 'toaxis',
        'title': 'Price'
        }
        
    )
    priceTracker.update_traces(hovertemplate='Time: %{x}<br>Price: $%{y}')
    
    volumeTracker = px.scatter(x=stock_Price, y=stock_Volume_Change_abs,  size = stock_Volume_Change_abs ,title=f"{company_symbol} Stock Volume Change vs. Price")
    volumeTracker.update_layout(
        xaxis_title='Price',
        yaxis_title='Volume Change (absolute)',
        xaxis_showgrid=False,   # Set the x-axis grid lines to show
        yaxis_showgrid=False,   # Set the y-axis grid lines to show
        xaxis_gridcolor='lightgray',  # Set the x-axis grid color
        yaxis_gridcolor='lightgray',  # Set the y-axis grid color
        plot_bgcolor='rgb(255, 255, 255)',  # Set the background color to white
        hovermode='x unified',
        xaxis={
                'showspikes': True,
                'spikemode': 'toaxis',
                'title': 'Price'
            },
        yaxis={
                'showspikes': True,
                'spikemode': 'toaxis',
                'title': 'Volume Change (absolute)'
            }
    )
    volumeTracker.update_traces(hovertemplate='Price: $%{x}<br>Volume Change: %{y}')

    return priceTracker,volumeTracker