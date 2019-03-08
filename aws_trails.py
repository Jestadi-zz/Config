#!/usr/bin/python3

import boto3
#from datetime import datetime, timezone
from datetime import *

client = boto3.client('iam')
response = client.list_users()
user_responses = response['Users']

today = datetime.now(timezone.utc)

#print("today is: ", today)
#print(user_responses)

for user_response in user_responses:
  create_duration = today - user_response['CreateDate']
  duration_days = create_duration.days
  print("duration days: ", duration_days)
  if duration_days >= 30 :
    print("old user: ", user_response['UserName'])

# () --- method/fn call
# ('str') --- string/character array
# [] --- array/list 
