import urllib
import urllib.request  #用來建立請求
import requests
import json
from decimal import *

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
line_bot_api = LineBotApi('SfYJqq5ckA4xHKPEQBiuxpcJc0oYvR+ftPoxNPOxJQX68BvRLXnyjylgw+y+8NJH9E2ncJIR1gVcWJOY8PQ23cySa/xBEkqCDQPRwlrsFV67WloyByqaG4MkLmzPnnUKUv9198YtwXQroc0g0n0RdAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('54629cbee6579ede1c338ad616813c78')

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
    if "經緯度" in text:
        try:
            url = "https://io.adafruit.com/api/v2/allenleekawai/feeds/gps?x-aio-key=7f88a12eb90e4a1c9e062e83630292da"
            headers = {'User-Agent':
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
            req = urllib.request.Request(url, headers = headers)
            conn = urllib.request.urlopen(req)
            data = conn.read()
            docj = json.loads(data)
            doc = docj['last_value'].split(" ")
            reply_text = "現在時間：" + doc[2] + "\n\n經度：" + doc[7] + "\n緯度：" + doc[12]
            message = TextSendMessage(reply_text)
            line_bot_api.reply_message(event.reply_token, message)
        except:
            reply_text = "出錯了"
            message = TextSendMessage(reply_text)
            line_bot_api.reply_message(event.reply_token, message)
    elif "地圖資訊" in text:
        try:
            url = "https://io.adafruit.com/api/v2/allenleekawai/feeds/gps?x-aio-key=7f88a12eb90e4a1c9e062e83630292da"
            headers = {'User-Agent':
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
            req = urllib.request.Request(url, headers = headers)
            conn = urllib.request.urlopen(req)
            data = conn.read()
            docj = json.loads(data)
            doc = docj['last_value'].split(" ")
            lond = Decimal(doc[7]).quantize(Decimal('0.00000000000000'))
            latd = Decimal(doc[12]).quantize(Decimal('0.00000000000000'))
            lon = str(lond)
            lat = str(latd)
            location_message = LocationSendMessage(title='my location',address='Taiwan',latitude=lat,longitude=lon)
            line_bot_api.reply_message(event.reply_token, location_message)
        except:
            reply_text = "出錯了"
            message = TextSendMessage(reply_text)
            line_bot_api.reply_message(event.reply_token, message)
    elif "我愛鯊魚" in text:
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
