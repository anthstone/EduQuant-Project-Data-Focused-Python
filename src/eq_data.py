import pandas as pd
from pathlib import Path


def get_finance_stats(ticker):
    try:
        path = Path(__file__).parent.absolute().parent
        df = pd.read_csv(path / "data" / "finance_stats.csv", index_col=0)
        return df.loc[ticker.upper()].to_dict()
    except FileNotFoundError:
        print("Data is missing. Try running 'Update Data' from the main menu")
        return None


def get_closing_prices(ticker):
    try:
        path = Path(__file__).parent.absolute().parent
        df = pd.read_csv(path / "data" / "closing_prices.csv", index_col=0)
        return list(df.loc[ticker.upper()].items())
    except FileNotFoundError:
        print("Data is missing. Try running 'Update Data' from the main menu")
        return None
