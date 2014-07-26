import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    
def tweet_score(tweet, scores):
    sent_sum = 0;
    words = re.sub("[^\w]", " ",  tweet.encode('utf-8')).split()
    for word in words:
        if word.lower() in scores:
            sent_sum += int(scores[word.lower()])
    return str(sent_sum)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            print tweet_score(tweet["text"], scores)

if __name__ == '__main__':
    main()
