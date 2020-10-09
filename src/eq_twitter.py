import twitter
import pandas as pd


api = twitter.Api(
    "xjBcMPKQDKtmS9YOxRjDs2v4T",
    "8sK4L0kYM0VT8UecMu8IPZgd54O8d20uaSnFwiAQvcDz0AWVRB",
    "1309554738543943684-jD3glTsDlofSFWX5DPVFSguZsBRaMp",
    "UbHoxvZky0ZcJQwQ0hpb6oIlDu01Dd3IuMslv0nzVmg2A",
)

# TODO
def retrieve_handle_from_ticker(ticker):
    pass


def scrape_timeline(handle):
    timeline = api.GetUserTimeline(screen_name=handle, count=200)

    df = pd.DataFrame(columns=["Text"])
    for tweet in timeline:
        tweet = tweet.AsDict()
        if "in_reply_to_screen_name" not in tweet:
            df.loc[tweet["id"]] = tweet["text"]

