import pytest
from wework.api.api_corp_tag import CorpTap


class TestCropTap:
    def set_up_class(self):
        self.corptap = CorpTap()

    def test_001(self):
        r = self.corptap.add_corp_tag("xxx")
        assert r.status_code == 200

    @pytest.mark.smoke
    @pytest.mark.parametrize('id,name,check', [
        ["ett_ZrEAAAtvx0Xibb3lSu4_IDG3OHTg", "xxx", 0],
        ["ett_ZrEAAAtvx0Xibb3lSu4_IDG3OHTg", "123", 0],
        ["ett_ZrEAAAtvx0Xibb3lSu4_IDG3OHTg", "@#$", 0],
        ["ett_ZrEAAAtvx0Xibb3lSu4_IDG3OHTg", "XXX", 0],
        ["ett_ZrEAAAtvx0Xibb3lSu4_IDG3OHTg", "老王", 0],
    ], ids=["英文", "数字", "字符", "大写字母", "汉字"])
    def test_edit_corp_tag(self, id, name, check):
        r = self.corptap.edit_corp_tag(id, name)
        assert r.status_code == 200
        assert r.json()["errcode"] == check

    def test_add(self):
        pass
        # @pytest.mark.smoke
        # @pytest.mark.parametrize('id,name,check', [], ids=["group_name"])
        # def test_add_corp_tag(self, name, check, id):
        #     r = self.corptap.add_corp_tag(name, **id)
        #     assert r.status_code == 200
        #     assert r.json()["errcode"] == check
