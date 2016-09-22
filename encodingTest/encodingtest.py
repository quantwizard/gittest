# -*- coding: utf-8 -*-
import sys


def main1():
    print sys.getdefaultencoding()
    print "----"
    print sys.stdout.encoding
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    # print sys.getdefaultencoding()
    test_str = "好"
    test_uni = u"好"

    print "str: %s" % test_str
    print test_uni.encode('utf-8', 'xmlcharrefreplace')
    print test_uni
    print "----"
    # print test_uni.encode()


def main():
    # 该测试显示不论是str类型还是unicode类型，最终存储在文件中
    # 时都是使用utf-8编码后存储的，即存储的都是"e5a5bd" 字节码
    # 注：可以用sublime十六进制方式打开文件
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    with open("strfile.txt", "w") as strfile:
        strfile.write("好")

    with open("unicodefile2.txt", "w") as unifile:
        unifile.write(unicode("好", 'utf-8'))

    reload(sys)
    sys.setdefaultencoding('utf-8')
    with open("unicodefile.txt", "w") as unifile:
        unifile.write(u"好")


if __name__ == '__main__':
    main1()
