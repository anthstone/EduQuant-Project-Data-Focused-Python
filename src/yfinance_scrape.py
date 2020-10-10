import requests
from bs4 import BeautifulSoup
import pandas as pd

from tech_stocks import get_tech_stocks

# TODO
def get_finance_stats(ticker):
    df = pd.read_csv("../data/finance_stats.csv")
    print(df.loc[ticker])


# TODO
def get_closing_prices(ticker):
    df = pd.read_csv("../data/closing_prices.csv")


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
            d[cells[0].text] = cells[4].text

    return d


def update_data():
    tickers = get_tech_stocks()

    # start with first ticker to set columns
    d = fetch_finance_stats(tickers[0])
    df1 = pd.DataFrame(columns=d.keys())
    df1.loc[tickers[0]] = d.values()

    # start with first ticker to set columns
    d = fetch_closing_prices(tickers[0])
    df2 = pd.DataFrame(columns=d.keys())
    df2.loc[tickers[0]] = d.values()

    for ticker in tickers[1:]:
        # financial info
        d = fetch_finance_stats(ticker)
        df1.loc[ticker] = d

        # closing prices
        d = fetch_closing_prices(ticker)
        df2.loc[ticker] = d

    df1.to_csv("../data/finance_stats.csv")
    df2.to_csv("../data/closing_prices.csv")


if __name__ == "__main__":
    # get_finance_stats("AAPL")
    # get_closing_prices("AAPL")
    update_data()
