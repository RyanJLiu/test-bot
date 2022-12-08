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
          "text": "設定作息時間",
          "label": "設定作息時間"
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

helper={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "help",
        "size": "md",
        "weight": "bold"
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
          "label": "設定",
          "text": "設定"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "行程",
          "text": "行程"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "關於我",
          "text": "關於我"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "緊急呼叫",
          "text": "緊急呼叫"
        }
      }
    ]
  },
  "styles": {
    "header": {
      "backgroundColor": "#00B800"
    }
  }
}
