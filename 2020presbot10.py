import botometer
import json
import numpy as np
import pandas as pd
import time
import csv

users_df = pd.read_csv('users.csv',names=['UserID'])
accountid = users_df.UserID[900000:1000000]


mashape_key = '6aa6cfce51mshc532d614b896bf0p13fa3ejsn5d2a842a85d4'

twitter_app_auth = {
    'consumer_key': '3RNe2tkVtBhP3l77PSEzuaJ4j',
    'consumer_secret': 'S7bKaeiPIwifrKLkz8X93yAvtmDp5P2YVjST9jZluiaM3lHMmx',
    'access_token': '24392777-FUblnicXsCELwqdlu3x65GQ6KqcYUgqbnyFJrg0rL',
    'access_token_secret': 'smfpEPYCP5rifdCmvPpBKqEJ7qrKmWhkitmQdR7JXo5Cj',
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

for screen_name, result in bom.check_accounts_in(accountid):

    if 'TweepError' in str(result):
        if result['error'] == 'TweepError: Not authorized.':
             with open('bot_fail10.txt','a') as f:
                  f.write(screen_name+' is a private account\n')

        elif 'Sorry, that page does not exist.' in result['error']:
             with open('bot_fail10.txt','a') as f:
                  f.write(screen_name+' is a suspended account\n')
    else:
         with open('bot_pass10.txt','a') as f:
              json.dump(result,f)
              f.write('\n')
