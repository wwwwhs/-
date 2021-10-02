# todo 5. pytest fixture 用法
"""
测试夹具 fixture :我们可以在不修改当前函数代码逻辑的情况下，通过 fixture 来额外添加一些处理
定义
    fixture 是一个函数，在函数上添加注解@pytest.fixture来定义
    定义在 conftest.py 中，无需 import 就可以调用
    定义在其他文件中，import 后也可以调用
    定义在相同文件中，直接调用
使用
    第一种使用方式是@pytest.mark.usefixtures(fixturename)（如果修饰 TestClass 能对类中所有方法生效）
    第二种使用方式是作为函数参数
    第三种使用方式是 autouse（不需要显示调用，自动运行）
        autouse 遵循 scope 的规则，scope="session"整个会话只会运行 1 次，其他同理
        autouse 定义在 module 中，module 中的所有 function 都会用它（如果 scope="module"，只运行 1 次，如果 scope="function"，会运行多次）
        autouse 定义在 conftest.py，conftest 覆盖的 test 都会用它
        在使用 autouse 时需要同时注意 scope 和定义位置
    fixture 的顺序优先按 scope 从大到小，session > package > module > class > function
    夹具范围
Fixtures在首次被测试请求时创建，并根据它们的scope:
    function:默认范围，在测试结束时销毁夹具。
    class:在类中的最后一个测试的拆卸期间，夹具被破坏。
    module:在模块中最后一个测试的拆卸期间，夹具被破坏。
    package:在拆解包中的最后一个测试期间，夹具被破坏。
    session:夹具在测试会话结束时被销毁。
    笔记:
    Pytest一次只缓存一个fixture实例，这意味着当使用参数化fixture时，pytest可能会在给定范围内多次调用fixtures
"""
import datetime

import pytest

from StagePytest.calculator import Calcuator


@pytest.fixture(scope="class", autouse=True)
def time_data():
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(time)


def test_mul_001():
    result = Calcuator().mul(4, 5)
    assert result == 20


def test_mul_003():
    result = Calcuator().mul(4, 5)
    print(result)
    assert result == 20


