from selenium import webdriver
import os


# 截图函数
def insert_img(driver, file_name):
    # 找出bbs路径
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 获取当前脚本路径的上一层
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]

    file_path = base + '/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver, 'baidu.png')
    driver.quit()



