import botometer
import json
import numpy as np
import pandas as pd
import time
import csv

users_df = pd.read_csv('users.csv',names=['UserID'])
accountid = users_df.UserID[1100000:1200000]


mashape_key = '6aa6cfce51mshc532d614b896bf0p13fa3ejsn5d2a842a85d4'

twitter_app_auth = {
    'consumer_key': 'WKv65XyQvDBPy4kbLA9rfN9bQ',
    'consumer_secret': 'Xb39g4pRXkikjwSi4VwjK7xr1FhNI4mQLEKsxGPgGOSQY1xaGW',
    'access_token': '1067627610136489985-C5GB8aLklJao4NQSKKNbjRXGs73rbM',
    'access_token_secret': 'prHKqX2eAiDnmO9IxDhWXh0lfZQR7K9wgyAiDAvadCTkO',
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

for screen_name, result in bom.check_accounts_in(accountid):

    if 'TweepError' in str(result):
        if result['error'] == 'TweepError: Not authorized.':
             with open('bot_fail12.txt','a') as f:
                  f.write(screen_name+' is a private account\n')

        elif 'Sorry, that page does not exist.' in result['error']:
             with open('bot_fail12.txt','a') as f:
                  f.write(screen_name+' is a suspended account\n')
    else:
         with open('bot_pass12.txt','a') as f:
              json.dump(result,f)
              f.write('\n')
