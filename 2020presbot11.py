import botometer
import json
import numpy as np
import pandas as pd
import time
import csv

users_df = pd.read_csv('users.csv',names=['UserID'])
accountid = users_df.UserID[1000000:1100000]


mashape_key = '6aa6cfce51mshc532d614b896bf0p13fa3ejsn5d2a842a85d4'

twitter_app_auth = {
    'consumer_key': 'OdIkhW2E1HG6Giwkt0kXHsDzb',
    'consumer_secret': 'fzk906yJeZSois9zjS0TKXI6b9MPbKhWzrcAHPlKiHYDB8uPYs',
    'access_token': '1067627610136489985-bqvH5KONbjBUZ54xJgWxxGcm6r1jIT',
    'access_token_secret': 'yrIA9WLqpWwoBNe0yF1L08gPcpcKd8V9DUKFA5QPS6QBT',
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

for screen_name, result in bom.check_accounts_in(accountid):

    if 'TweepError' in str(result):
        if result['error'] == 'TweepError: Not authorized.':
             with open('bot_fail11.txt','a') as f:
                  f.write(screen_name+' is a private account\n')

        elif 'Sorry, that page does not exist.' in result['error']:
             with open('bot_fail11.txt','a') as f:
                  f.write(screen_name+' is a suspended account\n')
    else:
         with open('bot_pass11.txt','a') as f:
              json.dump(result,f)
              f.write('\n')
