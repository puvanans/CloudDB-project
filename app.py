import requests
import pickle
from datetime import datetime
import plotly.express as px
import plotly.graph_objs as go

from fundamentalScripts import accessing_endpoints_loop,dataExtraction,percent_Change,dataTransformation,stockViz

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods =['GET','POST'])

def home():
    if request.method == 'POST':
        ticker = request.form['ticker']
        data = accessing_endpoints_loop(ticker)
        data = dataExtraction(data)
        data = dataTransformation(data)
        priceTracker = stockViz(data)
        
        return render_template('result.html', price_plot = priceTracker.to_html(full_html=False))

    return render_template('home.html')
        
    if __name__ == '__main__':
    app.run()