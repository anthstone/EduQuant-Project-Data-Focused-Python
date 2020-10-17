# eq_utilities.py
# Description: modules containing many miscellaneous helper functions
# Authors: Anthony Stone
#          Alexander Talbott
#          Jim Wang


import os
import matplotlib.pyplot as plt

# because it looks nice
plt.style.use("fivethirtyeight")

# a list of all tickers in EduQuant
def get_tech_stocks():
    tech_stocks = [
        "AAPL",
        "ADBE",
        "ADI",
        "ADSK",
        "AMAT",
        "AMD",
        "ANSS",
        "ASML",
        "AVGO",
        "BIDU",
        "CDNS",
        "CDW",
        "CERN",
        "CHKP",
        "CSCO",
        "CTSH",
        "CTXS",
        "DOCU",
        "FB",
        "GOOG",
        "GOOGL",
        "INTC",
        "INTU",
        "KLAC",
        "LRCX",
        "MCHP",
        "MSFT",
        "MU",
        "MXIM",
        "NTES",
        "NVDA",
        "NXPI",
        "QCOM",
        "SNPS",
        "SPLK",
        "SWKS",
        "TXN",
        "VRSN",
        "WDAY",
        "WDC",
        "XLNX",
        "BABA",
        "TSLA",
        "CRM",
        "PYPL",
        "ATVI",
        "EA",
        "MTCH",
        "ZG",
        "TTD",
        "AMZN",
        "ORCL",
        "SAP",
        "IBM",
        "VMW",
        "HPQ",
        "DDD",
        "ACIW",
        "ADTN",
        "AKAM",
        "MDRX",
        "ALTR",
        "DOX",
        "AZPN",
        "CACI",
        "CIEN",
        "CRUS",
        "CVLT",
        "GLW",
        "CREE",
        "DBD",
        "EQIX",
        "FFIV",
        "FICO",
        "GRMN",
        "IT",
        "GWRE",
        "IDCC",
        "JCOM",
        "JNPR",
        "LHX",
        "LDOS",
        "MRVL",
        "MSI",
        "NCR",
        "NTAP",
        "NLOK",
        "NUAN",
        "ON",
        "PANW",
        "PBI",
        "PLT",
        "PRGS",
        "PTC",
        "SAIC",
        "STX",
        "SMTC",
        "NOW",
        "SLAB",
        "SSNC",
        "SYNA",
        "TDC",
        "TER",
        "TWTR",
        "TYL",
        "VSAT",
        "VIAV",
    ]
    return tech_stocks


# generate a line plot from a list of tuples and a given title
def print_line_plot(list_of_tuples, title):
    unpacked = list(zip(*list_of_tuples))
    plt.figure(figsize=(30, 15))
    plt.plot(unpacked[0], unpacked[1])
    plt.title(title.upper())
    plt.xticks(rotation=45, ha="right")
    plt.savefig(title + ".png")
    print("Chart has been saved to the current directory")


# check if the user inputted ticker is supported in EduQuant
def get_ticker_input():
    while True:
        ticker = input("Type the ticker of the stock you want to select: ")
        if ticker.upper() in get_tech_stocks():
            return ticker
        else:
            print("Not a valid ticker. Try again.")


# taken from https://www.tutorialspoint.com/how-to-clear-screen-in-python
def screen_clear():
    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")
