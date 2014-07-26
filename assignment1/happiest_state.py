'''
Created on Jul 13, 2014

@author: Zheng
'''

import json
import sys
import re
import operator

def get_tweet_score(tweet, scores):
    sent_sum = 0;
    words = re.sub("[^\w]", " ",  tweet.encode('utf-8')).split()
    for word in words:
        if word.lower() in scores:
            sent_sum += int(scores[word.lower()])
    return sent_sum

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = {}
    state_happiness_dict = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    for line in tweet_file:
        tweet = json.loads(line)
        if "text" not in tweet:
            continue
        if "place" in tweet:
            if tweet.get("place") != None:
                place = tweet["place"]
#                 print place
                if ("country_code" in place and place["country_code"] == "US"):
                    m = re.search("\w+, (\w+)", tweet["place"]["full_name"])
                    state = m.group(1)
            
                    if state in state_happiness_dict:
                        state_happiness_dict[state] += get_tweet_score(tweet["text"], scores)
                    else:
                        state_happiness_dict[state] = get_tweet_score(tweet["text"], scores)
                
    print max(state_happiness_dict.iteritems(), key=operator.itemgetter(1))[0]
          
if __name__ == '__main__':
    main()