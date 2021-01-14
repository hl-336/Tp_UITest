# 1.有自动化测试框架实施公司,基类文件基本已经封装不需要编写,而且不能随意改动
# 2.如果有自动化框架,则需要自行编写
from selenium.webdriver.support.wait import WebDriverWait

from utils import UtilsDriver


class BasePage:

    # 创建初始化方法,在初始化方法中定义的一个实例属性的来存储打开的浏览器驱动对象
    def __init__(self):
        self.driver = UtilsDriver.get_admin_driver()

    # 公用的元素定位的方法
    # 原因:期望通过显示等待的方法来定位元素,解决元素定位对于页面加载的依赖
    def fd_em(self, location):
        """
        :param location: 对于location的值有要求,必须为元组或者是列表,且其元素必须有2个,第一个必须是定位方式,第二个必须是该定位方式所要求的值
        :return:
        """
        # 驱动对象.元素定位的方法
        # 要定位元素就必须通过元素的信息来决定定位方式和值
        try:
            # 显示等待定位元素
            element = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(*location))
            # 返回找到的元素对象
            return element
        except Exception as e:
            print("找不到元素对象！！！！！！")

    # 公用的模拟输入的方法:封装一个公用的模拟输入的方法,可以支持所有的元素进行输入操作
    def type_ele(self, el, text):
        """
        :param el: 元素对象,在调用方法时必须传递元素对象
        :param text: 要输入文本信息
        :return:
        """
        # 思考:
        # 1.必须有元素对象 需要支持所有的元素对象,所以不能将元素对象给写死,只能通过外部进行传递
        # 2.必须有输入的文本
        el.clear() # el元素对象 .  清除文本
        el.send_keys(text) # el元素对象 . 输入字符串
