#!/usr/bin/env python

import requests,json,sys,os

ACCESS_TOKEN=os.environ["ACCESS_TOKEN"]
REATING=chr(int(float(os.environ["value"]))+64)
send_by="Himanshu"
sub= "bug report"
msg= "Current Quality Status is " + REATING + ", https://sonarcloud.io/dashboard?id=HimanshuKapoor328_bc-25&branch=master" 

urldest= 'https://cliq.zoho.com/api/v2/channelsbyname/sonartest/message'

headers = {
        "Content-type": "application/json",
        "Authorization": "Zoho-oauthtoken " + (ACCESS_TOKEN)
        }

content = {
                "text": (msg),
                "broadcast" :"true",
                "bot": {
                        "name": (send_by)
                        },
                "card": {
                        "title": (sub),
                        "theme": "modern-inline"
                        }
                }


post = requests.post(url=urldest, data=json.dumps(content), headers=headers)
