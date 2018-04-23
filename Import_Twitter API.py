'''
(1) API Authentication
TASKS:
Import the package tweepy.
Pass the parameters consumer_key and consumer_secret to the function tweepy.OAuthHandler().
Complete the passing of OAuth credentials to the OAuth handler auth by applying to it the method set_access_token(), 
along with arguments access_token and access_token_secret.

'''

# Import package
import tweepy

# Store OAuth authentication credentials in relevant variables

access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

'''
(2) Streaming tweets

TASKS: create the Streamobject and to filter tweets according to particular keywords.

- Create your Stream object with authentication by passing tweepy.Stream() the authentication handler auth and the Stream listener l;
- To filter Twitter streams, pass to the track argument in stream.filter() a list containing the desired keywords 'clinton', 'trump', 'sanders', and 'cruz'.

'''
# Initialize Stream listener
l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
stream.filter(track = ['clinton', 'trump', 'sanders', 'cruz'])


'''
Code for the tweet Stream Listener Class:
Defined a Tweet listener that creates a file called 'tweets.txt', collects streaming tweets as .jsons 
and writes them to the file 'tweets.txt'; once 100 tweets have been streamed, the listener closes the file and stops listening.
'''

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
print(status)


'''
(3) Load and explore your Twitter data

TASKS:
    Assign the filename 'tweets.txt' to the variable tweets_data_path.
    Initialize tweets_data as an empty list to store the tweets in.
    Within the for loop initiated by for line in tweets_file:, load each tweet into a variable, tweet, using json.loads(), then append tweet to tweets_data using the append() method.
    Hit submit and check out the keys of the first tweet dictionary printed to the shell.
'''
# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())


'''
(4) Twitter Data to DataFrame

'''
