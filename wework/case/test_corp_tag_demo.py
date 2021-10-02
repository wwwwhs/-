import requests
from jsonpath import jsonpath
from wework.api.base_api import BaseApi


class TestCorpTag():
    def test_get_corp_tag_list(self):
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            "params": {"access_token": BaseApi().gettoken()},
            "json": {"group_id": ["ett_ZrEAAAtvx0Xibb3lSu4_IDG3OHTg"]}
        }
        r = requests.request(**data)
        print(jsonpath(r.json(), "$..[?(@.name=='小王')]")[0]['id'])
        iD = jsonpath(r.json(), "$..[?(@.name=='小王')]")[0]['id']
        print(iD)
