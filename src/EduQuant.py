# EduQuant.py
# Description: main module
# Authors: Anthony Stone
#          Alexander Talbott
#          Jim Wang

import eq_simulator
import eq_stocks
import eq_utilities
import yfinance_scrape
import sec_scrape


def main_menu():
    # main event loop
    while True:
        print("Welcome to EduQuant")
        print("Please pick an option below by typing the corresponding number")
        print("1. See stocks")
        print("2. Stock simulator")
        print("3. See recent financial news")
        print("4. Update data")
        print("5. Exit")

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
        if response > 5 or response < 1:
            eq_utilities.screen_clear()
            print("-----------Not a valid response. Try again!")
            print()
            print()
            continue
        # else we're all good

        # See stocks
        if response == 1:
            eq_utilities.screen_clear()
            # stock menu event loop
            eq_stocks.print_stock_menu()
        # Stock simulator
        elif response == 2:
            eq_utilities.screen_clear()
            # simulator menu event loop
            eq_simulator.print_sim_menu()
        # TODO
        # See recent financial news
        elif response == 3:
            eq_utilities.screen_clear()
        # Update data
        elif response == 4:
            while True:
                eq_utilities.screen_clear()
                print("What would you like to update?")
                print("1. Stock closing prices")
                print("2. Stock financial statistics")
                print("3. SEC data")
                print("4. All (Warning: this takes forever)")
                print("5. Back to main menu")

                response = input()

                try:
                    response = int(response)
                except:
                    eq_utilities.screen_clear()
                    print("-----------Not a valid response. Try again!")
                    print()
                    print()
                    continue

                # sanity check
                if response > 5 or response < 1:
                    eq_utilities.screen_clear()
                    print("-----------Not a valid response. Try again!")
                    print()
                    print()
                    continue

                # 1. Stock closing prices
                if response == 1:
                    eq_utilities.screen_clear()
                    yfinance_scrape.update_data("cp")
                # 2. Stock financial statistics
                elif response == 2:
                    eq_utilities.screen_clear()
                    yfinance_scrape.update_data("fs")
                # 3. SEC data
                elif response == 3:
                    eq_utilities.screen_clear()
                    sec_scrape.update_data()
                # 4. All
                elif response == 4:
                    eq_utilities.screen_clear()
                    yfinance_scrape.update_data("cp")
                    yfinance_scrape.update_data("fs")
                    sec_scrape.update_data()
                # 5. Back to main menu
                elif response == 5:
                    eq_utilities.screen_clear()
                    break
        # 5. Back to main menu
        elif response == 5:
            eq_utilities.screen_clear()
            break


def main():
    # main menu, start interaction
    main_menu()
    print("See you later!")


if __name__ == "__main__":
    main()
