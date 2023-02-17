{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1895621e-04f9-4a40-81f2-5b41414a5474",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "# Used to access APIs\n",
    "import time\n",
    "# Used to check the runtime of the function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "da0f3007-7fc5-4142-9a7c-ecfa9516c982",
   "metadata": {},
   "outputs": [],
   "source": [
    "def accessing_endpoints_loop(ticker:str):\n",
    "    \n",
    "    endpoints =[\n",
    "      # {'name':'Balance_sheet','url':f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={ticker}&apikey=RQRA0RQ6ZZAVMA26'},\n",
    "      {'name':'Stock_price','url': f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={ticker}&outputsize=full&apikey=RQRA0RQ6ZZAVMA26'}\n",
    "        # ,{'name':'Income_statement','url':f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey=RQRA0RQ6ZZAVMA26'},\n",
    "    ]\n",
    "    \n",
    "    raw_data = []\n",
    "    \n",
    "    for endpoint in endpoints:\n",
    "        name = endpoint['name']\n",
    "        url = endpoint['url']\n",
    "        \n",
    "    try:\n",
    "        response = requests.get(url)\n",
    "        response.raise_for_status()\n",
    "        raw_data.append(response.json())\n",
    "    \n",
    "    except response.exceptions.HTTPError as err:\n",
    "      return f'HTTP error with {name} endpoint :{err}'\n",
    "\n",
    "    except response.exceptions.RequestExceptions as err:\n",
    "      return f'Request error with {name} endpoint:{err}'\n",
    "\n",
    "    return raw_data\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1c8daa50-aa25-4f3b-af10-8848bc8db947",
   "metadata": {},
   "outputs": [],
   "source": [
    "company_stock_data = accessing_endpoints_loop('TSLA')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "272a807f-c74a-4f52-a3e2-06ef677c4980",
   "metadata": {},
   "outputs": [],
   "source": [
    "# (company_stock_data[0]['Monthly Time Series'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "d44bf7fd-96cc-46b0-a2f0-08f87fb6a456",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The average runtime is:\n",
      "0.22313609917958577\n"
     ]
    }
   ],
   "source": [
    "\n",
    "ticker_symbols = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'FB', 'JNJ', 'V', 'PG', 'JPM','XOM', 'VZ', 'T', 'HD', 'UNH', 'MA', 'INTC', 'CVX', 'WFC', 'PFE','CSCO', 'DIS', 'PEP', 'BAC', 'BA', 'MRK', 'NKE', 'KO', 'GE', 'MCD','CAT', 'DWDP', 'MMM', 'IBM', 'WMT', 'UNP', 'AXP', 'VRSN', 'UPS', 'ORCL','CHTR', 'TMO', 'ADBE', 'DOW', 'LLY', 'ACN', 'ABT', 'NVDA', 'AVGO', 'HON','TXN', 'NEE', 'INTU', 'MO', 'MDLZ', 'PM', 'TATAMOTORS', 'VOD', 'MMC', 'VFC','ADP', 'ITW', 'ROP', 'CELG', 'LMT', 'BLK', 'BKNG', 'WBA', 'SBUX', 'DUK','EXC', 'LOW', 'AMT', 'SO', 'PNC', 'EMR', 'HUM', 'PPG', 'RTN', 'LRCX','CVS', 'PPL', 'MRO', 'AEP', 'MS', 'D', 'CAG', 'ED', 'AIG', 'CMCSA']\n",
    "\n",
    "run_time_list = []\n",
    "\n",
    "for i in ticker_symbols:\n",
    "\n",
    "  start_time = time.time()\n",
    "\n",
    "  accessing_endpoints_loop(i)\n",
    "\n",
    "  end_time = time.time()\n",
    "\n",
    "  run_time = (end_time)-(start_time)\n",
    "\n",
    "  run_time_list.append(run_time)\n",
    "\n",
    "print(\"The average runtime is:\")\n",
    "print(sum(run_time_list)/len(ticker_symbols))  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "fa1d82c3-5208-4ab7-b321-67cafc0dc9d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(company_stock_data[0])\n",
    "# (company_stock_data[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "060b8367-4997-4853-8e08-9339db4d0e41",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8a98dd6f-8a33-477c-a595-a0aeda3cf3e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"tesla_stock_data.pkl\", \"wb\") as f:\n",
    "    pickle.dump(company_stock_data,f)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
