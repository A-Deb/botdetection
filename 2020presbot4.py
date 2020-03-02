import botometer
import json
import numpy as np
import pandas as pd
import time
import csv

users_df = pd.read_csv('users.csv',names=['UserID'])
accountid = users_df.UserID[300000:400000]


mashape_key = '6aa6cfce51mshc532d614b896bf0p13fa3ejsn5d2a842a85d4'

twitter_app_auth = {
    'consumer_key': '0P6rYEgLZIczzaUl0YL8x9dQu',
    'consumer_secret': 'eGN6iVhW9CMojYoZN7ZIrPKSB8EBvDpOyUlMQH62qBMmR1Q7Ab',
    'access_token': '1150558994294902784-N8ostEMAjVowofnSxDwSNtxQq4s7uu',
    'access_token_secret': '4Q7NjbSc6PxSCoSMPhY27dxxiWB3Mcp377TAEcITWLr4n',
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

for screen_name, result in bom.check_accounts_in(accountid):

    if 'TweepError' in str(result):
        if result['error'] == 'TweepError: Not authorized.':
             with open('bot_fail4.txt','a') as f:
                  f.write(screen_name+' is a private account\n')

        elif 'Sorry, that page does not exist.' in result['error']:
             with open('bot_fail4.txt','a') as f:
                  f.write(screen_name+' is a suspended account\n')
    else:
         with open('bot_pass4.txt','a') as f:
              json.dump(result,f)
              f.write('\n')
