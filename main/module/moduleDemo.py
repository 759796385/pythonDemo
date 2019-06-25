#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' 模块的文档注释，任何模块代码第一个字符串都视为模块的注释 '
# 上面两行是标准注释，第一行让文件在各平台运行（没有好像也行），第二行表示文件用utf8编码
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
        print(args)
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()

# sys模块有个argv变了，存储了命令行所有参数，第一个参数永远是python文件全路径名称
# 当前文件运行时，会将__name__命名为__main__，该类被其它类引用，这个name就失效了

# 作用域如同java中的作用域
# 不带任何修饰的 就是public
# 两个下划线的 是特殊变量，作为特殊用途，一般自己使用不定义   如:__author__，__name__
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc
# python好渣，无法从语法上限制访问，只能通过命名来进行特殊约定
