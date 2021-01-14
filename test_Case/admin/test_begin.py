import pytest

from utils import UtilsDriver

@pytest.mark.run(order=1)
class TestBegin:

    def test_begin(self):
        # 将关闭浏览器驱动对象关闭标识变量修改为False
        # 修改完毕之后,后续所有的测试用例在调用quit_admin_driver
        # 时都不会关闭浏览器
        UtilsDriver.chang_admin_key(False)