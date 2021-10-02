# todo 4.参数化&数据驱动
"""
parametrize(argnames,argvalues,indirect=False,ids=None,scope=None)
    1. argnames: 参数名字
    2. argvalues: 参数值（可以为list和tuple，或者字典列表，字典元祖等）,参数值有N个，用例就会执行N次。
    3. ids 用例名称 与 参数值的下表一致
参数化与数据驱动

@pytest.mark.smoke 标记用例
@pytest.mark.parametrize(‘k1,k2,k3',[[v1,v2,v3],[V1,V2,V3]], ids=['用例名称1','用例名称2'])
    1. 第一个参数是字符串，多个参数中间用逗号隔开
    2. 第二个参数是list,多组数据用列表or元祖类型;传三个或更多参数也是这样传。
    3. list的每个元素都是一个列表or元组，列表or元组里的每个元素和按参数顺序一一对应第一参数字符串
    4. ids= 给每一个用例起名字，对应关系如上
"""

import pytest

from StagePytest.calculator import Calcuator


# 使用方式
# 整数 大数 小数 负数
@pytest.mark.parametrize('a,b,check', [
    (10, 5, 5),
    [1000, 999, 1],
    (0.5, 0.2, 0.3),
    [-1, 10, -11]
], ids=["int", "big", "tiny", "minus"])
def test_sub(a, b, check):
    result = Calcuator().sub(a, b)
    print(result)
    assert result == check


# 使用方法二
@pytest.mark.parametrize("a", [
    (10, 5, 2),
    [1000, 20, 50],
    (0.4, 0.2, 2),
    [-1, 10, -0.1]
], ids=["整数", "大数", "小数", "负数"])
def test_div(a):
    result = Calcuator().div(a[0], a[1])
    assert result == a[2]
