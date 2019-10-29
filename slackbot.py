from slackclient import SlackClient
import json
import time

# the bot currently replies only to `BOT TEST`. this is a test feature to
# ensure that the bot is working
# features will be appended to this code base

# configuration happens here :)
# var:
# 	slack_bot_token: contains user bot tokens
tokens = {}
with open('configs.json') as json_data:
	tokens = json.load(json_data)

# declare client instance
slack_client = SlackClient(tokens.get('slack_bot_token'))

# connect to client api
if slack_client.rtm_connect():

	#inifinite loop that continously checks for events
	while slack_client.server.connected is True:
		messages = slack_client.rtm_read()
		print(messages)
		print('--' * 50)

		if messages:
			for message in messages:
				if message.get("subtype") is None and message.get('user') is not None and message.get('text') is not None and  "BOT TEST" in message.get('text'):
					channel = message['channel']
					send_message = 'Responding to `BOT TEST` message sent by user <@%s>' % message['user']
					slack_client.api_call('chat.postMessage', channel=channel, text=send_message)
		
		# ensures api makes a call per second
		time.sleep(1)

else:
	print('Connection failed')
