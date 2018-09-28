from time import sleep
import unittest, random, sys
from bbs.test_case.models import myunit, function
from bbs.test_case.page_obj.loginPage import Login

sys.path.append('./models')
sys.path.append('./page_obj')


class LoginTest(myunit.MyTest):
    """社区登录测试"""

    # 测试用户登录
    def user_login_verify(self, username='', password=''):
        l = Login(self.driver)
        l.user_login(username, password)

    # def test_login1(self):
    #     """用户名密码为空"""
    #     self.user_login_verify()
    #     po = Login(self.driver)
    #     self.assertEqual(po.user_error_hint(), '账号不能为空')
    #     self.assertEqual(po.pwd_error_hint(), '密码不能为空')
    #     function.insert_img(self.driver, 'user_pwd_empty.png')
    #     print('login1被执行了')
    #
    # def test_login2(self):
    #     """用户名正确，密码为空"""
    #     self.user_login_verify(username='pytest')
    #     po = Login(self.driver)
    #     self.assertEqual(po.pwd_error_hint(), '密码不能为空')
    #     function.insert_img(self.driver, 'pwd_empty.png')
    #
    # def test_login3(self):
    #     """用户名密码不匹配"""
    #     character = random.choice('qwertyuioplkjhgfdsazxcvbnm')
    #     username = 'zhangsan' + character
    #     self.user_login_verify(username=username, password='123456')
    #     po = Login(self.driver)
    #     self.assertEqual(po.user_error_hint(), '密码与账号不匹配')
    #     function.insert_img(self.driver, 'user_psw_true.png')

    def test_login4(self):
        """用户名密码正确"""
        self.user_login_verify(username='zhangsan', password='123456')
        po = Login(self.driver)
        # self.assertEqual(po.user_login_sucess())
        function.insert_img(self.driver, 'user_psw_true.png')
    print('sta被执行了')


if __name__ == "__main__":
    unittest.main()
