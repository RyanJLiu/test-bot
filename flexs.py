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


emergency={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "緊急呼叫",
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
        "text": "打119",
        "action": {
          "type": "uri",
          "label": "action",
          "uri": "tel://119"
        }
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "button",
        "text": "聯絡護理師"
      }
    ]
  },
  "styles": {
    "header": {
      "backgroundColor": "#FF0000"
    }
  }
}

schedule={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "行程",
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
          "label": "新增行程",
          "text": "新增行程"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "行程確認",
          "text": "行程確認"
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

scheduleset={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "新增行程",
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
          "label": "新增外出行程",
          "text": "新增外出行程"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "新增藥物提醒",
          "text": "新增藥物提醒"
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

schedulecheck={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "行程確認",
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
          "label": "確認外出行程",
          "text": "確認外出行程"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "確認藥物提醒",
          "text": "確認藥物提醒"
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
