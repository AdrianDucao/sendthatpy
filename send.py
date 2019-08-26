#!/bin/python3.7

import requests

url = "https://nexmo-nexmo-messaging-v1.p.rapidapi.com/send-sms"

to = input("To: ")
message = input("Messsage: ")

querystring = {"text": message,"title":"nsa","from":"your mama","to": to}

payload = ""
headers = {
    'x-rapidapi-host': "nexmo-nexmo-messaging-v1.p.rapidapi.com",
    'x-rapidapi-key': "your own authentication key",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)