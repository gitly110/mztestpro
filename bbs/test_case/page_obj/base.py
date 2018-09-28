class Page(object):
    '''
    页面基础类，用于所有页面继承
    '''

    bbs_url = 'http://bbs.meizu.cn'

    # 初始化参数
    def __init__(self, selenium_driver, base_url=bbs_url, parent=None):
        self.driver = selenium_driver
        self.base_url = base_url
        self.parent = parent
        self.timeout = 30

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        # 判断当前URL是不是我们的目标URL
        # assert self.on_page(), 'Did not land on %s' % url

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    # 打开BBS
    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 更简便调用JavaScript
    def script(self, scr):
        return self.driver.execute_script(scr)

    print('base被调用')

