from flask import Flask, request, abort, render_template
import flexs
import json
import re

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('UYBnsEo8qLdA4aQAdbX/NUxy9L86NT5epTsoy8d3h2xRItfJyecH49jRkUP26eHbHqN6FCUyboStjuk7TMg/a1u+c+z9mS/CvKJ2/g3my9olG4CQy2yLfHO3ceORUy5CxufKXbUl1xyG7nGHSsM7IwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0a0caaf1002fb8f6c80362f8f88cc716')

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if ("USER SET" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text="", contents=flexs.setting))
    elif("設定時間" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請前往此網站以修改設定\nhttps://liff.line.me/1657681037-8xpGL6E9"))
    elif("設定個人資料" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請前往此網站以修改設定\nhttps://liff.line.me/1657681037-jQkN7qOw"))
    elif ("USER MANUAL" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="This is a bot developed for patients to solving problems recovering at home."))
    elif ("Schedule Check" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Checking..."))
    elif ("Emergency Call" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="119"))
    elif ("測試" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="測試成功"))
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
