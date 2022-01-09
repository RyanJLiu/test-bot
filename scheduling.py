from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError

CHANNEL_ACCESS_TOKEN = "UYBnsEo8qLdA4aQAdbX/NUxy9L86NT5epTsoy8d3h2xRItfJyecH49jRkUP26eHbHqN6FCUyboStjuk7TMg/a1u+c+z9mS/CvKJ2/g3my9olG4CQy2yLfHO3ceORUy5CxufKXbUl1xyG7nGHSsM7IwdB04t89/1O/w1cDnyilFU="
to = "Ud0b3296f8e4a70520b4ed2f2d1b3bdd8"

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

try:
    line_bot_api.push_message(to, TextSendMessage(text='Time for lunch.'))
except LineBotApiError as e:
    raise e
