# usr/bin/env python
# -- coding:utf-8 -*-

from getData import getdata
from forwardPropagation import forward
import sys

INPUT_NUM = 2

def main():
    w = [1.0,1.0,1.5]
    data = getdata(sys.argv[1])  #e[0] = [[0, 0], [0, 1], [1, 0], [1, 1]] ,  e[1] = 4
    e = data[0]
    e_num = data[1]
    for i in range(e_num):
        print(i,end=" ")
        for j in range(INPUT_NUM):
            print(e[i][j],end=" ")
        o = forward(w,e[i])  #順伝播
        print(o)

if __name__ == '__main__':
    main()
