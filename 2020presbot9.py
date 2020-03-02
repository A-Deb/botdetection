import botometer
import json
import numpy as np
import pandas as pd
import time
import csv

users_df = pd.read_csv('users.csv',names=['UserID'])
accountid = users_df.UserID[800000:900000]


mashape_key = '6aa6cfce51mshc532d614b896bf0p13fa3ejsn5d2a842a85d4'

twitter_app_auth = {
    'consumer_key': 'Msh7SwQkk1MeQ6W3SQaohd4xF',
    'consumer_secret': 'TL5ohNwqts2Mnsyd52oRWFws5xXeVmlxukYEOO3T0v2SBlYwKp',
    'access_token': '24392777-cU62O31OlInDCOW7umFYRprrlRmn6s5XMnsqBaMU2',
    'access_token_secret': 'sOG8K1VOZhayuYwFIWtZyvYFLxXQjPiM5VxT6AhOJoORZ',
}

bom = botometer.Botometer(wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

for screen_name, result in bom.check_accounts_in(accountid):

    if 'TweepError' in str(result):
        if result['error'] == 'TweepError: Not authorized.':
             with open('bot_fail8.txt','a') as f:
                  f.write(screen_name+' is a private account\n')

        elif 'Sorry, that page does not exist.' in result['error']:
             with open('bot_fail8.txt','a') as f:
                  f.write(screen_name+' is a suspended account\n')
    else:
         with open('bot_pass8.txt','a') as f:
              json.dump(result,f)
              f.write('\n')
