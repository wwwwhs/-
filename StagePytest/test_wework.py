import requests
import json

# 添加
add = {
    "group_id": "ett_ZrEAAAtvx0Xibb3lSu4_IDG3OHTg",
    "group_name": "老王头tou",
    "tag": [{
        "name": "小小xiaooo王"
    }
    ]
}

# 更改
edit = {
    "id": "ett_ZrEAAAtvx0Xibb3lSu4_IDG3OHTg",
    "name": "老王头",
}

# 删除
drop = {
    "tag_id": [
        "ett_ZrEAAAoD2qbkHOCQLqgGQ36WQpOg"
    ]
}


def test_gettoken():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwd72b10b8b35b649a&corpsecret=fKbsBFrahcfJ9I5mRWKjY4wsQUDOs3WcB7oR1oaLS8o'
    r = requests.request('get', url=url)
    print(r.json())
    assert r.json()['errcode'] == 0
    token = r.json()['access_token']
    return token


a = test_gettoken()
b = {'access_token': a}


def test_search_001():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
    r = requests.request('post', url=url, params=b)
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.json()['errcode'] == 0
    assert r.json()['errmsg'] == "ok"


def test_add_001():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag'
    r = requests.request('post', url=url, params=b, json=add)
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.json()['errcode'] == 0
    assert r.json()['errmsg'] == "ok"


def test_deit_001():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag'
    r = requests.request('post', url=url, params=b, json=edit)
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.json()['errcode'] == 0
    assert r.json()['errmsg'] == "ok"

def test_drop_001():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag'
    r = requests.request('post', url=url, params=b, json=drop)
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.json()['errcode'] == 0
    assert r.json()['errmsg'] == "ok"


# pytest --clean-alluredir --alluredir ./result  清除原来的json生成新json文件
# allure generate result -o ./report --clean 生成allure报告
