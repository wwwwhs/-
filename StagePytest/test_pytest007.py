# todo 7. pytest fixture 参数传递
"""
"""
import datetime

import pytest


@pytest.fixture()
def time_data():
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return time


import pytest
import requests

par_to_test = [{
    "case": "serach a word :haha",
    "headers": {},
    "querystring": {
        "wd": "hah"
    },
    "payload": {},
    "expected": {
        "status_code": 200
    }
},
    {
        "case": "serach a word2 :kuku",
        "headers": {},
        "querystring": {
            "wd": "kuku"
        },
        "payload": {},
        "expected": {
            "status_code": 200
        }},

    {
        "case": "serach a word3 :xiaoyulaoshi",
        "headers": {},
        "querystring": {
            "wd": "xiaoyulaoshi"
        },
        "payload": {},
        "expected": {
            "status_code": 200
        }}
]


@pytest.fixture(params=par_to_test)
def class_scope(request):
    return request.param


def test_baidu_search(class_scope):
    url = "https://www.baidu.com"
    r = requests.request("GET", url, data=class_scope["payload"], headers=class_scope["headers"],
                         params=class_scope["querystring"])
    assert r.status_code == class_scope["expected"]["status_code"]