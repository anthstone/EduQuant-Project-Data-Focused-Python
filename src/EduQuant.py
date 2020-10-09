import os

# taken from https://www.tutorialspoint.com/how-to-clear-screen-in-python
def screen_clear():
    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")


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

        response = input()
        try:
            response = int(response)
        except:
            screen_clear()
            print("Not a valid response. Try again!")
            continue

        # sanity checks
        if response > 5 or response < 1:
            screen_clear()
            print("Not a valid response. Try again!")
            continue
        # else we're all good

        # See stocks
        if response == 1:
            screen_clear()
            pass
        # Stock simulator
        elif response == 2:
            screen_clear()
            pass
        # See recent financial news
        elif response == 3:
            screen_clear()
            pass
        # Update data
        elif response == 4:
            screen_clear()
            pass
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
