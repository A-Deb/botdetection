import botometer
import json
import numpy as np
import pandas as pd
import time
import csv

users_df = pd.read_csv('users.csv',names=['UserID'])
accountid = users_df.UserID[400000:500000]


mashape_key = '6aa6cfce51mshc532d614b896bf0p13fa3ejsn5d2a842a85d4'

twitter_app_auth = {
    'consumer_key': 'bNTAQHB0Lsm16ZIBZM3tXzyFF',
    'consumer_secret': 'iTP3ADkwvzuXZoYnof4Dmt1r4t7j2tLXXjC6lGxD7OA9vZCYrZ',
    'access_token': '1150558994294902784-pxlxGBW1sSTXF1pbqbR4QVZwOmOrAN',
    'access_token_secret': 'UXgPRL5A8Bg78ifKBe9RPLhD2UOEcgmQDbVkBalsxLJ1o',
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

for screen_name, result in bom.check_accounts_in(accountid):

    if 'TweepError' in str(result):
        if result['error'] == 'TweepError: Not authorized.':
             with open('bot_fail5.txt','a') as f:
                  f.write(screen_name+' is a private account\n')

        elif 'Sorry, that page does not exist.' in result['error']:
             with open('bot_fail5.txt','a') as f:
                  f.write(screen_name+' is a suspended account\n')
    else:
         with open('bot_pass5.txt','a') as f:
              json.dump(result,f)
              f.write('\n')
