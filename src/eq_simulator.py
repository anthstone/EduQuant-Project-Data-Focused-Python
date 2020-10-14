import eq_data
import eq_utilities
import pandas as pd
from datetime import date, datetime
from pathlib import Path


def sell_stock(ticker, portfolio):
    if ticker.upper() not in portfolio.index:
        print("-----------Ticker not in portfolio")
        print()
        print()
    else:
        price = portfolio.loc[ticker.upper()]["Current Price"]
        portfolio.at["Cash", "Current Price"] += price
        # profit
        profit = (
            portfolio.loc[ticker.upper()]["Current Price"]
            - portfolio.loc[ticker.upper()]["Purchase Price"]
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
    elif closing_price > portfolio.loc["Cash"]["Current Price"]:
        print("-----------Not enough cash!")
        print()
        print()
    else:
        today = date.today().strftime("%B %d, %Y")
        portfolio.loc[ticker.upper()] = {
            "Date Purchased": today,
            "Time held (days)": 0,
            "Current Price": closing_price,
            "Purchase Price": closing_price,
            "Change since purchase": 0,
        }

        portfolio.at["Cash", "Current Price"] -= closing_price

    save_portfolio(portfolio)

    return portfolio


def update_portfolio(portfolio):
    today = datetime.today()
    for idx, row in portfolio.iterrows():
        if idx != "Cash":
            d = datetime.strptime(row["Date Purchased"], "%B %d, %Y")
            time_held = (today - d).days
            current_price = eq_data.get_closing_prices(idx)[0][1]
            change = current_price - row["Purchase Price"]

            portfolio.at[idx, "Current Price"] = current_price
            portfolio.at[idx, "Change since purchase"] = change
            portfolio.at[idx, "Time held (days)"] = time_held

    return portfolio


def load_portfolio():
    try:
        path = Path(__file__).parent.absolute().parent
        portfolio = pd.read_csv(path / "data" / "portfolio.csv", index_col="Ticker")
        portfolio = update_portfolio(portfolio)
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
            "Change since purchase": 0,
        }
        save_portfolio(portfolio)

    return portfolio


def save_portfolio(portfolio):
    portfolio.to_csv(path / "data" / "portfolio.csv")


def print_sim_menu():
    portfolio = load_portfolio()
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
