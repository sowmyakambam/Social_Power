#!/usr/bin/python
# -*- coding: utf-8 -*-
import oauth2
import json
import config
import collections


def oauth_req(url, http_method="GET",
              post_body="", http_headers=None):
    # data1 = []
    print url
    consumer = oauth2.Consumer(key=config.CONSUMER_KEY,
                               secret=config.CONSUMER_SECRET)
    token = oauth2.Token(key=config.key, secret=config.secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(
        url, method=http_method, body=post_body, headers=http_headers)
    content = content[0:(len(content))]
    foll = json.loads(content)
    # print content
    for data in foll:
        print data["text"]
        print data["favorite_count"]
        print data["statuses_count"]
        # data1["followers_count"] = data["followers_count"]
        # data1["statuses_count"] = data["statuses_count"]
        # data1["profile_image_url_https"] = data["profile_image_url_https"]
        # data1["favourites_count"] = data["favourites_count"]
    #     t = (data["followers_count"], data["statuses_count"],
    #          data["profile_image_url_https"], data["favourites_count"])
    #     data1.append(t)
    # j = json.dumps(data1)
    # print j
    # rowarrays_file = 'data.js'
    # f = open(rowarrays_file, 'a')
    # print >> f, j

    # # Convert query to objects of key-value pairs

    # objects_list = []
    # for data in foll:
    #     d = collections.OrderedDict()
    #     d['followers_count'] = data["followers_count"]
    #     d['statuses_count'] = data["statuses_count"]
    #     d['profile_image_url_https'] = data["profile_image_url_https"]
    #     objects_list.append(d)

    # j = json.dumps(objects_list)
    # objects_file = 'data1.js'
    # f = open(objects_file, 'a')
    # print >> f, j
    return content


oauth_req('https://api.twitter.com/1.1/statuses/user_timeline.json?'
          'screen_name=narendramodi')
