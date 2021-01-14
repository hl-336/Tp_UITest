import pytest

from utils import UtilsDriver

@pytest.mark.run(order=99)
class TestEnd:

    def test_end(self):
        # 将关闭浏览器驱动对象关闭标识变量修改为Ture
        # 修改完毕之后,主动调用quit_admin_driver
        UtilsDriver.chang_admin_key(True)
        UtilsDriver.quit_admin_driver()