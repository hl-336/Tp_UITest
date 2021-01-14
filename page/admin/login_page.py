# 对象库层:
# 1.维护、管理元素定位方式 --->通过实例属性来进行管理
# 2.定位界面上所有需要使用的元素对象  --->通过实例方法来进行定位
import allure
from selenium.webdriver.common.by import By

from base.admin.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        # 重写父类的初始化方法
        super().__init__()
        # 用户名输入框
        self.username = (By.NAME, "username")
        # 密码输入框
        self.passwrod = (By.NAME, "password")
        # 验证码
        self.code = (By.NAME, "vertify")
        # 登陆按钮
        self.login_btn = (By.NAME, "submit")

    # 找到用户名输入框
    def find_username(self):
        # 通过self调用父类元素定位的方法找到具体的元素对象
        return self.fd_em(self.username)

    # 找到密码输入框
    def find_passwrod(self):
        return self.fd_em(self.passwrod)

    # 找到验证码输入框
    def find_code(self):
        return self.fd_em(self.code)

    # 找到登陆按钮
    def find_login_btn(self):
        return self.fd_em(self.login_btn)


# 操作层:
# 实例方法到底定义几个:
#    在手工形式的测试用例中有多少条操作步骤就封装多少个实例方法,测试方法含义和手工测试用例的步骤需要对应上
class LoginHandle(BasePage):
    """
    1.组织好操作层的结构 --->定义类，定义实例方法
    2.分析操作步骤的实现 --->模拟输入的方法可以通过调用父类的公用方法来实现,只需要提供要输入信息的元素
    对象和文本即可，元素对象可以通过调用对象库层的方法拿到
    """

    def __init__(self):
        super().__init__()
        self.login_page = LoginPage()

    # 输入用户名
    @allure.step(title="输入用户名")
    def input_username(self, user):
        # 调用父类模拟输入方法(el=用户名的元素对象,text=输入的文本)
        self.type_ele(el=self.login_page.find_username(), text=user)

    # 输入密码
    @allure.step(title="输入密码")
    def input_pwd(self, pwd):
        # 调用父类模拟输入方法(el=密码的元素对象,text=输入的文本)
        self.type_ele(el=self.login_page.find_passwrod(), text=pwd)

    # 输入验证码
    @allure.step(title="输入验证码")
    def input_code(self, code):
        # 调用父类模拟输入方法(el=验证码的元素对象,text=输入的文本)
        self.type_ele(el=self.login_page.find_code(), text=code)

    # 点击登陆按钮
    @allure.step(title="点击登陆按钮")
    def click_login_btn(self):
        # 拿到登陆按钮的元素对象,调用点击方法
        self.login_page.find_login_btn().click()


# 业务层:
# 连续调用操作层中定义好多个操作实例方法,形成完整测试用例步骤
class LoginProxy:

    def __init__(self):
        # 不想每次的调用实例方法时都去创建一次操作层的实例对象
        # 那么提前创建好操作层的实例对象并存储的到当前类的实例
        # 属性中方便后续调用
        self.login_handle = LoginHandle()

    # 后台管理系统登陆
    def admin_login(self, user, password, code):
        # 1.输入用户名
        self.login_handle.input_username(user=user)
        # 2.输入密码
        self.login_handle.input_pwd(pwd=password)
        # 3.输入验证码
        self.login_handle.input_code(code=code)
        # 4.点击登陆
        self.login_handle.click_login_btn()
