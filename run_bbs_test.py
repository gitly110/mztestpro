import os
import smtplib
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText


# 定义发送邮件
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = 'liuyuannew@163.com'
    msg['To'] = '1685500561@qq.com'

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('liuyuannew@163.com', 'liuyuan1')
    smtp.sendmail('liuyuannew@163.com', '1685500561@qq.com', msg.as_string())
    smtp.quit()
    print('email has send out')


# 查找测试报告目录，找到最新的测试报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './bbs/report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='魅族社区自动化测试报告', description='测试环境：windows 7，浏览器：chrome')
    discover = unittest.defaultTestLoader.discover('./bbs/test_case', pattern='*_sta.py')
    runner.run(discover)
    fp.close()

    file_path = new_report('./bbs/report/')
    send_mail(file_path)
