# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:02:20 2020

@author: antho
"""
import requests
import io
import pandas as pd

# https://www.scrapehero.com/scrape-nasdaq-stock-market-data/
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
    "Connection": "keep-alive",
    "Host": "www.nasdaq.com",
    "Referer": "http://www.nasdaq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
}

tickers = {"AAPL", "FB", "AMD", "AMZN", "GOOGL", "ATVI", "ADBE"}

for ticker in tickers:
    url = f"https://www.nasdaq.com/api/v1/historical/{ticker}/stocks/2020-08-23/2020-09-23"
    response = requests.get(url, headers=headers, verify=False)
    df = pd.read_csv(io.StringIO(response.text))
    print(df.head())
