from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('f+GWRpzMzeR+yG+A0I5SNc78aCy1WqglZz+4ctEhltFmwtkeC8m3IeHC5CzgIym2rlhkFOB7evoQlc153nu41uOZW3IpjLm3mX5VjSshSeLDnPY7Z7B8Y2dE6PBFwSlgLVNxLxqRCjSUImmvaSzNqgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('c172b5dcee5285bbdc77f025bda38932')

line_bot_api.push_message('U652bbe8cebc4e01249e2b57703bb713c', TextSendMessage(text='我更新了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if "我愛鯊魚" in text:
        reply_text = "鯊魚愛我"
        message = TextSendMessage(reply_text)
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
