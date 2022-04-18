# -*- coding=utf-8 -*-

def maopao(list):
    n = len(list)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

if __name__ == '__main__':
    list = [1,6,5,3,8]
    maopao(list)
    print(list)




