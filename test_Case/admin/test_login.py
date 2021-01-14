# 以pytest结构层面定义测试
# 1.定义测试类
# 2.定义测试方法
# -----------------------------------------------------------------
# 以测试用例步骤层面来填充代码
# a.打开浏览器   不管该测试类中存在多少个测试方法,整个模块在执行测试的时候只会打开一次浏览器,
# 整个测试类中只会执行一次的动作放在类级别初始化方法中
# b.每执行一个测试场景都需要回归到原点,每个测试方法之前都要执行的代码放在函数级别的初始化方法中
# c.执行登陆场景 (多种情况的测试)，通过登录页面PO文件业务层所提供登陆方法来完成登陆，具体测试步骤需要写在测试方法中
# d.关闭浏览器  在整个测试用例模块都执行完毕之后再关闭浏览器
import time

import allure
import pytest
from selenium.webdriver.common.by import By

from page.admin.login_page import LoginProxy
from utils import UtilsDriver, is_el_exist


@pytest.mark.run(order=2)
class TestAdminLogin:

    # 步骤a
    def setup_class(self):
        # 打开浏览器  --->调用utils工具中获取浏览器驱动对象的方法
        self.driver = UtilsDriver.get_admin_driver()

    # 步骤b
    def setup(self):
        time.sleep(2)
        self.driver.get("http://localhost/index.php/Admin/Admin/login")

    def test_admin_login(self):
        # 步骤c
        # 调用业务层登陆方法完成登陆
        LoginProxy().admin_login("admin", "admin123", "8888")
        # 对登陆结果进行判断 assert expression  期望expression的返回结果为真
        # 1.期望登陆成功之后右上角显示的用户名 == 登陆时所用的用户
        # 2.期望登陆跳转到后台管理首页,首页中有商城超链接的元素,那只要能找得到商城的元素对象则证明登陆成功
        # 断言1:实际结果
        msg = self.driver.find_elements(By.CSS_SELECTOR, ".manager .name")[1].text
        # 断言1:期望结果
        expect = "admin"
        assert msg == expect

        # 断言2:期望能找到【商城】的超链接
        assert is_el_exist(self.driver, "商城")

        # 截图并且体现在测试报告中
        allure.attach(self.driver.get_screenshot_as_png(),"登陆结果",allure.attachment_type.PNG)

    # 步骤d
    def teardown_class(self):
        UtilsDriver.quit_admin_driver()
