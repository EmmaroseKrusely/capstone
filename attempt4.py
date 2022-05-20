#!/usr/bin/env python
# coding: utf-8

# In[3]:


import GetOldTweets3 as got
import pandas as pd


# In[31]:


def username_tweets_to_csv(username, start_date, end_date, count):
    
    tweetCriteria = got.manager.TweetCriteria().setUsername(username)                                            .setSince(start_date).setUntil(end_date).setMaxTweets(count)
    
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    
    user_tweets = [[tweet.id, tweet.date, tweet.text, tweet.username, tweet.to, tweet.retweets, tweet.favorites, tweet.mentions]]
    
    tweets_df = pd.DataFrame(user_tweets, columns = ['ID','Datetime','Text','User','To','Retweets','Favorites','Mentions'])
    
    tweets_df.to_csv('{}-{}k-tweets.csv'.format(username, int(count/1000)), sep=',')


# In[32]:


username = 'elonmusk'

count = 100

since_date = '2022-5-1'
end_date = '2022-5-2'

username_tweets_to_csv(username, since_date, end_date, count)


# In[ ]:




