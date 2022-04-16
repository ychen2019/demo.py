# _*_ coding=utf-8 _*_

### 一、基础语法 ###
# list =["a", "b", "c"]
# print list              # python2.x的print语句
# from __future__ import print_function  # 导入__future__包
# print(list)             # Python2.x 的 print 语句被禁用，使用报错

# #1.1、注释
# #前注释
# print ("Hello, Python!")  #后注释

'''print("hello");print("runoob")'''
""" print("hello");print("runoob") """

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# #1.2、输入
# raw_input("按下 enter 键退出，其他任意键显示...\n")

# #1.3、换行
# x="a"
# y="b"
# # 换行输出
# print x
# print y
# print '---------'
# # 不换行输出
# print x,     # 注意后方逗号
# print y,111
# # 不换行输出
# print x,y

# #1.4、代码组
# if True:
#     print("yes")
# else:
#     print("no")

# #1.5、变量赋值
# # Numbers（数字）
# # String（字符串）
# # List（列表）
# # Tuple（元组）
# # Dictionary（字典）
# a = b = c = 1
# print a
# print b
#
# a, b, c = 2, 4, "john"
# print a
# print c

# 二、变量类型
# #python 四种不同的数字类型：
# # int（有符号整型）
# # long（长整型，也可以代表八进制和十六进制）  # long类型只存在于Python2.X版本
# # float（浮点型）
# # complex（复数）
# counter = 100   # 整型变量
# miles = 1000.0  # 浮点型
# name = "John"   # 字符串
# print counter
# print miles
# print name

# #2.1、数字
# #数字 数据类型用于存储数值,不需要赋值时 加引号
# #数字 是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象
# var1 = 1
# var2 = 10
# print var1,var2
# del  var1
# print var1,var2

# #2.2、字符串
# #字符串或串(String)是由数字、字母、下划线组成的一串字符
# # 从左到右索引默认0开始的，最大范围是字符串长度少1
# # 从右到左索引默认-1开始的，最大范围是字符串开头
# s = 'abcdefg'
# print s[1:5]

# #加号（+）是字符串连接运算符，星号（*）是重复操作
# str = 'Hello World!'
# print str       # 输出完整字符串
# print str[0]    # 输出字符串中的第一个字符
# print str[2:5]  # 输出字符串中第三个至第六个之间的字符串
# print str[2:]   # 输出从第三个字符开始的字符串
# print str * 2   # 输出字符串两次
# print str + "TEST"  # 输出连接的字符串
# print str[1::2] # 分别输出了e,l,空格，o,l,!
# print str[-5:-1]

# #2.3、列表
# #List（列表）是Python中使用最频繁的数据类型
# #列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）
# list1 = ['one',123,4.56,'two','four',55,66,77,88]
# list2 = ['three','oh']
#
# print list1
# print list1[1]
# print list1[1:3]
# print list1[1:]
# print list1[:2]
# print list1[0:3:2]
# print '------'
# print list1[-1]
# print list1[-3:-1]
# print list1[-3:]
# print list1[:-1]
# print '------'
# print list2 * 2
# print list1 + list2

# #2.4、元组
# #元组是另一个数据类型，类似于 List（列表）
# #元组用 () 标识，内部元素用 逗号隔开，但是元组不能 二次赋值，相当于只读列表
# tuple1 = ('one',22,'three',4.56,55,66,77,88)
# tuple2 = ('hi','hello',33)
# list1 = ['h','i','j']
# #元组内容不可修改，列表可以
# # tuple1[1] = 100
# list1[1]  =200
# # print tuple1[1]
# print '------'
# print list1[1]
# print tuple1
# print tuple1[1]
# print tuple1[1:3]
# print tuple1[1:]
# print tuple1[:3]
# print tuple1[0:7:2]
# print '------'
# print tuple1[-3:-1]
# print tuple1[-3:]
# print tuple1[:-1]
# print tuple1[0:7:3]
# print tuple1[-1:-2]
# print '------'
# print tuple2 * 2
# print tuple1 + tuple2

# #2.5、字典  dictionary
# #字典是除 列表 以外python之中最灵活的内置数据结构类型。列表是 有序 的对象集合，字典是 无序 的对象集合
# #两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
# dict1 = {1:'one',2:'two','three':33,'four':'four',5:5}
#
# print dict1
# print dict1.keys()
# print dict1.keys()[1]
# print dict1.keys()[1:3]
# print dict1.keys()[-1]
# print dict1.keys()
# print dict1.keys()[-5:-1:2]
# print '------'
# print dict1.values()

# #数据类型转换
# # int(x [,base])，，将x转换为一个整数
# x = 1.51
# print int(x)

# # long(x [,base] )，，将x转换为一个长整数
# x = 1234.567
# print long(x)

# # float(x)，，将x转换到一个浮点数
# x = 1
# print float(x)

# # str(x)，，将对象 x 转换为字符串
# x = 11
# print str(x)

# # list(s)，，将序列 s 转换为一个列表
# x = 'hello,boy'
# print list(x)

# # tuple(s)，，将序列 s 转换为一个元组
# x = [1,'two',3]
# print tuple(x)

#未解决
# # dict(d)，，创建一个字典。d 必须是一个序列 (key,value)元组
# x = (1,'one')
# print dict(x)

# # set(s)，，转换为可变集合

# # repr(x)，，将对象 x 转换为表达式字符串
# x = [1,'hh']
# print repr(x)

# # eval(str)，，用来计算在字符串中的有效Python表达式,并返回一个对象




















