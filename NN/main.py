import sys
from getData import getdata
from hiddenLayer import calcHidden
from outputLayer import calcOutput

inputNum = 2

def main():
    data = getdata(sys.argv[1])
    e = data[0] #[[0,0],[0,1],[1,0],[1,1]]
    e_num = data[1] #4
    for i in range(e_num):
        print(i,end=" ")
        for j in range(inputNum):
            print(e[i][j],end=" ")
        hiddenOut = calcHidden(e[i])
        o = calcOutput(hiddenOut)
        print(o)

if __name__ == "__main__":
    main()
