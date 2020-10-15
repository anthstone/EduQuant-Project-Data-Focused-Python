import requests
from bs4 import BeautifulSoup
import pandas as pd
import eq_utilities
from pathlib import Path


def fetch_finance_stats(ticker):
    d = {}
    r = requests.get(f"https://finance.yahoo.com/quote/{ticker}?p={ticker}")
    soup = BeautifulSoup(r.text, "lxml")
    tables = soup.findAll("table")
    try:
        d["Average Volume"] = tables[0].findAll("tr")[7].findAll("td")[1].text
        d["Market Cap"] = tables[1].findAll("tr")[0].findAll("td")[1].text
        d["Beta"] = tables[1].findAll("tr")[1].findAll("td")[1].text
        d["P/E Ratio"] = tables[1].findAll("tr")[2].findAll("td")[1].text
        d["EPS"] = tables[1].findAll("tr")[3].findAll("td")[1].text
    except:
        d = {}

    return d


def fetch_closing_prices(ticker):
    d = {}
    r = requests.get(f"https://finance.yahoo.com/quote/{ticker}/history?p={ticker}")
    soup = BeautifulSoup(r.text, "lxml")
    tables = soup.findAll("table")
    for tr in tables[0].findAll("tr"):
        cells = tr.findAll("td")
        if len(cells) > 3:
            d[cells[0].text] = cells[4].text.replace(",", "")

    return d


def update_data(option="cp"):
    path = Path(__file__).parent.absolute().parent

    print("Updating stock data...")
    tickers = eq_utilities.get_tech_stocks()

    # start with first ticker to set columns
    d = fetch_finance_stats(tickers[0])
    df = pd.DataFrame(columns=d.keys())
    df.loc[tickers[0]] = d.values()

    if option == "cp":
        path = path / "data" / "closing_prices.csv"
    elif option == "fs":
        path = path / "data" / "finance_stats.csv"
    else:
        return None

    for ticker in tickers[1:]:
        # closing prices
        if option == "cp":
            d = fetch_closing_prices(ticker)
        # financial info
        elif option == "fs":
            d = fetch_finance_stats(ticker)

        df.loc[ticker] = d

    df.to_csv(path)
