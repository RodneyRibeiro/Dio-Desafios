"""
Docstring
"""
import tweepy
import os

def authenticate():
    """
    :return:
    """
    consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def fetch_tweets(api, query, count=100):
    """
    :param api:
    :param query:
    :param count:
    :return:
    """
    tweets = api.search_tweets(q=query, count=count, lang='en')
    return tweets