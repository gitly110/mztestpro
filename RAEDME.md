## bbs：

存放BBS项目的测试用例、测试报告和测试数据等。

    data：测试数据

    report：HTML测试报告。其下的image存放截图

    test_case：用例目录，存放用例及相关模块。

        models：公共的配置函数和类。

        page_obj：用例的页面对象（Page Object）。根据自定义规则，
                  以‘*Page.py’命名的文件封装为的页面对象文件。
        *_sta.py：用例文件。根据测试文件匹配规则，以‘*_sta.py’
                  命名的文件被当作自动化测试用例执行。

## driver：

存放浏览器驱动。如selenium-sever-standalone-2.47.0.jar、
Chromedriver.exe等。（根据测试场景，将浏览器驱动复制到系统环境变量path目录下）

## package：

存放自动化用到的扩展包。如HTMLTestRunner.py属于一个单独模块，并作了修改。所以，
需要提前复制把它到python的lib目录下。

## run_bbs_test.py：

项目主程序。用来运行BBS自动化用例。

## startup.bat：

启动selenium server，默认启动driver目录下的selenium-sever-standalone-2.47.0.jar。

## README：

介绍当前项目的架构、配置和使用说明。


