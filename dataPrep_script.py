{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "946157cc-3469-4f29-9bae-ccc669aafcec",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import pprint\n",
    "import time\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6be206c3-5229-4299-8d13-1ec19dd0e34d",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"tesla_stock_data.pkl\", \"rb\") as f:\n",
    "    company_stock_data = pickle.load(f)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "8b27fb86-d82b-424c-a887-15f49d8a2684",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'1. open': '221.4800',\n",
       " '2. high': '240.8450',\n",
       " '3. low': '187.8700',\n",
       " '4. close': '212.2800',\n",
       " '5. volume': '121687759'}"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(company_stock_data[0])\n",
    "(company_stock_data[0]['Monthly Time Series']['2016-06-30'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "e8767349-b1f5-4991-9628-c79e17176fb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def dataExtraction(data):\n",
    "    \n",
    "    company_monthly_data = data[0]['Monthly Time Series']\n",
    "    \n",
    "    dateString = list(company_monthly_data.keys())\n",
    "    \n",
    "    monthly_closing_price = []\n",
    "    \n",
    "    monthly_trading_volume = []\n",
    "    \n",
    "    for date in dateString:\n",
    "        \n",
    "        value = company_monthly_data[date]\n",
    "        \n",
    "        closing_price = float(value['4. close'])\n",
    "        \n",
    "        stock_Volume = int(value['5. volume'])\n",
    "        \n",
    "        monthly_closing_price.append(closing_price)\n",
    "        \n",
    "        monthly_trading_volume.append(stock_Volume)\n",
    "        \n",
    "    return dateString,monthly_closing_price,monthly_trading_volume\n",
    "   \n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "76d99a6f-6c7d-486a-a77a-246cd8b8ebfd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "tuple"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(dataExtraction(company_stock_data))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f548ec02-dc5c-4114-a036-a38d4fa54077",
   "metadata": {},
   "source": [
    "## Average runtime\n",
    "\n",
    "* The cell below calculates the average runtime of the dataExtraction function. \n",
    "* Eventually this will be encapsulated into a function itself, which will taken in a function as an arguement."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "6c71a489-0d72-4662-9fd1-a6282e6ec9f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def percent_Change(data):\n",
    "    i = 0\n",
    "    percent_Change = []\n",
    "    while i < len(data)-1:    \n",
    "        start = data[i]\n",
    "        end =data[i+1]\n",
    "        difference = end - start\n",
    "        change = round((difference/start)*100,2)\n",
    "        percent_Change.append(change)\n",
    "        i = i+1\n",
    "    return percent_Change\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f6ace6ef-f826-4103-a9e8-100e05b2a7bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def dataTransformation(tuple):\n",
    "    \n",
    "    dateString, stock_Price, stock_Volume = dataExtraction(company_stock_data)\n",
    "    \n",
    "    date = [datetime.strptime(date_str,'%Y-%m-%d') for date_str in dateString]\n",
    "    \n",
    "    stock_Price_Change = percent_Change(stock_Price)\n",
    "    \n",
    "    stock_Volume_Change = percent_Change(stock_Volume)\n",
    "    \n",
    "    stock_Price_Change.insert(0,0)\n",
    "    \n",
    "    stock_Volume_Change.insert(0,0)\n",
    "    \n",
    "    \n",
    "    return dateString,date, stock_Price, stock_Volume, stock_Price_Change, stock_Volume_Change\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "f998dd14-55fb-4d63-b3e3-493f79bcd45b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_for_visualization = (dataTransformation(dataExtraction(company_stock_data)))\n",
    "# data_for_visualization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "8ea11f8c-ca35-44dc-b144-61982dab1cb2",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"data_for_visualization.pkl\", \"wb\") as file:\n",
    "    pickle.dump(data_for_visualization ,file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "a4261361-b2bc-4251-baf0-4a7b9d589dd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The average run time list comprehension without insertion :\n",
      "0.01223604313446698\n"
     ]
    }
   ],
   "source": [
    "x = 0\n",
    "\n",
    "run_time_list = []\n",
    "\n",
    "while x <= 5000:\n",
    "    \n",
    "    start = time.time()\n",
    "    \n",
    "    (dataTransformation(dataExtraction(company_stock_data)))\n",
    "    \n",
    "    end = time.time()\n",
    "    \n",
    "    run_time = end - start\n",
    "    \n",
    "    run_time_list.append(run_time)\n",
    "    \n",
    "    x += 1\n",
    "\n",
    "print(\"The average run time list comprehension without insertion :\")\n",
    "print(sum(run_time_list)/x)\n",
    "    "
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
