# eq_simulator.py
# Description: module for stock simulator
# Authors: Anthony Stone
#          Alexander Talbott
#          Jim Wang


import eq_data
import eq_utilities
import pandas as pd
from datetime import date, datetime
from pathlib import Path


def sell_stock(ticker, portfolio):
    # check if the ticker is in the portfolio
    if ticker.upper() not in portfolio.index:
        print("-----------Ticker not in portfolio")
        print()
        print()
    # if not, sell it and add the revenue to Cash
    else:
        price = portfolio.loc[ticker.upper()]["Current Price"]
        portfolio.at["Cash", "Current Price"] += price
        # calculate profit
        profit = (
            # round to 2 places
            round(
                portfolio.loc[ticker.upper()]["Current Price"]
                - portfolio.loc[ticker.upper()]["Purchase Price"],
                2,
            )
        )
        print(f"Your profit from {ticker} is {profit}")

        portfolio.drop(ticker.upper(), inplace=True)

    save_portfolio(portfolio)

    return portfolio


def purchase_stock(ticker, portfolio):
    closing_price = eq_data.get_closing_prices(ticker)[0][1]

    # check if ticker already in portfolio
    if ticker.upper() in portfolio.index:
        print("-----------Ticker already in portfolio")
        print()
        print()
    # if not, buy it (if there is enough Cash)
    elif closing_price > portfolio.loc["Cash"]["Current Price"]:
        print("-----------Not enough cash!")
        print()
        print()
    # create a new portfolio if there isn't one
    else:
        today = date.today().strftime("%B %d, %Y")
        portfolio.loc[ticker.upper()] = {
            "Date Purchased": today,
            "Time held (days)": 0,
            "Current Price": closing_price,
            "Purchase Price": closing_price,
            "Change since purchase": 0.0,
        }

        # subtract purchase price from cash
        portfolio.at["Cash", "Current Price"] -= closing_price

    save_portfolio(portfolio)

    return portfolio


# update the portfolio with current closing prices, dates, and change in price since purchase
def update_portfolio(portfolio):
    today = datetime.today()
    for idx, row in portfolio.iterrows():
        if idx != "Cash":
            # calculate how long the stock has been held
            d = datetime.strptime(row["Date Purchased"], "%B %d, %Y")
            time_held = (today - d).days
            # get the current price of the stock from the data file
            # closing_prices.csv
            current_price = eq_data.get_closing_prices(idx)[0][1]
            change = current_price - row["Purchase Price"]

            portfolio.at[idx, "Current Price"] = current_price
            portfolio.at[idx, "Change since purchase"] = change
            portfolio.at[idx, "Time held (days)"] = time_held

    return portfolio


def load_portfolio():
    # check for the existence of a portfolio data file
    try:
        path = Path(__file__).parent.absolute().parent
        portfolio = pd.read_csv(path / "data" / "portfolio.csv", index_col="Ticker")
        # update it to the current data
        portfolio = update_portfolio(portfolio)
    # if it doesn't exist, start an empty one with $10,000 cash
    except:
        print("No portfolio yet. You have $10,000 to start buying some stocks.")
        portfolio = pd.DataFrame(
            columns=[
                "Ticker",
                "Date Purchased",
                "Time held (days)",
                "Current Price",
                "Purchase Price",
                "Change since purchase",
            ],
        )
        portfolio.set_index("Ticker", inplace=True)
        portfolio.loc["Cash"] = {
            "Date Purchased": "-",
            "Time held (days)": "-",
            "Current Price": 10000.0,
            "Purchase Price": 0,
            "Change since purchase": 0.0,
        }
        save_portfolio(portfolio)

    return portfolio


# save the portfolio to a data file
def save_portfolio(portfolio):
    path = Path(__file__).parent.absolute().parent
    portfolio.to_csv(path / "data" / "portfolio.csv")


def print_sim_menu():
    portfolio = load_portfolio()
    # main event loop
    while True:
        print("EduQuant Stock Simulator")
        print()
        print()
        print(portfolio)
        print()
        print()
        print("What would you like to do?")

        print("1. Purchase a stock")
        print("2. Sell a stock")
        print("3. Back to main menu")

        # validate input
        response = input()
        try:
            response = int(response)
        except:
            eq_utilities.screen_clear()
            print("-----------Not a valid response. Try again!")
            print()
            print()
            continue

        # sanity checks
        if response > 4 or response < 1:
            eq_utilities.screen_clear()
            print("-----------Not a valid response. Try again!")
            print()
            print()
            continue
        # else we're all good

        # Purchase a stock
        if response == 1:
            ticker = eq_utilities.get_ticker_input()
            eq_utilities.screen_clear()
            portfolio = purchase_stock(ticker, portfolio)
        # Sell a stock
        if response == 2:
            ticker = eq_utilities.get_ticker_input()
            eq_utilities.screen_clear()
            portfolio = sell_stock(ticker, portfolio)
        # Back to main menu
        if response == 3:
            eq_utilities.screen_clear()
            break
