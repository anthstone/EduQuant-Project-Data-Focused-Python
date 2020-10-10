import news_scrape
import sec_scrape
import yfinance_scrape


def update_data():
    yfinance_scrape.update_data()
    sec_scrape.update_data()
    news_scrape.update_data()
