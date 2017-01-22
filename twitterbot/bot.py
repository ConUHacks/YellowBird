#!/usr/bin/env python
import tweepy, time
from keys import keys
import nuquery, ypquery
from random import randint
import re
keywords = "@butterxxxx #askYP "
counter = randint(0,4)

def getPair(text):
    text = re.sub(keywords, '', text)
    print("\tObtaining a pair of results for "+text)

    output_n = nuquery.query_nuance(str(text))
    print("\tOutput from nuance: "+output_n)

    _json = ypquery.query_yellowp(output_n)
    print("\tOutput from yp:"+str(_json)[:50])

    i1 = randint(0,len(_json))
    i2 = randint(0,len(_json))
    while i1 == i2:
        i2 = randint(0,len(_json))

    return _json[i1]['businessName'], _json[i2]['businessName']

def answer(sn, o1, o2, counter):
    if counter%4 == 0:
        return "@"+sn+" Wow! You have plenty of options. Check "+o1+" or "+o2
    elif counter%4 == 1:
        return "@"+sn+" Here you have two suggestions :) "+o1+" and "+o2
    elif counter%4 == 2:
        return "@"+sn+" Lucky! I found "+o1+" and "+o2+" for you."
    elif counter%4 == 3:
        return "@"+sn+" I hope "+o1+" and "+o2+" are of some help :)"

def login(keys):
    auth = tweepy.OAuthHandler(keys[0], keys[1])
    auth.set_access_token(keys[2], keys[3])
    return tweepy.API(auth)

api = login(keys)

# determine starting point
lastID = api.user_timeline("butterxxxx")[0].id_str
print("starting from ID: "+lastID)

# reset previous answers
for i in range(1,len(api.user_timeline("butterxxxx"))-1):
    print(i)
    # api.destroy_status(api.user_timeline("butterxxxx")[i].id_str)

# listen for new tweets
while True:
    twts = api.search(q=keywords, since_id=lastID)
    if len(twts): lastID = twts[0].id_str

    for s in twts:
        time.sleep(2)
        sn = s.user.screen_name
        print("Found a tweet from "+sn)
        txt = s.text
        # send txt to the back, obtain 2 business names and a link if possible
        o1, o2 = getPair(txt)
        print("\tPair of results: "+o1+","+o2)
        m = answer(sn,o1,o2,counter)
        if len(m)+14 < 140:
            m +=" goo.gl/yWeXRO"
        elif len(m) > 140:
            m = m[:140]
        print("\tGenerated answer: \""+m+"\"")
        counter += 1
        s = api.update_status(m, s.id)

    print("Iteration complete")
    time.sleep(3)
