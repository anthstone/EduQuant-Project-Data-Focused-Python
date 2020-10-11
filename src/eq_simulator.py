import eq_utilities
import pandas as pd


def load_portfolio():
    try:
        portfolio = pd.read_csv("../data/portfolio.csv", index_col="Ticker")
    except:
        portfolio = pd.DataFrame(
            columns=[
                "Ticker",
                "Date Purchased",
                "Time held (days)",
                "Price",
                "Change since purchase",
            ],
        )
        portfolio.set_index("Ticker")

    return portfolio


def save_portfolio(portfolio):
    portfolio.to_csv("../data/portfolio.csv")


def print_sim_menu():
    while True:
        portfolio = load_portfolio()
        print("EduQuant Stock Simulator")
        print()
        print()
        if portfolio.empty:
            print("No portfolio yet! Buy some stocks to get started.")
        else:
            print(portfolio)
        print()
        print()
        print("What would you like to do?")

        print("1. Purchase a stock")
        print("2. Sell a stock")
        print("3. Generate a graph of my portfolio")
        print("4. Back to main menu")

        # validate input
        response = input()
        try:
            response = int(response)
        except:
            eq_utilities.screen_clear()
            print("Not a valid response. Try again!")
            continue

        # sanity checks
        if response > 4 or response < 1:
            eq_utilities.screen_clear()
            print("Not a valid response. Try again!")
            continue
        # else we're all good

        # TODO
        # Purchase a stock
        if response == 1:
            ticker = eq_utilities.get_ticker_input()
            eq_utilities.screen_clear()
            # purchase_stock(ticker)
        # TODO
        # Sell a stock
        if response == 2:
            ticker = eq_utilities.get_ticker_input()
            eq_utilities.screen_clear()
            # sell_stock(ticker)
        # TODO
        # Generate a graph of my portfolio
        if response == 3:
            eq_utilities.screen_clear()
            # eq_utilities.print_line_plot(list_of_tuples, title)
        # Back to main menu
        if response == 4:
            eq_utilities.screen_clear()
            break


if __name__ == "__main__":
    print_sim_menu()
