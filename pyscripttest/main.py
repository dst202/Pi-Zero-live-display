import tweepy
import time
import os

# Twitter API credentials (Replace with your own keys)
API_KEY = "your-api-key"
API_SECRET = "your-api-secret"
ACCESS_TOKEN = "your-access-token"
ACCESS_SECRET = "your-access-secret"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def fetch_tweets():
    """Fetches latest tweets from the home timeline."""
    try:
        tweets = api.home_timeline(count=5, tweet_mode="extended")
        return [tweet.full_text for tweet in tweets]
    except Exception as e:
        return [f"Error: {str(e)}"]

def display_tweets():
    """Continuously fetches and displays tweets in the terminal."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Clear screen
        tweets = fetch_tweets()
        print("=" * 50)
        for tweet in tweets:
            print("\n".join(tweet.split("\n")[:5]))  # Show first 5 lines
            print("-" * 50)
        time.sleep(30)  # Refresh every 30 seconds

if __name__ == "__main__":
    display_tweets()
