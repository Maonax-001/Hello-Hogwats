import unittest
#4。discover 发现某个路径下 符合pattern规则的文件里的测试用例
from HTMLReport.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == "__main__":

    # test_dir = r"C:\Users\11418\PycharmProjects\测试开发进阶"
    test_dir = "./"  #当前路径
    discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
    # print(type(discover))
    # print("{}".format(discover))
    # unittest.TextTestRunner(verbosity=2).run(discover)

    report_title = "---test Search 测试报告---"
    desc = "第二次尝试自己发报告"
    report_file = "report.html"

    #第三方框架分析生成测试报告
    with open(report_file,"wb") as report:
        runner = HTMLTestRunner(stream=report,title=report_title,description=desc)
        runner.run(discover)

