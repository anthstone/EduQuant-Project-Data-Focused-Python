# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:23:03 2020

@author: antho
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

from tech_stocks import get_tech_stocks

tickers = get_tech_stocks()

df1 = pd.DataFrame(columns=["Average Volume", "Market Cap", "Beta", "P/E Ratio", "EPS"])

for ticker in tickers:
    # financial info
    r = requests.get(f"https://finance.yahoo.com/quote/{ticker}?p={ticker}")
    soup = BeautifulSoup(r.text, "lxml")
    tables = soup.findAll("table")
    average_volume = tables[0].findAll("tr")[7].findAll("td")[1].text
    market_cap = tables[1].findAll("tr")[0].findAll("td")[1].text
    beta = tables[1].findAll("tr")[1].findAll("td")[1].text
    pe_ratio = tables[1].findAll("tr")[2].findAll("td")[1].text
    eps = tables[1].findAll("tr")[3].findAll("td")[1].text
    df1.loc[ticker] = {
        "Average Volume": average_volume,
        "Market Cap": market_cap,
        "Beta": beta,
        "P/E Ratio": pe_ratio,
        "EPS": eps,
    }

    # closing prices
    df2 = pd.DataFrame(columns=["Closing Price"])
    r = requests.get(f"https://finance.yahoo.com/quote/{ticker}/history?p={ticker}")
    soup = BeautifulSoup(r.text, "lxml")
    tables = soup.findAll("table")
    for tr in tables[0].findAll("tr"):
        cells = tr.findAll("td")
        if len(cells) > 3:
            df2.loc[cells[0].text] = cells[4].text