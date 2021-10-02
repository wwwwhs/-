import json

import requests


# todo:第一层：分析接口测试剥离重复的动作-封装到BaseApi中(比如gettoken,send)
# todo:第二层：将接口封装成一个个独立的方法,进行参数化处理,方便后期测试进行调用
# todo:第三层：创建api对应的测试文件,设计我们的测试用例
# todo:第四层：执行测试用例(数据驱动&关键字驱动)使用pytest框架中的功能进行数据驱动
'''
第二层技术点 参数化设计(参数非常多40+)
第三层技术点 用例设计，用例流程设计，jsonpath，断言设计
第四层技术点 执行方式，数据的来源，数据的保存，数据的重复使用
'''


class BaseApi:
    def __init__(self):
        pass
        self.wework = self.gettoken()

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=3, ensure_ascii=False))
        return r

    def gettoken(self):
        # todo:获取 access_token
        corpid = "wwd72b10b8b35b649a"
        corpsecret = "fKbsBFrahcfJ9I5mRWKjY4wsQUDOs3WcB7oR1oaLS8o"
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        token = self.send(data).json()['access_token']
        return token