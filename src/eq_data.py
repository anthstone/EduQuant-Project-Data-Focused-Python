import pandas as pd
import news_scrape
import sec_scrape
import yfinance_scrape


def get_finance_stats(ticker):
    df = pd.read_csv("../data/finance_stats.csv", index_col=0)
    return df.loc[ticker.upper()].to_dict()


def get_closing_prices(ticker):
    df = pd.read_csv("../data/closing_prices.csv", index_col=0)
    return list(df.loc[ticker.upper()].items())


def update_data():
    yfinance_scrape.update_data()
    sec_scrape.update_data()
    news_scrape.update_data()
