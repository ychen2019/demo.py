# -*- coding:utf-8 -*—

# 互不相同且无重复数字的三位数，排列方式
# # python的100实例之1
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i, j, k)
                print '------'




# 企业发放的奖金根据利润提成
# # python的100实例之2
# i = int(raw_input("净利润为："))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for cus in range(0, 6):
#     if i > arr[cus]:
#         r += (i-arr[cus])*rat[cus]
#         print (i-arr[cus])*rat[cus]
#         i = arr[cus]
# print r

# x + 100 = n2, x + 100 + 168 = m2,求x
# # python的100实例之3
# for i in range(1,85):
#     if 168 % i == 0:
#         j = 168 / i
#         if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
#             m = (i + j)/2
#             n = (i - j)/2
#             x = n * n - 100
#             print x


# 判断这一天是这一年的第几天
# # python的100实例之4
# year = int(input('年份：'))
# month = int(input('月份：'))
#
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 < month <= 12:
#     sum = months[month - 1]
# else:
#     print '月份不对，月份的范围为1~12'
#     exit()
#
# day = int(input('日期：'))
# if month in [1, 3, 5, 7, 8, 10, 12] and day < 1 or day > 31:
#     print '日期范围为1~31'
#     exit()
# if month in [4, 6, 9, 11] and day < 1 or day > 30:
#     print '日期范围为1~30'
#     exit()
# if month == 2 and day < 1 or day > 29 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
#     print '闰年2月，日期范围为1~29'
#     exit()
# if month == 2 and day < 1 or day > 28 and (year % 4 != 0 or (year % 4 == 0 and year % 100 == 0)):
#     print '平年2月，日期范围为1~28'
#     exit()
#
# sum += day
# if month > 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
#     sum += 1
# print '这是%d年的第 %d 天' % (year, sum)


# # python的100实例之5
# list = []
# for i in range(0,3):
#     x = raw_input('int:')
#     list.append(x)
# list.sort()
# print list


# # python的100实例之6
# # 方法一：
# def fib(n):
#     a,b = 1,1
#     for i in range(0,n-1):
#         a,b = b,a+b
#     return a
# print fib(10)

# # 方法二：
# def fib(n):
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [1,1]
#     fibs = [1,1]
#     for i in range(2,n):
#         fibs.append(fibs[-1]+fibs[-2])
#     return fibs
#
# x = int(input('正整数：'))
# print fib(x)

# 将一个列表的数据复制到另一个列表中
# # python的100实例之7
# a = [1,2,3]
# b = a[:]
# print b


# 输出 9*9 乘法口诀表
# # python的100实例之8
# for i in range(1,10):
#     print
#     for j in range(1,i+1):
#         print '%dx%d=%d'%(i,j,i*j),


# 暂停一秒输出
# python的100实例之9
# import time
#
# myDic = {1:'a',2:'b'}
# for key,value in dict.items(myDic):
#     print key,value
#     time.sleep(1)

# 暂停一秒输出，并格式化当前时间
# python的100实例之10
# import time
#
# print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# time.sleep(1)
# print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

