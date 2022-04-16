# -*- coding=utf-8 -*-

# # python模块(Module)，是一个python文件，以 .py结尾，包含了 python对象定义和 Python语句
# # 模块让你能够有逻辑地组织你的 python 代码段
# # 把相关的代码分配到 一个模块里能让你的代码更好用，更易懂
# # 模块能定义 函数、类和变量，模块里也能包含 可执行的代码

# # 1.1、import 语句
# # 模块定义好后，我们可以使用 import语句来引入模块
# # 当解释器遇到 import语句，如果模块在当前的搜索路径就会被导入
# # 搜索路径是一个解释器会先进行搜索的所有目录的列表。如果想要导入模块 support.py，需要把命令放在 脚本的顶端
# # 一个模块只会被 导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行
# #import runoob_py2.orthers.support
# import support
# # 现在可以调用模块里包含的函数了
# support.print_func("Runoob")

# # 1.2、from...import 语句
# # python的 from语句让你从 模块中导入一个 指定的部分到当前命名空间中
# 如，要导入 模块fib的 fibonacci函数
# from fib import fibonacci
# 这个声明不会把 整个fib模块导入到当前的命名空间中，它只会将 fib里的fibonacci单个,引入到执行这个声明的模块 的全局符号表

# # 1.3、from...import * 语句
# # 把一个模块的 所有内容全都导入到当前的命名空间也是可行的
# # 它提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明 不该被过多地使用
from math import *
# import math   二者有何区别

# # 2 搜索路径
# # 当你导入一个模块，python解析器对模块位置的搜索顺序为：
# # 1、当前目录
# # 2、如果不在当前目录，python则搜索在 shell变量PYTHONPATH下的每个目录
# # 3、如果都找不到，python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
# # 模块搜索路径存储在 system模块的 sys.path变量中。变量里包含当前目录、PYTHONPATH和 由安装过程决定的默认目录
# # 在windows系统，典型的 PYTHONPATH如下：
# # set PYTHONPATH=c:\python27\lib      D:\Softwares\python2\Lib  # 本机的py2位置

# # 3 命名空间和作用域
# # 变量是拥有匹配对象的名字（标识符）。命名空间是一个包含了 变量名称们（键）和它们各自相应的 对象们（值）的字典
# # 一个python表达式可以访问局部命名空间和全局命名空间里的变量
# # 如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量
# # 每个函数都有自己的命名空间。类的方法的作用域规则和 通常函数的一样
# # python会智能地猜测一个变量是局部的还是全局的，它假设任何在 函数内赋值的变量 都是局部的
# # 如果要给 函数内的全局变量赋值，必须使用 global语句
# # global VarName的表达式会告诉python，VarName 是一个全局变量，这样 Python 就不会在局部命名空间里寻找这个变量了

# # 例如，我们在全局命名空间里定义一个变量 Money，
# # 我们再在函数内给变量 Money赋值，然后 python会假定 Money是一个 局部变量，
# # 然而，我们并没有在访问前 声明一个局部变量 Money，结果就是会出现一个 UnboundLocalError的错误，
# # 取消 global语句前的注释符就能解决这个问题
# Money = 2000
# def AddMoney():
#     # 想改正代码就取消以下注释:
#     global Money
#     Money = Money + 1
#
# print Money
# AddMoney()
# print Money

# # 4 函数
# # 4.1 dir()函数
# # dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
# # 返回的列表容纳了在一个模块里定义的所有模块、变量和函数
# import math
# print dir(math)
# # 特殊字符串，变量__name__指向 模块的名字，__file__指向该 模块的导入文件名

# # 4.2 globals()和 locals() 函数
# # 根据调用地方的不同，globals()和 locals()函数可被用来返回 全局和局部命名空间里的名字
# # 如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名
# # 如果在函数内部调用 globals()，返回的是所有在该函数里能访问的 全局名字
# # 两个函数的返回类型都是 字典。所以名字们能用 keys()函数摘取

# # 4.3 reload()函数
# # 当一个模块被导入到一个脚本，模块顶层部分的代码 只会被执行一次
# # 如果你想 重新执行模块里顶层部分的代码，可以用 reload()函数。该函数会重新导入之前导入过的模块
# reload(module_name)
# # module_name要直接放模块的名字，而不是一个字符串形式。比如想重载 hello模块
# reload(hello)

# # 5 python中的包
# # 包是一个分层次的文件目录结构，它定义了一个由模块、子包、和子包下的子包等组成的python的应用环境
# # 简单来说，包就是文件夹，但该文件夹下 必须存在__init__.py文件, 该文件的内容可以为空
# # __init__.py 用于标识当前文件夹是一个包。

# from support import runoob1,runoob2
#
# runoob1()
# runoob2()








