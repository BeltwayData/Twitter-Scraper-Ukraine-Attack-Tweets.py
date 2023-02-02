import snscrape.modules.twitter as sntwitter
import pandas as pd

query = 'Ukraine AND attack'
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
 #   print(vars(tweet))
 #   break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.coordinates, tweet.place,])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet', 'Coordinates', 'Place'])

print(df)

df.to_csv('tweets100.csv', index=False)