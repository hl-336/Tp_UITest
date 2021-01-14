# 所有的页面可以统一认知为一个类 (所有的狗有个狗类)
# 页面类的属性就是长在页面上的标签元素,通过实例属性来管理所有的元素对象  (狗有自己的属性:年龄 性别 毛 脚)
# 页面上都有自己可以提供的业务方法  (狗有自己的实例方法:吃喝拉撒)
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.admin.base_page import BasePage


# 分类页面的页面类
class CatePage(BasePage):

    def __init__(self):
        super().__init__()
        # iframe
        self.frame_ele = (By.ID, "workspace")
        # 【新增分类】
        self.add_cate_btn = (By.CSS_SELECTOR, ".add")
        # 分类名称输入框
        self.cate_name = (By.NAME, "name")
        # 手机分类名称输入框
        self.phone_cate_name = (By.NAME, "mobile_name")
        # 一级分类 Select标签元素对象
        self.one_cate = (By.ID, "parent_id_1")
        # 二级分类 Select标签元素对象
        self.two_cate = (By.ID, "parent_id_2")
        # 是否导航
        self.is_nav = (By.CSS_SELECTOR, ".cb-enable")
        # 排序输入框
        self.order_box = (By.ID, "t_sort")
        # 分佣比例输入框
        self.sub_cm_box = (By.NAME, "commission_rate")
        # 【确认按钮】
        self.submit_btn = (By.ID, "submitBtn")

    # 新增分类
    def add_cate(self, cate_name, phone_cate_name, o_catename, t_catename, num, rate):
        """
        :param cate_name: 新增的三级分类名称
        :param phone_cate_name: 新增的手机分类名称
        :param o_catename: 选中一级分类名称
        :param t_catename: 选中二级分类名称
        :param num: 排序权重值
        :param rate: 分佣比率
        :return:
        """
        # 1.frame切换
        # 驱动对象.switch_to.frame(frame元素对象)
        self.driver.switch_to.frame(self.fd_em(self.frame_ele))
        # 2.点击【新增分类】
        self.fd_em(self.add_cate_btn).click()
        # 3.输入分类名称
        self.type_ele(el=self.fd_em(self.cate_name), text=cate_name)
        # 4.输入手机分类名称
        self.type_ele(el=self.fd_em(self.phone_cate_name), text=phone_cate_name)
        # 5.选择一级分类
        # Select(<select>的元素对象).select_by_visiable_text()
        Select(self.fd_em(self.one_cate)).select_by_visible_text(o_catename)
        # 6.选择二级分类:一定要先触发一下二级分类选项的加载
        self.fd_em(self.two_cate).click()
        time.sleep(5)
        Select(self.fd_em(self.two_cate)).select_by_visible_text(t_catename)
        # 7.(*)选择导航
        self.fd_em(self.is_nav).click()
        # 8.输入排序
        self.type_ele(el=self.fd_em(self.order_box), text=num)
        # 9.输入分佣比例
        self.type_ele(el=self.fd_em(self.sub_cm_box), text=rate)
        # 10.点击【确认提交】
        self.fd_em(self.submit_btn).click()
