#!/usr/bin/env python

# Marvel comics API fun stuff
# Reference: http://www.virtuallyghetto.com/2014/02/having-some-fun-with-marvel-comics-api.html
# Not using any of the Vmware stuff from this, just the Get Character calls

import requests
import json
import time
import hashlib
import random
import argparse
import atexit
import sys


# Marvel API keys
marvel_public_key = ''
marvel_private_key = ''

def getMarvelCharacters(number_of_characters):
    timestamp = str(int(time.time()))
    # hash is required as part of request which is md5(timestamp + private + public key)
    hash_value = hashlib.md5(timestamp + marvel_private_key + marvel_public_key).hexdigest()

    characters = []
    for x in xrange(number_of_characters):
        #randomly select one of the 1402 Marvel character
        offset = random.randrange(1,1402)
        limit = '1'

        # GET /v1/public/characters
        url = 'http://gateway.marvel.com:80/v1/public/characters?limit=' + limit + '&offset=' + str(offset) + '&apikey=' + marvel_public_key + '&ts=' + timestamp + '&hash=' + hash_value
        headers = {'content-type':'application/json'}
        request = requests.get(url, headers=headers)
        data = json.loads(request.content)
        # retrieve character name & replace spaces with underscore so we don't have stupid spaces in our VM names
        character = data['data']['results'][0]['name'].strip().replace(' ','_')
        characters.append(character)
    return characters
