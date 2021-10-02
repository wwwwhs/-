"""
接口文档：https://developers.dingtalk.com/document/robots/custom-robot-access
"""

# todo:发送请求到钉钉
import json

import requests


class DingRobot:
    _ding = "https://oapi.dingtalk.com/robot/send?access_token=" \
            "e6cdea9512c176d08eba5b12d00a2f60a577d0a861c35e766af36b3511ee55c0"
    _headers = {"Content-Type": "application/json;charset=utf-8"}
    _key = "大宝贝"

    def __init__(self):
        pass

    def send(self, data):
        requests.post(url=self._ding, headers=self._headers, data=json.dumps(data))

    def send_text(self):
        content = {
            "msgtype": "text",
            "text": {
                "content": self._key + "我就是我,@郑佳怡 是不一样的烟火",
            },
            "at": {
                "atMobiles": [],
                "atUserIds": [],
                "isAtAll": False
            }
        }
        return self.send(content)

    def send_link(self):
        content = {
            "msgtype": "link",
            "link": {
                "text": "王振阳大宝贝",
                "title": self._key,
                "picUrl": "",
                "messageUrl": "https://www.bilibili.com/"
            }
        }
        return self.send(content)

    def send_card(self):
        content = {
            "msgtype": "feedCard",
            "feedCard": {
                "links": [
                    {
                        "title": self._key + "卡卡卡卡卡卡卡",
                        "messageURL": "https://www.dingtalk.com/",
                        "picURL": "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png"
                    }
                ]
            }
        }
        self.send(content)


if __name__ == '__main__':
    ding = DingRobot()
    ding.send_text()
    ding.send_link()
    ding.send_card()
    ding.send_markdown()