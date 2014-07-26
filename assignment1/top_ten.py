'''
Created on Jul 13, 2014

@author: Zheng
'''
import json
import sys
import operator

def main():
    tweet_file = open(sys.argv[1])
    hash_dict = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if tweet.get("entities") == None:
            continue            
        hashtag_list = tweet.get("entities").get("hashtags")
        if not hashtag_list:
            continue
        for hashtag in hashtag_list:
            hash_text = hashtag.get("text").encode('utf-8')
            if hash_text in hash_dict:
                hash_dict[hash_text] += 1
            else:
                hash_dict[hash_text] = 1 
    sorted_hash = sorted(hash_dict.iteritems(), key=operator.itemgetter(1))
    sorted_hash.reverse()
    for hasht in sorted_hash[:10]:
        print (hasht[0] + " " + str(hasht[1]))
    
if __name__ == '__main__':
    main()
