# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:23:03 2020

@author: antho
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:02:20 2020

@author: antho
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

tickers = {"ORCL"}

for ticker in tickers:
    r = requests.get(f"https://finance.yahoo.com/quote/{ticker}?p={ticker}")
    soup = BeautifulSoup(r.text, "lxml")
    tables = soup.findAll("table")
    previous_close = tables[0].findAll("tr")[0].findAll("td")[1].text
    average_volume = tables[0].findAll("tr")[7].findAll("td")[1].text
    market_cap = tables[1].findAll("tr")[0].findAll("td")[1].text
    beta = tables[1].findAll("tr")[1].findAll("td")[1].text
    pe_ratio = tables[1].findAll("tr")[2].findAll("td")[1].text
    eps = tables[1].findAll("tr")[3].findAll("td")[1].text

    df = pd.DataFrame(columns=["Closing Price"])
    r = requests.get(f"https://finance.yahoo.com/quote/{ticker}/history?p={ticker}")
    soup = BeautifulSoup(r.text, "lxml")
    tables = soup.findAll("table")
    for tr in tables[0].findAll("tr"):
        cells = tr.findAll("td")
        if len(cells) > 3:
            df.loc[cells[0].text] = cells[4].text
