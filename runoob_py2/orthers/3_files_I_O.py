# -*- coding=utf-8 -*-

# # 1、输出 output 打印到屏幕
# # 最简单的输出方法是用 print语句，你可以给它传递零个或多个用逗号隔开的表达式。
# # 此函数把你 传递的表达式转换成一个 字符串表达式

# # 2、输入 input 读取键盘输入
# # python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘
# # 2.1 raw_input函数
# # raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
# str = raw_input("请输入：")
# print "你输入的内容是:",str

# # 2.2 input函数
# # input([prompt]) 函数和 raw_input([prompt]) 函数基本类似
# # 但是input可以接收一个 python表达式作为输入，并将运算结果返回
# str = input("请输入：")
# print "你输入的内容是: ", str
# # 请输入：[x*5 for x in range(2,10,2)]   # 要完整的输入带括号的


# # 3 文件操作
# # python提供了必要的 函数和方法进行默认情况下的文件基本操作
# # 3.1 open函数  打开文件
# # 必须先用python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写
# # 语法：file object = open(file_name [, access_mode][, buffering])
# # 各个参数的细节如下：
# # file_name变量是一个包含了你要访问的 文件名称的字符串值
# # access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# # buffering == 0，就不会有寄存
# # buffering == 1，访问文件时会寄存行
# # buffering > 1 的整数，表明了这就是的寄存区的缓冲大小
# # buffering < 0，寄存区的缓冲大小则为系统默认

# # 3.2 文件对象的属性
# # 一个文件被打开后，你有一个file对象，你可以得到有关该文件的各种信息。
# # 以下是和file对象相关的所有属性的列表：
# # file.closed	如果文件已被关闭，返回true；否则返回false
# # file.mode	返回被打开文件的访问模式
# # file.name	返回文件的名称
# # file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true

# # 创建文件，foo.txt
# fo = open("foo.txt", "w")
# print "文件名: ", fo.name
# print "是否已关闭 : ", fo.closed
# print "访问模式 : ", fo.mode
# print "末尾是否强制加空格 : ", fo.softspace

# # 3.3 close()方法   open是函数，closed是方法
# # file对象的 close（）方法刷新缓冲区里任何 还没写入的信息，并关闭该文件，这之后便 不能再进行写入
# # 当一个文件对象的引用被重新指定给另一个文件时，python 会关闭之前的文件。用close（）方法关闭文件是一个很好的习惯
# fo = open("foo.txt", "w")  # 打开一个文件
# print "文件名: ", fo.name
#
# # 关闭打开的文件
# fo.close()

# # 3.4 write()方法
# # write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字
# # write()方法不会在字符串的结尾添加换行符('\n')
# fo = open("foo.txt", "w")
# fo.write("www.runoob.com!\nVery good site!\n")
# # fo.write("你好\n世界!\n")
# # print open('foo.txt')
# # 关闭已打开的文件
# fo.close()

# # 3.5 read()方法
# # read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，python字符串可以是二进制数据，而不是仅仅是文字
# # 语法：fileObject.read([count])
# # 被传递的参数是要从已打开文件中读取的字节计数,
# #  该方法从文件的开头开始读入，如果没有传入count，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾
# fo = open("foo.txt", "r+")
# # fo.write("www.runoob.com!\nVery good site!\n")
# str = fo.read(10)
# print "读取的字符串是 : ", str
# # 关闭打开的文件
# fo.close()

# # 3.6 文件定位
# # tell()方法，告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后
# # seek（offset [,from]）方法改变当前文件的位置。offset变量表示 要移动的字节数。
# # From变量指定 开始移动字节的参考位置。
# # from == 0，这意味着将文件的开头作为移动字节的参考位置
# # from == 1，则使用当前的位置作为参考位置
# # from == 2，那么该文件的末尾将作为参考位置

# 打开一个文件
# fo = open("foo.txt", "r+")
# fo.write("www.runoob.com!\nVery good site!\n")
# str = fo.read(10)
# print "读取的字符串是 : ", str
#
# # 查找当前位置
# position = fo.tell()
# print "当前文件位置 : ", position
#
# # 把指针再次重新定位到文件开头
# position = fo.seek(0, 1)
# str = fo.read(10)
# print "重新读取字符串 : ", str
# # 关闭打开的文件
# fo.close()

# # 重名命（rename）和删除（remove）必须先导入它，然后才可以调用相关的各种功能
# # 3.7 rename()方法  重命名
# # rename() 方法需要两个参数，当前的文件名和新文件名
# import os
# # 重命名文件test1.txt到test2.txt。
# os.rename("test1.txt", "test2.txt")

# # 3.8 remove()方法  删除
# # 用remove()方法删除文件，需要提供要删除的文件名作为参数
# import os
#
# # 删除一个已经存在的文件test2.txt
# os.remove("foo.txt")

# # 所有文件都包含在各个不同的目录下,不过python也能轻松处理。os模块有许多方法能帮你创建、删除和更改目录
# # 3.9 mkdir()方法  创建新的目录
# # 可以使用os模块的mkdir()方法，在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数
# import os
# # 创建目录test，，在当前目录下创建一个新目录test
# os.mkdir("test")

# # 3.10 getcwd()方法  显示当前的工作目录
# import os
# # 给出当前的目录
# print os.getcwd()

# # 3.11 chdir()方法  改变当前的目录
# # 可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称
# import os
# # 将当前目录改为"/home/newdir"  # !/usr/bin/python
# os.chdir("/home/newdir")   # 这是针对linux系统的操作

# # 3.12 rmdir()方法
# # rmdir()方法删除目录，目录名称以参数传递。
# # 在删除这个目录之前，它的所有内容应该先被清除
# import os
# # 删除”/orthers/test”目录
# os.rmdir("test")





