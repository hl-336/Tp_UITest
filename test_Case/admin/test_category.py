# 以pytest结构层面定义测试
# 1.定义测试类
# 2.定义测试方法
# -----------------------------------------------------------------
# 以测试用例步骤层面来填充代码
# a.打开浏览器   不管该测试类中存在多少个测试方法,整个模块在执行测试的时候只会打开一次浏览器,
# 整个测试类中只会执行一次的动作放在类级别初始化方法中
# b.每执行一个测试场景都需要回归到原点,每个测试方法之前都要执行的代码放在函数级别的初始化方法中
# c.执行新增分类 (多种情况的测试)，
# d.关闭浏览器  在整个测试用例模块都执行完毕之后再关闭浏览器
import time

import pytest

from page.admin.cate_page import CatePage
from page.admin.home_page import HomeProxy
from utils import UtilsDriver

@pytest.mark.run(order=3)
class TestCateGory:

    def setup_class(self):
        # 获取浏览器驱动(打开测试网址)
        self.driver = UtilsDriver.get_admin_driver()

    def setup(self):
        # 回到后台管理系统首页
        time.sleep(2)
        self.driver.get("http://localhost/index.php/Admin/Admin/login")

    # 测试新增分类
    def test_add_category(self):
        # 跳转到分类管理的界面,就要调用代表着主页Home_page中业务层跳转分类方法
        HomeProxy().to_cate_page()
        # 跳转到分类管理界面之后,需要完成新增分类操作
        # 新增分类操作封装cate_page的对象中,只需要调用该页面对象中的新增分类的实例方法就可以完整分类新增
        CatePage().add_cate("TestCat", "锤子", "电脑、办公", "手机 、 数码 、 通信", 1, 1)

    def teardown_class(self):
        UtilsDriver.quit_admin_driver()
