import os,sys
from flask import Flask,request
from pprint import pprint
from pymessenger import Bot

bot=Bot(" fb page token")

app=Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    #print(request.data)
    data = request.get_json()

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                # IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                print("sender id", sender_id)

                print("recipient id", recipient_id)

                if messaging_event.get('message'):
                    # Extracting text message
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'

                    # Echo
                    response = messaging_text
                    bot.send_text_message(sender_id, response)



    #pprint(data['entry'][0]['messaging'][0]['message']['text'])
    return "ok", 200


if __name__ == "__main__":
    app.run(debug=True,port=5000)