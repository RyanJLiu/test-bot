from flask import Flask, request, abort

import re

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot.models import *

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
    msg = TextSendMessage(text=event.massage.text) # 使用者輸入的內容
    #profile = line_bot_api.get_profile(event.source.user_id)
    #user_name = profile.display_name #使用者名稱
    #uid = profile.user_id # 發訊者ID
    #if re.match("test", msg):
    #    line_bot_api.push_message(uid, TextSendMessage("test success"))
    #elif re.match("測試", msg):
    #    line_bot_api.push_message(uid, TextSendMessage("測試成功"))
    #else:
    line_bot_api.reply_message(event.reply_token, msg)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
