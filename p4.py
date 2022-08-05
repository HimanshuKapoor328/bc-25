#!/usr/bin/env python

import requests,json,sys

token="1000.59b28244231baa9a8946a8ce97e24615.7fb6ad782be7c8d9d4620000d048c52e"
sentby="Himanshu"
subject= "bug report"
message= 'Current Quality Status is D , "https://sonarcloud.io/dashboard?id=HimanshuKapoor328_bc-25&branch=master" '

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