import tweepy, time, sys
from good_morning import getString
from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

#Tweet every 24 hours
INTERVAL = 60 * 60 * 24

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# Time from https://www.programiz.com/python-programming/datetime/current-time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

