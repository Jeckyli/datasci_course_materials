'''
Created on Jul 13, 2014

@author: Zheng
'''
from __future__ import division

import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])
    term_dict = {}
    term_total = 0
    for line in tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            words = re.sub("[^\w]", " ",  tweet["text"].encode('utf-8')).split()
            for word in words:
                term_total += 1
                if word in term_dict:
                    term_dict[word] += 1
                else:
                    term_dict[word] = 1
    
    for term in term_dict:
        print (term + " " + str(term_dict[term]/term_total))
                   
if __name__ == '__main__':
    main()