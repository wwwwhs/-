import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def db():
    print(DB())
    return DB()

class DB:
    def __init__(self):
        self.intransaction = []

    def select(self):
        return 4, 5


# @pytest.fixtrue()
# def time_data()
#     time = datatime.datatime.now().strftime('%Y-%m-%d %H:%M:%S')
#     return time


@pytest.fixture()
def get_token():
    data = {
        "method": "get",
        "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        "params": {
            "corpid": "ww9d1346c103e1fee0",
            "corpsecret": ""
                    }
            }
    token = requests.request(**data).json()['access_token']
    yield token
    print(token)