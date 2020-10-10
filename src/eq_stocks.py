import eq_utilities
import eq_data
import tech_stocks
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

stock_list = tech_stocks.get_tech_stocks()


# TODO
def get_tweets(ticker):
    print(f"Tweets for {ticker}")

    response = input()
    eq_utilities.screen_clear()


# TODO
def get_finance_stats(ticker):
    print(f"Financial statistics for {ticker}")
    finance_stats = eq_data.get_finance_stats(ticker)

    print(finance_stats)
    response = input()
    eq_utilities.screen_clear()


def get_stock_prices(ticker):
    print(f"Stock prices for {ticker.upper()}")
    print()
    print()
    closing_prices = eq_data.get_closing_prices(ticker)

    # print headers
    print("Date", "\t\t\t", "Closing Price", "\t\t", "Change")

    # print weekly price
    for idx, val in enumerate(closing_prices[::5]):
        print(val[0] + ":", end="")
        print("\t\t", "{:>6}".format(val[1]), "\t\t", end="")

        if idx * 5 < len(closing_prices) - 5:
            diff = float(val[1]) - float(closing_prices[idx * 5 + 5][1])
            print("{0:>6.2f}".format(diff))
        else:
            print()

    print()
    response = input("Would you like to generate a graph?(y/n): ")
    if response.lower() == "y":
        print_line_plot(closing_prices, ticker)

    print()
    input("Press enter to return...")
    eq_utilities.screen_clear()


def print_line_plot(list_of_tuples, ticker):
    unpacked = list(zip(*list_of_tuples))
    plt.figure(figsize=(30, 15))
    plt.plot(unpacked[0], unpacked[1])
    plt.title(ticker.upper())
    plt.xticks(rotation=45, ha="right")
    plt.savefig("plot.png")


def print_stock_list():
    print("All stocks in EduQuant:")
    print_list = zip(
        stock_list[::8],
        stock_list[1::8],
        stock_list[2::8],
        stock_list[3::8],
        stock_list[4::8],
        stock_list[5::8],
        stock_list[6::8],
        stock_list[7::8],
    )
    for l in print_list:
        for i in l:
            print("{:<8s}".format(i), end="")
        print()


def get_ticker_input():
    while True:
        ticker = input("Type the ticker of the stock you want to select: ")
        if ticker.upper() in stock_list:
            return ticker
        else:
            print("Not a valid ticker. Try again.")


def print_stock_menu():
    while True:
        print(
            """
            EduQuant focuses on the tech stock market. There are over 100 tech stocks available in this application for you to 
            explore. You can look at each stock's information including their historical prices, tweets from the company, and 
            advanced financial statistics to inform your stock purchases.
            """
        )
        print()
        print("What would you like to do?")
        print("1. See list of stocks")
        print("2. Check a company's stock prices")
        print("3. Check a company's financial statistics")
        print("4. Read a company's tweets")
        print("5. Back to main menu")

        # validate input
        response = input()
        try:
            response = int(response)
        except:
            eq_utilities.screen_clear()
            print("Not a valid response. Try again!")
            continue

        # sanity checks
        if response > 5 or response < 1:
            eq_utilities.screen_clear()
            print("Not a valid response. Try again!")
            continue
        # else we're all good

        # See list of stocks
        if response == 1:
            eq_utilities.screen_clear()
            print_stock_list()
        # Check a company's stock prices
        if response == 2:
            ticker = get_ticker_input()
            eq_utilities.screen_clear()
            get_stock_prices(ticker)
        # Check a company's financial statistics
        if response == 3:
            ticker = get_ticker_input()
            eq_utilities.screen_clear()
            get_finance_stats(ticker)
        # Read a company's tweets
        if response == 4:
            ticker = get_ticker_input()
            eq_utilities.screen_clear()
            get_tweets(ticker)
        # Back to main menu
        elif response == 5:
            eq_utilities.screen_clear()
            break
