> # Imposter bot 

### Imposter is a telegram bot which creates a post with title and message with and index to track that post, in telegram channel or group in which this bot has been added. 
<br>

> List of Keys and Ids which is needed to work with this bot are:

1. A group or a channel\
You all know how to create a group or a channel, we would need **channel id or group id**.

2. A telegram bot\
To create a telegram bot you need botfather, after creation of Bot there would be an **auth key for bot** we would be needing that.

<br>

> ### How it works? 
\
Imposter is bascially a kind of interface given to some of the endpoints of **Telegram Bot Api**, it takes data from users and put it in perticular format in telegram Channels or groups.

> Step 1: Print title and message in telegram channel (Done)


To do this **sendMessage** method is getting used, interface takes **bot auth key**, **channel id**, **a title** and **message** from user.
<br><br>

> Step 2: Create or Append Index

There is a bit of processing in this situation, **it has been assumed that there are no index created by any user and only that index has been pinned to that channel**.

*if there is no pinned message it will create a new index*

Now it takes the **title** and **link of the sent message** and add title as hyperlink, linked to the message.


To get the pinned message **getChat** method is being used. \

If there is no pin, to create index **sendMessage** and to pin that index **pinChatMessage** are being used.\

if there is a pinned message, then it checks if it is index or not it it's not an index message then **editMessage**.


