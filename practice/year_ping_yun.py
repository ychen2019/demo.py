# encoding:utf-8
a = int(raw_input('请输入年份：'))
if a % 4 == 0 and a % 100 != 0:
    print('%d 是普通闰年' %a)
elif a % 400 == 0:
    print('%d 是世纪闰年' %a)
else:
    print('%d 是平年' %a)
