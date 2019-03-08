#!/usr/bin/python3

import boto3
from datetime import *

client = boto3.client('iam')
#response = client.get_group(   GroupName='admin-group')

#for passwd in response['Users']:
#   print(passwd['UserName'])
#   user = client.get_user(UserName=passwd['UserName'])['User']
#   print("user keys:", user.keys())
#   print("user: ", user)
#   last_used = user['PasswordLastUsed']
#   create_date = user['CreateDate']
#   print("create date: ", create_date)
#   print("password last used date: ", last_used)
#   print(passwd.keys())

users = client.list_users()['Users']
python3
for user in users:
#  print("user keys ", user.keys())
#  print("username: ", user['UserName'])
  try:
    print(user['UserName'], ":", user['PasswordLastUsed'])
 #   print("last used: ", user['PasswordLastUsed'])
  except KeyError as e:
    print("Key not found for user:", user['UserName'])

#print(response)


