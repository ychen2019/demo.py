# -*- coding=utf-8 -*-
# # python 函数（function）
# # 函数是组织好的，可重复使用的，用来实现单一或 相关联功能的代码段
# # 函数能提高应用的模块性和代码的重复利用率
# # python提供了许多内建函数，如 print()。也可以自己创建函数，叫做用户自定义函数

# # 1、定义一个函数
# # 以下是简单的规则：
# # 函数代码块以 def关键词开头，后接函数 标识符名称和 圆括号()
# # 任何 传入参数和 自变量必须放在圆括号中间。圆括号之间可以用于定义参数
# # 函数的第一行语句，可以选择性地使用 文档字符串，用于存放函数说明
# # 函数内容以 冒号起始，并且缩进
# # return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None
# # 2、调用函数
# # 定义一个函数只给了函数一个 名称，指定了函数里包含的 参数和代码块结构。      名称，参数
# # 这个函数的基本结构完成以后，可以通过 另一个函数调用执行，也可以直接从python 提示符执行

# def printme( str ):
#    '打印传入的字符串到标准显示设备上'
#    print str
#    return
# printme ('我要调用一次定义的函数')
# # printme()       # 函数需要传参，不然报错
# # printme (10,20)

# # 3、参数传递
# # 在python中，类型属于对象，变量是没有类型的
# a = [1, 2, 3]
# a = "Runoob"
# # 变量a 是没有类型的，它仅仅是一个对象的引用（一个指针），可以是 List类型对象，也可以指向 String类型对象
# # [1,2,3]是 List类型，"Runoob"是 String类型

# # 3.1、可更改(mutable)与 不可更改(immutable)对象
# # 在python中，数值（numbers）、字符串（strings）, 元组（tuples） 是不可更改的对象，
# # #          列表（list）、字典（dict）等 则是可以修改的对象
# # python中一切 都是对象，严格意义上，我们不能说 值传递还是 引用传递，我们应该说传 不可变对象和传 可变对象

# # 3.2、不可变类型：数值、字符串、元组
# # 变量赋值 a=5后再赋值 a=10，这里实际是新生成一个 int值对象10，再让 a指向它，而5被丢弃，不是改变a的值，相当于新生成了a
# # 可变类型：列表，字典等
# # 变量赋值 la=[1,2,3,4]后再赋值 la[2]=5,则是将列表la的 第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了

# # python函数的参数传递：
# # 不可变类型：
# # 类似 c++的值传递，如 整数、字符串、元组。如fun（a），传递的 只是a的值，没有影响 a对象本身，
# # 比如在 fun（a）内部修改 a的值，只是修改 另一个复制的对象，不会影响 a本身
# # 可变类型：类似 c++的引用传递，如 列表，字典。如 fun（la），则是将la 真正的传过去，修改后fun外部的la也会受影响

# # 传不可变对象
# def ChangeInt(a):
#     a = 10
#
# b = 2
# ChangeInt(b)
# print b
# # int对象2，指向它的变量是 b，在传递给ChangeInt 函数时，按传值的方式复制了变量b，a 和 b都指向了同一个 Int 对象，
# # 在 a=10时，则新生成一个 int值、对象为 10，并让 a指向它

# # 传可变对象
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append(11)
#     print "函数内取值: ", mylist
#     return
#
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print "函数外取值: ", mylist

# # 4、参数
# # 调用函数时可使用的正式参数类型：
# # 必备参数
# # 关键字参数
# # 默认参数
# # 不定长参数

# # 4.1、必备参数
# # 必备参数必须以 正确的顺序传入函数。调用时的 数量必须和声明时的一样
def printme(str):
    "打印任何传入的字符串"
    print str
    return

# 调用printme函数
# printme()     # 必须传入与定义相同数量的参数

# # 4.2、关键字参数
# # 关键字参数和函数调用关系紧密，函数调用使用关键字参数来 确定传入的参数值
# # 使用关键字参数允许函数调用时 参数的顺序与声明时不一致，因为python 解释器能够用 参数名匹配参数值
# def printme(str):
#     "打印任何传入的字符串"
#     print str
#     return
#
# printme('ok')
# printme(str="My string")

# def printinfo(name, age):
#     "打印任何传入的字符串"
#     print "Name: ", name
#     print "Age ", age
#     return
#
# # printme(10,'two')
# printinfo(age=50, name="miki")   # 传入参数要有对应的名称，顺序没要求

# # 4.3、默认参数
# # 调用函数时，默认参数的值如果没有传入，则被认为是 默认值
# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print "Name: ", name
#     print "Age ", age
#     return
#
# printinfo(age=50, name="chen")
# printinfo(name="li")

# # 4.4、不定长参数
# # 你可能需要一个函数能处理比当初声明时 更多的参数，这些参数叫做不定长参数。和上述2种参数不同，声明时 不会命名
# # 加了星号（*）的变量名会存放 所有未命名的变量参数
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print "输出: "
#     print arg1
#     for var in vartuple:
#         print var
#     return
#
# printinfo(10)
# printinfo(70, 60, 50)

# # 5、匿名函数
# # lambda只是一个表达式，函数体比def 简单很多
# # lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中 封装有限的逻辑进去
# # lambda函数拥有自己的命名空间，且不能访问自有参数 列表之外或全局命名空间里的参数
# # 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
# summ = lambda arg1, arg2, arg3: arg1 + arg2 + arg3
#
# print "相加后的值为 : ", summ(10, 20, 30)
# print "相加后的值为 : ", summ(20, 20, 40)

# # 6、return 语句
# # return语句[表达式] 退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句 返回None
# def sum(arg1, arg2):
#     # 返回2个参数的和 "
#     total = arg1 + arg2
#     print "函数内 : ", total
#     # exit()
#     return total
#
# # 调用sum函数
# total = sum(10, 20)
# print sum(1,2)

# # 7、变量作用域
# # 一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限 决定于这个变量是在哪里赋值的
# # 变量的作用域决定了，在哪一部分程序你可以访问哪个特定的变量名称
# # 定义在 函数内部的变量拥有一个 局部作用域，定义在 函数外的拥有 全局作用域
# # 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
# # 调用函数时，所有在 函数内声明的变量名称都将被加入到作用域中

# total = 0  # 这是一个全局变量
# def sum(arg1, arg2):
#     # 返回2个参数的和"
#     total = arg1 + arg2  # total在这里是局部变量.
#     print "函数内是局部变量 : ", total    # 函数内执行
#     return total
#
# sum(10, 20)     # 在定义函数中执行
# print "函数外是全局变量 : ", total





