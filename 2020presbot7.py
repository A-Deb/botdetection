import botometer
import json
import numpy as np
import pandas as pd
import time
import csv

users_df = pd.read_csv('users.csv',names=['UserID'])
accountid = users_df.UserID[600000:700000]


mashape_key = '6aa6cfce51mshc532d614b896bf0p13fa3ejsn5d2a842a85d4'

twitter_app_auth = {
    'consumer_key': 'XGl8nV4qT2e1X58J3H6kBajeS',
    'consumer_secret': 'YcxoUWt0ye9E6hpKNJ6qn3HLWYfNBUT1f9e6gyBVd719Ca2VJD',
    'access_token': '24392777-K6McP1kb7zOnel8Jd61QRurc0v7Oh7rFbfiq63OuK',
    'access_token_secret': 'eeQsdCrAB3u11pKCav7oe32GMEDyfMDxhf17w5sFuCkvx',
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

for screen_name, result in bom.check_accounts_in(accountid):

    if 'TweepError' in str(result):
        if result['error'] == 'TweepError: Not authorized.':
             with open('bot_fail7.txt','a') as f:
                  f.write(screen_name+' is a private account\n')

        elif 'Sorry, that page does not exist.' in result['error']:
             with open('bot_fail7.txt','a') as f:
                  f.write(screen_name+' is a suspended account\n')
    else:
         with open('bot_pass7.txt','a') as f:
              json.dump(result,f)
              f.write('\n')
