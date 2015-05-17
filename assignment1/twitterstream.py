import oauth2 as oauth
import urllib2 as urllib
import csv
import re
import json

# See assignment1.html instructions or README for how to get these credentials

api_key = "qLobLu6KzPlu4C5b7mCFshvzx"
api_secret = "oTVqZfdLya2KOvZmSzSqctWubQgxBaQ1NXqmhCWHZcU3PX9yp5"
access_token_key = "38148772-J6wKht8EnvffR2CwRXyp9SjaI1o9Ep4oIPJhps40G"
access_token_secret = "MOd2QoYMIbFAoKUjH9SxO6sXdJxuH78CtXO2vdhAStTeI"

_debug = 0

oauth_token		= oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler	= urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
	req = oauth.Request.from_consumer_and_token(oauth_consumer,
												token=oauth_token,
	   										    http_method=http_method,
												http_url=url, 
												parameters=parameters)

	req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

	headers = req.to_header()

	if http_method == "POST":
		encoded_post_data = req.to_postdata()
	else:
		encoded_post_data = None
		url = req.to_url()

	opener = urllib.OpenerDirector()
	opener.add_handler(http_handler)
	opener.add_handler(https_handler)

	response = opener.open(url, encoded_post_data)

	return response

def fetchsamples():
	url = "https://stream.twitter.com/1/statuses/sample.json"
	parameters = []
	response = twitterreq(url, "GET", parameters)
	for line in response:
		print line.strip()

def parse_users(input_file):
	user_list = []
	with open(input_file, 'rb') as csv_input:
		reader = csv.reader(csv_input)
		for row in reader:
			user = re.search('https://twitter.com/(.*)', row[0])
			user_list.append(user.group(1))
	return user_list		
	
def fetchTweets(users):
	url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
	parameters = {}
	for user in users:
		parameters['screen_name'] = user
		response = twitterreq(url, "GET", parameters)
		line = response.read()
		tweets = json.loads(line)
		output_file = user+'.csv'
		fieldnames = ['text', 'Time', '@']
		with open(output_file, 'wb') as csv_output:
			writer = csv.writer(csv_output, delimiter='\t')
			for tweet in tweets:
				row = (
		        	tweet['id'],                    # tweet_id
		            tweet['created_at'],            # tweet_time
		            tweet['user']['screen_name'],   # tweet_author
		            tweet['user']['id_str'],        # tweet_authod_id
		            tweet['text']                   # tweet_text
		        )
				values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
				writer.writerow(values)
			
if __name__ == '__main__':
	users = parse_users('sample.csv')
	fetchTweets(users)
