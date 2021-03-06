EduQuant

Necessary installs
- python-twitter
  - pip install python-twitter

To Run
- from the main directory
  - python src/EduQuant.py

Files
- src: directory that contains all source code
  - EduQuant.py: main program to be run
  - eq_data.py: handles all data retrieval from `data` directory
  - eq_simulator.py: stock simulator
  - eq_stocks.py: handles all stock data (closing prices/financial statistics)
  - eq_twitter.py: handles all twitter interactions
  - eq_utilities.py: contains many heavily used helper functions
  - news_scrape.py: scrapes recent financial news stories from Google Finance
  - sec_scrape.py: scrapes SEC filing data
  - yfinance_scrape.py: scrapes Yahoo Finance
- data: directory that contains all data files necessary
  - company_list.csv: list of companies and their corresponding stocks that are included in EduQuant
  - closing_prices.csv: recent closing stock prices for all companies in EduQuant
  - finance_stats.csv: current financial statistics for all companies in EduQuant
  - SEC_data_table.csv and sec_fsds: most recent SEC filing data for all companies in EduQuant
  - portfolio.csv: records of user's stock portfolio; the stock they buy and sell as well as their avaliable currency
-Tutorial Video:
	https://youtu.be/AsMuNNs9A6c

Team members
- Anthony Stone - astone2@andrew.cmu.edu
- Jim Wang - tzuching@andrew.cmu.edu
- Alexander Talbott - atalbott@andrew.cmu.edu

Known Issues
- Sometimes on Windows computers, the graphs do not display correctly.
  - For some reason the x and y axes automatically sort.
  - This problem does not happen on Linux or Mac