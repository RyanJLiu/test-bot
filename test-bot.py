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
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text="nothing", contents=flexs.setting))
    elif("設定作息時間" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請前往此網站以修改設定\nhttps://liff.line.me/1657681037-8xpGL6E9"))
    elif("設定個人資料" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請前往此網站以修改設定\nhttps://liff.line.me/1657681037-LvkoejpY"))
    elif ("HELP" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text="nothing", contents=flexs.helper))
    elif ("USER MANUAL" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text="nothing", contents=flexs.helper))
    elif ("設定" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="點選選單左上角按鈕，可設定個人資料或作息時間"))
    elif ("行程" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="點選選單右上角按鈕，可查詢行程"))
    elif ("關於我" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="This is a bot developed for patients to solving problems recovering at home."))
    elif ("緊急呼叫" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="點選選單右下角按鈕，可連絡護理師或撥打緊急電話"))
    elif ("SCHEDULE CHECK" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Checking..."))
    elif ("EMERGENCY CALL" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text="nothing", contents=flexs.emergency))
    elif ("測試" == str(event.message.text).upper().strip()):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="測試成功"))
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
