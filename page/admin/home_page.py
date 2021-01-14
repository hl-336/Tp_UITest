from selenium.webdriver.common.by import By

from base.admin.base_page import BasePage


# 对象库层
class HomePage(BasePage):
    # 对象库层:
    # 1.维护、管理元素定位方式 --->通过实例属性来进行管理
    # 2.定位界面上所有需要使用的元素对象  --->通过实例方法来进行定位
    def __init__(self):
        super().__init__()
        # 商城页
        self.shop_link = (By.LINK_TEXT, "商城")
        # 商品分类TAB
        self.cate_tab = (By.CSS_SELECTOR, "[data-param*='categoryList|G']")

    # 找到商城页超链接
    def find_shop_link(self):
        """方法/函数在调用之后会执行方法/函数其内部代码，如果需要获取其操作之后的结果，就一定要加上return"""
        return self.fd_em(self.shop_link)

    # 找到商品分类TAB
    def find_cate_tab(self):
        return self.fd_em(self.cate_tab)


# 操作层
class HomeHandle:
    """
    1.组织好操作层的结构 --->定义类，定义实例方法,在手工形式的测试用例中有多少条操作步骤就封装多少个实例方法,
    测试方法含义和手工测试用例的步骤需要对应上
    2.分析操作步骤的实现 --->模拟输入的方法可以通过调用父类的公用方法来实现,只需要提供要输入信息的元素
    对象和文本即可，元素对象可以通过调用对象库层的方法拿到
    """

    def __init__(self):
        self.home_page = HomePage()

    # 点击顶部商城
    def click_shop_link(self):
        # 找到元素对象直接调用click()
        self.home_page.find_shop_link().click()

    # 点击分类管理
    def click_cate_tab(self):
        self.home_page.find_cate_tab().click()


# 业务层
class HomeProxy:
    """
    1.形成手工测试用例中的测试步骤的一步或者多步
    """
    def __init__(self):
        self.home_handle = HomeHandle()

    # 跳转商品分类页面
    def to_cate_page(self):
        # 点击顶部商城
        self.home_handle.click_shop_link()
        # 点击分类管理
        self.home_handle.click_cate_tab()
