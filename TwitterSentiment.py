import tweepy
import time
from textblob import TextBlob

consumer_key = 'XxaNxxOaFAm1eXneisL2iWoOc'
consumer_secret = 'vXNxjXFicYT5LmLPOywMee6ghNOfxgK5Xh9EBiqeq1HWCGNHEk'

access_token = '1161490543899271169-YcTJx6pFKktOEgoHDoY8hmLdEGbPYO'
access_token_secret = 'vWaulJlmyrsv27iPCPEHjTTT3My9zFJQuxW3MXjmW5yyP'

auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

total = 0
overall_rating = 0

running_time = 3600
current_time = 0

current_tweets = []

user_input = input("Enter keyword to search for: ")

while current_time <= running_time:
    public_tweets = api.search(user_input)
    batch_rating = 0
    i = 0
    for tweet in public_tweets:
        if tweet.text not in current_tweets:
            current_tweets.append(tweet.text)
            analysis = TextBlob(tweet.text)
            i += 1
            batch_rating += analysis.sentiment.polarity
            if len(current_tweets) > 20:
                current_tweets.pop(0)

    overall_rating += batch_rating
    total += i

    print('Overall Rating: ' + str(overall_rating))
    print('Average Rating: ' + str(overall_rating/total))
    print('Total Number: ' + str(total))
    time.sleep(2.5)
    current_time += 2.5
