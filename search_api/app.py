import numpy as np
import pandas as pd
import tweepy
import sys
import os

import config

consumer_key = config.twitter_anidata_consumer_key
consumer_secret = config.twitter_anidata_consumer_secret
access_token = config.twitter_anidata_access_token
access_token_secret = config.twitter_anidata_access_token_secret

# App Only Auth gives higher limit, 18k tweets/hr
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
# wait_on_rate_limit/wait_on_rate_limit_notify calls auto wait when rate limit is reached
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
if(not api):
    print("Can't Authenticate")
    sys.exit(-1)

query = 'atlanta OR atl OR #atlanta OR #atl'  # what we're searching for
fName = 'tweets.csv'
tweetCount = 100

# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
# "Returns results with an ID greater than (that is, more recent than) the specified ID. 
# There are limits to the number of Tweets which can be accessed through the API. If the 
# limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available."
sinceId = None
# "Returns results with an ID less than (that is, older than) or equal to the specified ID."
max_id = -1

# return tweets before the given date (optional)
until_date = '2018-10-07'

count = 0
with open(fName, 'a') as f:
    while True:
        try:
            if (max_id <= 0):
                # to the beginning of twitter time
                if (not sinceId):
                    results = api.search(q=query, count=tweetCount, lang='en', until=until_date)
                # go to last tweet we downloaded
                else:
                    results = api.search(q=query, since_id=sinceId, count=tweetCount, lang='en', until=until_date)

            # if max_id > 0 
            else:
                # results from beginning of twitter time to max_id
                if (not sinceId):
                    results = api.search(q=query, max_id=str(max_id - 1), count=tweetCount, lang='en', until=until_date)
                # results from since_id to max_id
                else:
                    results = api.search(q=searchQuery, count=tweetCount,
                                         max_id=str(max_id - 1),
                                         since_id=sinceId,
                                         lang = 'en',
                                         until=until_date)
            if not results:
                print("No more tweets found")
                break
                
            for result in results:
                tweets_DF = pd.DataFrame({"created_at": [x.created_at for x in results],
                						  "text": [x.text for x in results], 
                						  "geo": [x.geo for x in results],
                						  "coordinates": [x.coordinates for x in results],
                						  "place": [x.place for x in results],
                						  "retweet_count": [x.retweet_count for x in results],
                						  "favorite_count": [x.favorite_count for x in results],
                						  "favorited": [x.favorited for x in results],
                						  "retweeted": [x.retweeted for x in results]
                                          }, 
                                          index =[x.id for x in results])
                tweets_DF.name = 'Tweets'
                tweets_DF.index.name = "ID"
                tweets_DF.to_csv(f, header=False)
                
            count += len(results)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = results[-1].id
        except (KeyboardInterrupt, SystemExit):
        	print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, os.path.abspath(fName)))
        	quit()
        except tweepy.TweepError as e:
            print("Error : " + str(e))
            break


print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
