#!/usr/bin/env python

import requests,json,sys

token="1000.bc17bd15b79c96341f94c350d476373a.f66ee711e088c00aae37c7dd88ff264d"
sentby="Himanshu"
subject= "bug report"
message= 'Current Quality Status is E , "https://sonarcloud.io/dashboard?id=HimanshuKapoor328_bc-25&branch=master" '

urldest= 'https://cliq.zoho.com/api/v2/channelsbyname/sonartest/message'

headers = {
        "Content-type": "application/json",
        "Authorization": "Zoho-oauthtoken " + (token)
        }

content = {
                "text": (message),
                "broadcast" :"true",
                "bot": {
                        "name": (sentby)
                        },
                "card": {
                        "title": (subject),
                        "theme": "modern-inline"
                        }
                }


post = requests.post(url=urldest, data=json.dumps(content), headers=headers)