import requests
import json


class AccessToken:
    _ding = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwd72b10b8b35b649a&corpsecret=fKbsBFrahcfJ9I5mRWKjY6JddFkoT7tcY94NmqKOZoE'
    _headers = {"Content-type": "application/json;charset=utf-8"}

    def send(self, data):
        requests.post(url=self._ding, headers=self._headers, data=json.dumps(data))

    def token(self):
        respond = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwd72b10b8b35b649a&corpsecret'
            '=fKbsBFrahcfJ9I5mRWKjY6JddFkoT7tcY94NmqKOZoE')
        responds = respond.json()
        token = responds.get('access_token')
        return token


# class WeWork(AccessToken):
#     _url = 'https://work.weixin.qq.com/wework_admin/frame#customer/tagconfig'
#     _headers = {"Content-type": "application/json;charset=utf-8"}
#
#     def __int__(self):
#         pass
#
#     def send(self, data):
#         requests.post(url=self._url, headers=self._headers, data=json.dumps())
#
#     def inquire_link(self):
#         link = {
#             "tag_id":
#                 [
#                     "小王"
#                 ],
#             "group_id":
#                 [
#                     "老王"
#                 ],
#             "access_token": AccessToken.token
#                 }
#
#
# if __name__ == '__main__':
#     WeWork().inquire_link()
# ____________查询
a = AccessToken().token()
url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
params = {'access_token': a}


search = {
    "tag_id":
        [
            "小小王"
        ],
    "group_id":
        [
            "老王头tou",
        ]
}
r1 = requests.post(url, params=params, data=search)
print(json.dumps(r1.json(), indent=2, ensure_ascii=False))


# -------------添加
# a = AccessToken().token()
# url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag'
# params = {'access_token': a}
#
# add = {
#     "group_id": "ett_ZrEAAAAc9D6tRPcM34NuXeiSd31w",
#     "group_name": "老王",
#     "tag": [{
#             "name": "小小王",
#         }
#     ]
#
# }
# r2 = requests.post(url, params=params, json=add)
# print(json.dumps(r2.json(), indent=2, ensure_ascii=False))


# _____________________编辑
# a = AccessToken().token()
# url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag'
# params = {'access_token': a}
# edit = {
#     "id": "ett_ZrEAAAAc9D6tRPcM34NuXeiSd31w",
#     "name": "老王头tou",
# }
# r3 = requests.post(url, params=params, json=edit)
# print(json.dumps(r3.json(), indent=2, ensure_ascii=False))


# ___________________删除
# a = AccessToken().token()
# url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag'
# params = {'access_token': a}
# drop = {
#     "tag_id": [
#         "ett_ZrEAAA9XjvFMC4_nWcb9iKzZWzEg"
#     ]
# }
# r4 = requests.post(url, params=params, json=drop)
# print(json.dumps(r4.json(), indent=2, ensure_ascii=False))