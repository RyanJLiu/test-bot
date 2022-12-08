import json

setting={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "setting",
        "weight": "bold",
        "size": "md"
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "設定個人資料",
          "text": "設定個人資料"
        }
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "text": "設定時間",
          "label": "設定時間"
        }
      }
    ]
  },
  "styles": {
    "header": {
      "backgroundColor": "#00b800"
    }
  }
}
