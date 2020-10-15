# news_scrape.py
# Description: scrapes news stories from Google Finance
# Authors: Anthony Stone
#          Alexander Talbott
#          Jim Wang


from bs4 import BeautifulSoup
from urllib.request import urlopen
import certifi
import ssl


def print_news():
    # using soup pacakge to open url, google finance, and creating soup object
    html = urlopen(
        "https://www.google.com/finance",
        context=ssl.create_default_context(cafile=certifi.where()),
    )
    soup = BeautifulSoup(html.read(), "html.parser")

    # initializing lists to add the elements later on
    articles = []
    links = []
    source = []
    time = []

    # in each for loop, finding the information I want through class ID, and appending to lists above
    for item in soup.findAll("div", attrs={"class": "AoCdqe"}):
        articles.append(item.text)

    for item in soup.findAll("div", attrs={"class": "sfyJob"}):
        source.append(item.text)

    for item in soup.findAll("div", attrs={"class": "Adak"}):
        time.append(item.text)

    for item in soup.findAll("a"):
        if "href" in item.attrs and "jslog" in item.attrs and "target" in item.attrs:
            links.append(str(item.attrs["href"]))

    print("These are the top articles on Google Finance!")

    # printing the lists of information
    for i in range(len(articles)):
        print(str(i + 1) + ": " + articles[i])
        print("Source: " + source[i])
        print("Time: " + time[i])
        print("Link: " + links[i])
        print("\n")
