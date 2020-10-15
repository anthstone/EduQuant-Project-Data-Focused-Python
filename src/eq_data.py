# eq_data.py
# Description: module to handle data retrieval
# Authors: Anthony Stone
#          Alexander Talbott
#          Jim Wang


import pandas as pd
from pathlib import Path

# retrieve financial statistics from the data file
def get_finance_stats(ticker):
    # check if it exists
    try:
        path = Path(__file__).parent.absolute().parent
        df = pd.read_csv(path / "data" / "finance_stats.csv", index_col=0)
        # return as a dict
        return df.loc[ticker.upper()].to_dict()
    # if it doesn't, print a message and exit gracefully
    except FileNotFoundError:
        print("Data is missing. Try running 'Update Data' from the main menu")
        return None


# retrieve closing prices from the data file
def get_closing_prices(ticker):
    # check if it exists
    try:
        path = Path(__file__).parent.absolute().parent
        df = pd.read_csv(path / "data" / "closing_prices.csv", index_col=0)
        # return as a list
        return list(df.loc[ticker.upper()].items())
    # if it doesn't, print a message and exit gracefully
    except FileNotFoundError:
        print("Data is missing. Try running 'Update Data' from the main menu")
        return None
