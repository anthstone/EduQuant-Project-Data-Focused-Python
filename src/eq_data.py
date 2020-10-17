# eq_data.py
# Description: module to handle data retrieval
# Authors: Anthony Stone
#          Alexander Talbott
#          Jim Wang


import pandas as pd
from pathlib import Path


# get the company's name from its ticker
def get_name(ticker):
    path = Path(__file__).parent.absolute().parent
    df = pd.read_csv(path / "data" / "company_list.csv", index_col=0)
    return df[df["Stock Code"].str.contains(ticker)]["Company Name"].values[0]


# retrieve financial statistics from the data file
def get_finance_stats(ticker):
    # check if it exists
    try:
        path = Path(__file__).parent.absolute().parent
        df1 = pd.read_csv(path / "data" / "finance_stats.csv", index_col=0)
        df2 = pd.read_csv(path / "data" / "SEC_data_table.csv", index_col=0)

        # get the company's full name
        company_name = get_name(ticker)
        # grab the most recent accounts payable
        ap_dict = df2[df2["name"].str.contains(company_name)]["value"]
        most_recent_ap = next(iter(ap_dict))

        # return as a dict
        d = df1.loc[ticker.upper()].to_dict()
        d["Accounts Payable"] = most_recent_ap

        return d
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
