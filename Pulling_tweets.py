#Day1 about how to pull tweets from the Twitter account 
import tweepy
consumer_key = "entering the key here"
consumer_secret = "entering the key here"
access_token = "entering the key here"
access_token_secret = "entering the key here"


from tweepy.auth import OAuthHandler
#Creating the Auth Object
auth = OAuthHandler(consumer_key, consumer_secret)
#Setting the access token and secret
auth.set_access_token(access_token, access_token_secret)
#Creating the API object while passing in the auth info
api = tweepy.API(auth)

#Testing the API to get tweets from home timeline, and storing it in public_tweets variable
public_tweets = api.home_timeline()
#Printing each tweet
for tweet in public_tweets:
    print (tweet.text)
 
#This should print the first 15 tweets from your home Twitter account. 
#This data can be used for Text mining

#To refer to specific attributes of each tweet object, we have to look at the JSON returned by the Twitter API.
#Day 2 about extracting specific attributes
