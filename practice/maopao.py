# -*- coding=utf-8 -*-
# 冒泡排序
def maopao(list1):
    n = len(list1)
    for i in range(n - 1):
        flag = 0
        for j in range(n - 1 - i):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
                flag = 1
        if flag == 0:
            break

if __name__ == '__main__':
    list1 = [1, 5, 8, 6, 4]
    maopao(list1)
    print(list1)
