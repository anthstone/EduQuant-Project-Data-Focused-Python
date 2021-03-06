# eq_stocks.py
# Description: module that handles most of the stock functionality
# Authors: Anthony Stone
#          Alexander Talbott
#          Jim Wang


import eq_utilities
import eq_data
import eq_twitter
import math

stock_list = eq_utilities.get_tech_stocks()

# get the twitter timeline of a given ticker and display it
def get_tweets(ticker):
    print(f"Recent tweets for {ticker.upper()}")
    print()
    print()
    # get corresponding handle from ticker
    handle = eq_twitter.retrieve_handle_from_ticker(ticker)
    # scrape the timeline of tweets
    timeline = eq_twitter.scrape_timeline(handle)

    for tweet in timeline:
        print(tweet)
        print()

    print()
    input("Press enter to return...")
    eq_utilities.screen_clear()


# get a ticker's corresponding financial statistics and display them
def get_finance_stats(ticker):
    finance_stats = eq_data.get_finance_stats(ticker)
    if finance_stats is None:
        return

    print(f"Financial statistics for {ticker.upper()}")
    print()
    print()

    for i in finance_stats:
        print("{:<15s}".format(i + ":"), "\t\t", end="")

        # change "nan" to "N/A" for prettier printing
        if type(finance_stats[i]) == float:
            if math.isnan(finance_stats[i]):
                to_print = "N/A"
            else:
                to_print = str(round(finance_stats[i], 2))
        else:
            to_print = str(finance_stats[i])
        # make them look pretty
        print("{:>15s}".format(to_print))

    print()
    input("Press enter to return...")
    eq_utilities.screen_clear()

    return


# get recent closing prices from a given ticker
def get_stock_prices(ticker):
    closing_prices = eq_data.get_closing_prices(ticker)
    if closing_prices is None:
        return

    print(f"Stock prices for {ticker.upper()}")
    print()
    print()

    # print headers
    print("Date", "\t\t\t", "Closing Price", "\t\t", "Change")

    # print weekly price
    # every 5 days = once a week
    for idx, val in enumerate(closing_prices[::5]):
        print(val[0] + ":", end="")
        # print it pretty
        print("\t\t", "{:>6}".format(val[1]), "\t\t", end="")

        # calculate the difference of a closing price compared
        # to the closing price of one week ago (one week = 5 business days)
        if idx * 5 < len(closing_prices) - 5:
            diff = float(val[1]) - float(closing_prices[idx * 5 + 5][1])
            # print it pretty
            print("{0:>6.2f}".format(diff))
        else:
            print()

    print()
    # build a line plot of the recent closing prices
    response = input("Would you like to generate a graph?(y/n): ")
    if response.lower() == "y":
        eq_utilities.print_line_plot(closing_prices, ticker)

    print()
    input("Press enter to return...")
    eq_utilities.screen_clear()

    return


def print_stock_list():
    print("All stocks in EduQuant:")
    # zip into 8 lists in order to display 8 columns
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


def print_stock_menu():
    # event loop
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
            ticker = eq_utilities.get_ticker_input()
            eq_utilities.screen_clear()
            get_stock_prices(ticker)
        # Check a company's financial statistics
        if response == 3:
            ticker = eq_utilities.get_ticker_input()
            eq_utilities.screen_clear()
            get_finance_stats(ticker)
        # Read a company's tweets
        if response == 4:
            ticker = eq_utilities.get_ticker_input()
            eq_utilities.screen_clear()
            get_tweets(ticker)
        # Back to main menu
        elif response == 5:
            eq_utilities.screen_clear()
            break
