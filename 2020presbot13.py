import botometer
import json
import numpy as np
import pandas as pd
import time
import csv

users_df = pd.read_csv('users.csv',names=['UserID'])
accountid = users_df.UserID[1200000:1300000]


mashape_key = '6aa6cfce51mshc532d614b896bf0p13fa3ejsn5d2a842a85d4'

twitter_app_auth = {
    'consumer_key': 'VPJQZ2hLMfuXtZ96TuIbNYFR1',
    'consumer_secret': 'DLJgvucVg8EbOuMLvFMGjkBqRblyPnKenEToAkK0mrq7J9rv08',
    'access_token': '1067627610136489985-SBIDZ3idkSC29S62Zbakyqk2ajQkvA',
    'access_token_secret': 'x1Mmw0nlM2f1wDXdmMBY3u14d7S8yLfHoMWyJ4nGMUWbF',
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

for screen_name, result in bom.check_accounts_in(accountid):

    if 'TweepError' in str(result):
        if result['error'] == 'TweepError: Not authorized.':
             with open('bot_fail13.txt','a') as f:
                  f.write(screen_name+' is a private account\n')

        elif 'Sorry, that page does not exist.' in result['error']:
             with open('bot_fail13.txt','a') as f:
                  f.write(screen_name+' is a suspended account\n')
    else:
         with open('bot_pass13.txt','a') as f:
              json.dump(result,f)
              f.write('\n')
