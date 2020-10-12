import eq_data
import eq_simulator
import eq_stocks
import eq_utilities


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
            eq_utilities.screen_clear()
            eq_data.update_data()
        # Exit
        elif response == 5:
            break


def main():
    # main menu, start interaction
    main_menu()
    print("See you later!")


if __name__ == "__main__":
    main()
