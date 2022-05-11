__author__ = "Adiziel"
__email__ = "aditya.pathak.plus@gmail.com"
__status__ = "Started"


import requests
import json

from dotenv import dotenv_values

config = dotenv_values(".env")

bot_auth_key=config['AUTH_KEY']
chat_id="resource_log"

#create index
def create_index(id):
  message_link= f'https://t.me/resource_log/{id}'
  url_index=

#create a resource, title and entry in index
def entry():
  title = input('Enter Title: ')
  message=input('Enter message: ')

  for msg in title, message:
    # print(msg)
    url_send_message=f'https://api.telegram.org/bot{bot_auth_key}/sendMessage?chat_id=@{chat_id}&text={msg}'
    send_req = requests.get(url_send_message)

  if send_req.status_code == 200:
    id =send_req.json()['result']['message_id']
    create_index(title, id)
    print("Message Sent")
  else:
    print('MESSAGE: HIJACKED!!!!')

  

entry()

#https://api.telegram.org/bot5133615692:AAGF7sKZU9edhtYqSPYPG9LlSNujGpJCDvM/getMe
#https://api.telegram.org/bot5133615692:AAGF7sKZU9edhtYqSPYPG9LlSNujGpJCDvM/sendMessage?chat_id=@resource_log&text=[title](https://t.me/resource_log/26)&parse_mode=Markdown&disable_web_page_preview=True
#https://api.telegram.org/bot5133615692:AAGF7sKZU9edhtYqSPYPG9LlSNujGpJCDvM/editMessageText?chat_id=@resource_log&message_id=10&text=hey
#https://api.telegram.org/bot5133615692:AAGF7sKZU9edhtYqSPYPG9LlSNujGpJCDvM/pinChatMessage?chat_id=@resource_log&message_id=3&disable_notification=True
