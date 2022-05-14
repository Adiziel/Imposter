__author__ = "Adiziel"
__email__ = "aditya.pathak.plus@gmail.com"
__status__ = "Started"


import requests
import json

# create and manage index
def create_index(bot_auth_key, chat_id, title, id):
  # title and message link
  title=str(title)
  message_link= f'https://t.me/resource_log/{id}'

  # using 'getChat' method to get info regarding chat
  url_index= f'https://api.telegram.org/bot{bot_auth_key}/getChat?chat_id=@{chat_id}'

  try:
    """If INDEX is in Channel and Pinned"""
    # pinned message(index) data and id
    index_data = requests.get(url_index).json()['result']['pinned_message']['text']
    index_message_id = requests.get(url_index).json()['result']['pinned_message']['message_id']
    
    print("Index Found...")
    print(index_data)
    index=0
    for i in index_data:
      if i == '\n':
        index+=1
    print(index)
    index+=1
    index_final_data = "{}\n{}. {}>{}".format(index_data, index, title, message_link)
    # creating final string to pass as an argument in editMessage Url
    index_final_data=index_final_data.replace('\n', '%0A')

    # Using 'editMessageText' method to edit the INDEX message
    url_editmessage = f'https://api.telegram.org/bot{bot_auth_key}/editMessageText?chat_id=@{chat_id}&message_id={index_message_id}&text={index_final_data}&disable_web_page_preview=True'
    send_request = requests.get(url_editmessage)

    if send_request.status_code == 200:
      print("Message Sent")

  except KeyError:
    print('There is no index\nCreating index now... ')
    # creating new INDEX message
    index_final_data=f"INDEX%0A1. {title}>{message_link}"

    # Using 'sendMessage' method to create INDEX
    url_sendmessage = f'https://api.telegram.org/bot{bot_auth_key}/sendMessage?chat_id=@{chat_id}&text={index_final_data}&disable_web_page_preview=True'
    send_request = requests.get(url_sendmessage)

    # fetching message_id of INDEX message to pin it
    pin_message_id = send_request.json()['result']['message_id']

    # Using 'pinChatMessage' to pin INDEX message
    url_pinmessage=f'https://api.telegram.org/bot{bot_auth_key}/pinChatMessage?chat_id=@{chat_id}&message_id={pin_message_id}&disable_notification=True'
    pin_request = requests.get(url_pinmessage)
    if send_request.status_code == 200:
      print("Message Sent")


#create a resource, title and entry in index
def create_post():
  #user Inputs
  print('Input Credentials....')
  bot_auth_key= input('Telegram Bot Auth Key: ')
  chat_id= input('Channel/Group id: ')
  print("Post....")
  title = input('Enter Title: ')
  message=input('Enter message: ')

  #post creation
  msg = f'{title}%0A{message}'
  #url for 'sendMessage' method
  url_send_message=f'https://api.telegram.org/bot{bot_auth_key}/sendMessage?chat_id=@{chat_id}&text={msg}'
  send_req = requests.get(url_send_message)

  if send_req.status_code == 200:
    id =send_req.json()['result']['message_id']
    #calling 'create_index' to manage index
    create_index(bot_auth_key, chat_id, title, id)
  else:
    print('MESSAGE: HIJACKED!!!!')
  

if __name__ == '__main__':
  create_post()
