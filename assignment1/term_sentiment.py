import sys
import re
import json

def get_tweet_score(tweet, scores):
    sent_sum = 0;
    words = re.sub("[^\w]", " ",  tweet.encode('utf-8')).split()
    for word in words:
        if word.lower() in scores:
            sent_sum += int(scores[word.lower()])
    return sent_sum

def term_score(sent_file):
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    old_term_scores = term_score(sent_file)
    new_term_scores = {}
    
    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            tweet_score = get_tweet_score(tweet["text"], old_term_scores)
            words = re.sub("[^\w]", " ",  tweet["text"].encode('utf-8')).split()
            for word in words:
                if word in new_term_scores:
                    new_term_scores[word] += tweet_score
                else:
                    new_term_scores[word] = tweet_score
    
    for new_term in new_term_scores:
        print (new_term + " " + str(new_term_scores[new_term]))
                
if __name__ == '__main__':
    main()
