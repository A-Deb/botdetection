import botometer
import json
import numpy as np
import pandas as pd
import time
import csv

users_df = pd.read_csv('users.csv',names=['UserID'])
accountid = users_df.UserID[500000:600000]


mashape_key = '6aa6cfce51mshc532d614b896bf0p13fa3ejsn5d2a842a85d4'

twitter_app_auth = {
    'consumer_key': 'Ok8h1IXemPbnpsUoj0nukaNAF',
    'consumer_secret': 'oQcZNzBd5eKnjobSTUdHFwzgUcI3XoFTRSI8u9LvibjdGKEofu',
    'access_token': '984308525223432192-DtvgjOaD7rfdX6J1spjDKOGnY3fPi31',
    'access_token_secret': 'isYXAJtBLhHqywhMiN77zWwmatGRBCAXfyFw04zv9Fg1r',
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

for screen_name, result in bom.check_accounts_in(accountid):

    if 'TweepError' in str(result):
        if result['error'] == 'TweepError: Not authorized.':
             with open('bot_fail6.txt','a') as f:
                  f.write(screen_name+' is a private account\n')

        elif 'Sorry, that page does not exist.' in result['error']:
             with open('bot_fail6.txt','a') as f:
                  f.write(screen_name+' is a suspended account\n')
    else:
         with open('bot_pass4.txt','a') as f:
              json.dump(result,f)
              f.write('\n')
