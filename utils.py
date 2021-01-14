from selenium import webdriver

# 整个项目工程很多地方都需要获取已经创建好了的驱动对象
from selenium.webdriver.common.by import By


class UtilsDriver:
    # 存储TPshop后台管理系统驱动对象的私有属性
    __admin_driver = None

    # 创建或获取驱动的对象的公用方法
    # 1、创建驱动对象时需要将创建好的窗口存储到私有属性__admin_driver中也就是要修改该变量值而只有类级别的方法才有权限修改
    # 2、如果以实例属性的方式存储浏览器驱动对象,那么在调用方法时就必须创建UtilsDriver的实例对象,每次创建实例对象,其对应的实例
    # 属性都不是同一个,产生的结果还是会打开多个浏览器
    @classmethod
    def get_admin_driver(cls):
        # 如果__admin_driver当前不为空，则代表代码之前已经打开浏览器,那么只需要直接返回已经打开的浏览器驱动对象即可，不需要重新创建
        if cls.__admin_driver is None:
            # 创建驱动对象,因为后续对于该驱动对象需要进行操作,所以需要将创建的好的驱动对象先存储起来
            cls.__admin_driver = webdriver.Chrome()
            # 窗口最大化
            cls.__admin_driver.maximize_window()
            # 隐式等待
            cls.__admin_driver.implicitly_wait(10)
        # 返回创建好的驱动对象
        return cls.__admin_driver

    # 设置一个浏览驱动关闭标识变量
    __admin_key = True

    # 修改关闭驱动对象变量值的类方法
    @classmethod
    def chang_admin_key(cls, key):
        cls.__admin_key = key

    # 关闭后台管理驱动对象的方法
    @classmethod
    def quit_admin_driver(cls):
        # 为加强代码的健壮,防止在没有创建驱动对象之前直接调用关闭驱动对象的方法导致出错的情况则加上判断是否有打开的浏览器
        if cls.__admin_driver is not None and cls.__admin_key:
            # 1、直接拿到驱动对象之后调用quit()会关闭浏览器窗口,但是不会清除__admin_driver中的缓存值,如果不清楚,则再次调用get_admin_driver就不会
            # 打开浏览器窗口
            cls.__admin_driver.quit()
            # 2、实例方法不能直接修改私有属性所以需要将方法修改为类级别的方法
            cls.__admin_driver = None

    # 存储TPshop门户网站系统驱动对象的私有属性
    __buyer_driver = None

    # 创建或获取驱动的对象的公用方法
    # 1、创建驱动对象时需要将创建好的窗口存储到私有属性__admin_driver中也就是要修改该变量值而只有类级别的方法才有权限修改
    # 2、如果以实例属性的方式存储浏览器驱动对象,那么在调用方法时就必须创建UtilsDriver的实例对象,每次创建实例对象,其对应的实例
    # 属性都不是同一个,产生的结果还是会打开多个浏览器
    @classmethod
    def get_buyer_driver(cls):
        # 如果__admin_driver当前不为空，则代表代码之前已经打开浏览器,那么只需要直接返回已经打开的浏览器驱动对象即可，不需要重新创建
        if cls.__buyer_driver is None:
            # 创建驱动对象,因为后续对于该驱动对象需要进行操作,所以需要将创建的好的驱动对象先存储起来
            cls.__buyer_driver = webdriver.Chrome()
            # 窗口最大化
            cls.__buyer_driver.maximize_window()
            # 隐式等待
            cls.__buyer_driver.implicitly_wait(10)
        # 返回创建好的驱动对象
        return cls.__buyer_driver

    # 关闭BUYER门户网站驱动对象的方法
    @classmethod
    def quit_buyer_driver(cls):
        # 为加强代码的健壮,防止在没有创建驱动对象之前直接调用关闭驱动对象的方法导致出错的情况则加上判断是否有打开的浏览器
        if cls.__buyer_driver is not None:
            # 1、直接拿到驱动对象之后调用quit()会关闭浏览器窗口,但是不会清除__admin_driver中的缓存值,如果不清楚,则再次调用get_admin_driver就不会
            # 打开浏览器窗口
            cls.__buyer_driver.quit()
            # 2、实例方法不能直接修改私有属性所以需要将方法修改为类级别的方法
            cls.__buyer_driver = None


# 根据文本判断元素是否存在公用函数
def is_el_exist(qddx, text):
    # 所要定位元素的xapth
    xapth_str = "//*[contains(text(),'{}')]".format(text)
    try:
        # 如找到则将元素对象存储到is_suc的变量中,非常字符串为True
        is_suc = qddx.find_element(By.XPATH, xapth_str)
    except Exception as e:
        # 如找不到则is_suc存储一个False值
        is_suc = False
    return is_suc
