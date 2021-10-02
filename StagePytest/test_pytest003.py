# todo 3.pytest运行方式
import pytest
'''
在终端中输入pytest --help 可以查看指令
pytest --collect-only 查看可执行的用例
pytest test_*.py 执行测试用例
pytest -v 打印详细运行日志
pytest -x 发现报错立即停止
pytest --setup-show 用例执行的夹具
pytest --maxfail=2 最大报错为2
pytest -m 运行mark标记用例
pytest --lf 执行上次报错用例
pytest --ff 先执行上次报错用例，在执行其他的
pytest --junitxml=./result.xml 将执行结果生成xml文件

配置文件 pytest.ini : [pytest]
    markers 自定义mark 标签名
    addopts 运行时参数(可添加多个命令参数，空格分隔，所有参数与命令一致)
    norcursedirs = result logs datas test_demo* 运行时忽略某些文件a
'''


from StagePytest.calculator import Calcuator

def test_add_001():
    result = Calcuator().add(5, 4)
    print(result)
    assert result == 9


def test_add_002():
    result = Calcuator().add(0.1, 5)
    print(result)
    assert result == 5.1


def test_add_003():
    result = Calcuator().add(1000, 5000)
    print(result)
    assert result == 6000