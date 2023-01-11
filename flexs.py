import json

question={
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "疑難雜症",
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
          "label": "輕微頭痛",
          "text": "輕微頭痛"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "胸悶",
          "text": "胸悶"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "喉嚨痛",
          "text": "喉嚨痛"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "肚子痛",
          "text": "肚子痛"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "心情不好",
          "text": "心情不好"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "身體嚴重不適",
          "text": "身體嚴重不適"
        },
        "color": "#FF0000"
      }
    ]
  },
  "styles": {
    "header": {
      "backgroundColor": "#00B800"
    }
  }
}

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
      },
      {
        "type": "separator",
        "margin": "md"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "text": "更改護理師",
          "label": "更改護理師"
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
          "text": "查詢個人設定",
          "label": "查詢個人設定"
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
          "label": "打119",
          "uri": "tel://119"
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
          "label": "聯絡護理師",
          "text": "聯絡護理師"
          }
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
          "label": "疑難雜症",
          "text": "疑難雜症"
        }
      },
      {
        "type": "separator"
      },
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
        },
        "color": "#FF0000"
      }
    ]
  },
  "styles": {
    "header": {
      "backgroundColor": "#00B800"
    }
  }
}
