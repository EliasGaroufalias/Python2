import tweepy
import string
import re
from tweepy import OAuthHandler

consumer_key = 'placeholder'
consumer_secret = 'placeholder'
access_token = 'placeholder'
access_secret = 'placeholder'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweets=''
while True:
	try:
		username = raw_input("\nGive desired user's username:\n\n\t")
		for status in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode = 'extended').items(10):
			tweets += status._json['full_text']
			tweets += ' '
		break
	except:
		print '\nWrong Input, try again\n\n\n'
tweets = tweets.split()
for i in range(len(tweets)):
	tweets[i] = tweets[i].lower()
	tweets[i] = re.sub('['+string.punctuation+']', ' ', tweets[i])
	
c=[0]*len(tweets)
for i in range(len(tweets)):
	for j in range(len(tweets)):
		if tweets[i]==tweets[j]:
			c[i]+=1

maxx=c[0]
maxi=0
for i in range(1,len(c)):
	if c[i]>maxx:
		maxx=c[i]
		maxi=i
print "\n\nThe most popular word from user '" + username + "' einai '" + tweets[maxi] + "'"

#todo: input checks and co.
