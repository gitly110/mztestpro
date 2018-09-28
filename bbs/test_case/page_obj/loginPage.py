from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class Login(Page):
    '''
    用户登陆页面
    '''

    url = '/'
    # 定位
    bbs_login_user_loc = (By.XPATH, '//*[@id="mzCust"]/div/img')  # //*[@id="bbs-avatar"]/img
    bbs_login_button_loc = (By.ID, 'mzLogin')

    # Action
    def bbs_login(self):
        above = self.find_element(*self.bbs_login_user_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        #self.find_element(*self.bbs_login_user_loc).click()
        sleep(1)
        self.find_element(*self.bbs_login_button_loc).click()

    # 定位
    login_username_loc = (By.ID, 'account')
    login_password_loc = (By.ID, 'password')
    login_button_loc = (By.ID, 'login')

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def user_login(self, username='username', password='1111'):
        '''获取的密码登录'''
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(3)

    user_error_hint_loc = (By.XPATH, '//span[@for="account"]')
    pwd_error_hint_loc = (By.XPATH, '//span[@for="password"]')
    user_login_success_loc = (By.ID, 'mzCustName')

    # 用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    # 密码错误提示
    def pwd_error_hint(self):
        return self.find_element(*self.pwd_error_hint_loc).text

    # 登陆成功用户名
    def user_login_sucess(self):
        return self.find_element(*self.user_login_success_loc).text




