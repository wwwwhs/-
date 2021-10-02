# todo1.编写pytest能识别的测试用例
"""
pytest框架用例的识别方式
1.文件:test_*.py、*_test.py
2.类：Test
3.方法：test_*():
"""


def test_000():
    pass


class TestCal:
    def test_001(self):
        pass