import eq_utilities
import eq_stocks
import eq_data


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
            print("Not a valid response. Try again!")
            continue

        # sanity checks
        if response > 5 or response < 1:
            eq_utilities.screen_clear()
            print("Not a valid response. Try again!")
            continue
        # else we're all good

        # See stocks
        if response == 1:
            eq_utilities.screen_clear()
            # stock menu event loop
            eq_stocks.print_stock_menu()
        # TODO
        # Stock simulator
        elif response == 2:
            eq_utilities.screen_clear()
            pass
        # TODO
        # See recent financial news
        elif response == 3:
            eq_utilities.screen_clear()
            pass
        # Update data
        elif response == 4:
            eq_utilities.screen_clear()
            eq_data.update_data()
        # Exit
        elif response == 5:
            break


def main():
    # load data from files

    # main menu, start interaction
    main_menu()
    print("See you later!")


if __name__ == "__main__":
    main()
