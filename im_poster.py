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
def create_index(title, id):
  title=str(title)

  message_link= f'https://t.me/resource_log/{id}'

  url_index= f'https://api.telegram.org/bot{bot_auth_key}/getChat?chat_id=@{chat_id}'

  try:
    index_data = requests.get(url_index).json()['result']['pinned_message']['text']
    index_message_id = requests.get(url_index).json()['result']['pinned_message']['message_id']
    
    print("Index Found...")
    print(index_data)
    index=0
    for i in index_data:
      if i == '\n':
        index+=1
    print(index)
    index_final_data = "{}\n{}. {}>{}".format(index_data, index, title, message_link)
    index_final_data=index_final_data.replace('\n', '%0A')

    url_editmessage = f'https://api.telegram.org/bot{bot_auth_key}/editMessageText?chat_id=@{chat_id}&message_id={index_message_id}&text={index_final_data}&disable_web_page_preview=True'
    send_request = requests.get(url_editmessage)

    if send_request.status_code == 200:
      print("Message Sent")
  except KeyError:
    print('There is no index\nCreating index now... ')
    index_final_data=f"INDEX%0A1. {title}>{message_link}"
    url_sendmessage = f'https://api.telegram.org/bot{bot_auth_key}/sendMessage?chat_id=@{chat_id}&text={index_final_data}&disable_web_page_preview=True'
    send_request = requests.get(url_sendmessage)
    pin_message_id = send_request.json()['result']['message_id']
    url_pinmessage=f'https://api.telegram.org/bot{bot_auth_key}/pinChatMessage?chat_id=@{chat_id}&message_id={pin_message_id}&disable_notification=True'
    pin_request = requests.get(url_pinmessage)
    if send_request.status_code == 200:
      print("Message Sent")


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
  else:
    print('MESSAGE: HIJACKED!!!!')
  

entry()
# create_index()

#https://api.telegram.org/bot5133615692:AAGF7sKZU9edhtYqSPYPG9LlSNujGpJCDvM/getMe
#https://api.telegram.org/bot5133615692:AAGF7sKZU9edhtYqSPYPG9LlSNujGpJCDvM/sendMessage?chat_id=@resource_log&text=[title](https://t.me/resource_log/26)&parse_mode=Markdown&disable_web_page_preview=True
#https://api.telegram.org/bot5133615692:AAGF7sKZU9edhtYqSPYPG9LlSNujGpJCDvM/editMessageText?chat_id=@resource_log&message_id=10&text=hey
#https://api.telegram.org/bot5133615692:AAGF7sKZU9edhtYqSPYPG9LlSNujGpJCDvM/pinChatMessage?chat_id=@resource_log&message_id=3&disable_notification=True
#https://api.telegram.org/bot5133615692:AAGF7sKZU9edhtYqSPYPG9LlSNujGpJCDvM/getChat?chat_id=@resource_log