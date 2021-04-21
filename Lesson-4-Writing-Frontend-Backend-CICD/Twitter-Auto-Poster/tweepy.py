  
import tweepy


# Auth keys. Only put API and tokens in your script for testing only!!!
# Never commit to a public repository.
api_key = ''
api_secret = ''
access_token = ''
access_token_secret = ''

# Authenticate via the API key/secret and the access token/secret
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

# Error handling for authentication errors
try:
    api = tweepy.API(auth)

except tweepy.TweepError:
    print('Error! Failed to authenticate')

# Create a new tweet
api.update_status("Posting from Python")