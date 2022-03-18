
import tweepy
api_key="" #twitter developer api key
api_key_secret=""#twitter developer api key secrete
access_token="" #twitter developer access token
access_token_secret=""#twitter developer access token secrete
bearer_token="" #twitter developer bearer token

#initialize a new tweepy instance
client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret, wait_on_rate_limit=True)



def followUser(username):
    user=client.get_user(username=username)
    client.follow_user(target_user_id=user[0].id)

def unFollowUser(username):
    user=client.get_user(username=username)
    client.unfollow_user(target_user_id=user[0].id)

def getUsersFollowers(username):
    user=client.get_user(username=username)
    return client.get_users_followers(id=user[0].id, max_results=10).data

def getUsersFollowing(username):
    user=client.get_user(username=username)
    return client.get_users_following(id=user[0].id, max_results=10).data

def searchRecentTweets(query):
    return client.search_recent_tweets(query).data

def getUserTweets(username):
    user=client.get_user(username=username)
    return client.get_users_tweets(id=user[0].id).data

def tweet(text):
    client.create_tweet(text=text)

def likeTweet(tweet_id):
    client.like(tweet_id=tweet_id)

def retweet(tweet_id):
    client.retweet(tweet_id=tweet_id)

def getLikedTweets(username):
    user=client.get_user(username=username)
    return client.get_liked_tweets(id=user[0].id, max_results=10).data

