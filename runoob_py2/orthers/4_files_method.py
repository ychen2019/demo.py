# -*- coding=utf-8 -*-
# # 文件（file）方法

# # file对象使用 open函数来创建
# # 1、open() 方法
# # open()方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，
# # 如果该文件无法被打开，会抛出 OSError。
# # 使用open()方法一定要 保证关闭文件对象，即调用 close()方法
# # open()函数常用形式是接收两个参数：文件名(file)和模式(mode)

# # 完整的语法格式为：
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# # file: 必需，文件路径（相对或者绝对路径）。
# # mode: 可选，文件打开模式
# # buffering: 设置缓冲
# # encoding: 一般使用utf8
# # errors:  报错级别
# # newline: 区分换行符
# # closefd: 传入的file参数类型
# # opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符

# # 2、file 对象常用的函数：
# # file.close()   关闭文件。关闭后文件不能再进行读写操作
# # file.flush()   刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入
# # file.fileno()  返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上
# # file.isatty()  如果文件连接到一个终端设备返回 True，否则返回 False
# # file.next()    返回文件下一行
# # file.read([size])  从文件读取指定的字节数，如果未给定或为负则读取所有
# # file.readline([size])  读取整行，包括 "\n" 字符
# # file.readlines([sizeint])   读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力
# # file.seek(offset[, whence]) 设置文件当前位置
# # file.tell()  返回文件当前位置
# # file.truncate([size])  截取文件，截取的字节通过size指定，默认为当前文件位置
# # file.write(str)  将字符串写入文件，返回的是写入的字符长度
# # file.writelines(sequence)  向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符











