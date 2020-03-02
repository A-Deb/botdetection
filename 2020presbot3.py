import botometer
import json
import numpy as np
import pandas as pd
import time
import csv


users_df = pd.read_csv('users.csv',names=['UserID'])
accountid = users_df.UserID[200000:300000]
mashape_key = '6aa6cfce51mshc532d614b896bf0p13fa3ejsn5d2a842a85d4'

twitter_app_auth = {
'consumer_key': 'i9IO9aA2CRB0b2Dd7IhcKqROH',
'consumer_secret': 'Jh2gy2jFQoXaYhClqrYeFCVozJFGiD7e6JMISt7Rji8aqt6iME',
'access_token': '971146145144582144-qFEdwvzjwP1I3AhID2wH6cW5aiwaLIo',
'access_token_secret': 'zGQpYhDRRdYbfoKEvvYhDBlsJAinFUBDNOq8jOc8KbL92'
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)


for screen_name, result in bom.check_accounts_in(accountid):

    if 'TweepError' in str(result):
        if result['error'] == 'TweepError: Not authorized.':
             with open('bot_fail3.txt','a') as f:
                  f.write(screen_name+' is a private account\n')

        elif 'Sorry, that page does not exist.' in result['error']:
             with open('bot_fail3.txt','a') as f:
                  f.write(screen_name+' is a suspended account\n')
    else:
         with open('bot_pass3.txt','a') as f:
              json.dump(result,f)
              f.write('\n')
