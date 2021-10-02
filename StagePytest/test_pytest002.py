# todo 2.测试装置（夹具）
"""
模块级(setup_module/teardown_module)模块始末，全局的（优先最高）
函数级(setup_function/teardown_function)只对函数用例生效(不在类中)
类级(setup_class/teardown_class)只在类中前后运行一次（在类中） （重点）
方法级(setup_method/teardown_methond)开始于方法始末（在类中）
类里面的（setup/teardown）运行在调用方法的前后（重点）
"""

from StagePytest.calculator import Calcuator
def setup_module():
    print("作用在这个py文件")


def setup_function():
    print("作用在这个py文件-function")


def teardown_module():
    print("模块结束")


def test_003():
    print("@" * 10)


def test004():
    print("--" * 10)


class TestDemo:

    def setup_class(self):
        self.cal = Calcuator()

    def test_add(self):
        self.cal.add()

    def test005(self):
        print("%%" * 10)