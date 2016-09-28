#!/usr/bin/python
# -*- coding: utf-8 -*-
import oauth2
import json

CONSUMER_KEY = "XHU7ZKKYsqQca3FNwmFH7jgVG"
CONSUMER_SECRET = "D4DRagebN8Memx1ypqrkqFhEA7U61xdu6E3mCpgeQGt4cuZZJg"
key = "780744354688212992-2XEZqPj0HR4UbsjCR2Y3CDyK80SfeEM"
secret="UW1ximTxoinuX6bthyPahXSfK4BWACt53KGwH9ABVixtV"

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    content=content[0:(len(content))]
    foll=json.loads(content)
    print content
    for data in foll:
    	print data["followers_count"]
    	print data["statuses_count"]
    return content

oauth_req( 'https://api.twitter.com/1.1/users/lookup.json?screen_name=narendramodi', key, secret )