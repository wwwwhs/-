import json
import requests


# r1 = requests.get(
#     'https://oapi.dingtalk.com/robot/send?access_token=c3ed947c0a441e0a4d3a7269f78d3b266ae61a1e5bb2a4ea9c9030bf00e6f284')
# print(r1)


class DingRobot:
    _ding = 'https://oapi.dingtalk.com/robot/send?access_token=' \
            'c3ed947c0a441e0a4d3a7269f78d3b266ae61a1e5bb2a4ea9c9030bf00e6f284'
    _headers = {"Content-type": "application/json;charset=utf-8"}
    _key = "哈撒给"

    def __int__(self):
        pass

    def send(self, data):
        requests.post(url=self._ding, headers=self._headers, data=json.dumps(data))

    def send_text(self):
        content = {
            "msgtype": "text",
            "text": {
                "content": self._key + "老八蜜汁小汉堡"
            },
            "at": {
                "atMobiles": [],
                "atUserIds": [],
                "isAtAll": False
            }
        }
        return self.send(content)

    def send_link(self):
        links = {
            "msgtype": "link",
            "link": {
                "text": self._key,
                "title": "迪迦",
                "picUrl": "",
                "messageUrl": "https://baike.baidu.com/item/%E8%BF%AA%E8%BF%A6%C2%B7%E5%A5%A5%E7%89%B9%E6%9B%BC/13236751?fromtitle=%E8%BF%AA%E8%BF%A6&fromid=1690290&fr=aladdin"
            }
        }
        return self.send(links)

    def send_markdown(self):
        markdowns = {
            "msgtype": "markdown",
            "markdown": {
                "title": self._key,
                "text": "  杭州天气  \n > 9度，西北风1级，空气良89，相对温度73%\n > ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n > ###### 10点20分发布 [天气](https://www.dingtalk.com) \n"
            },
            "at": {
                "atMobiles": [],
                "atUserIds": [],
                "isAtAll": False
            }
        }
        return self.send(markdowns)


if __name__ == '__main__':
    ding = DingRobot()
    ding.send_text()
    ding.send_link()
    ding.send_markdown()

