import sys

inputNum = 2

def getdata(e):
    import csv
    with open(e,'r') as f:
        reader = csv.reader(f)
        arr = [list(map(float,row)) for row in reader]
        length = len(arr)
        return arr,length

def transFuncStep(u):
    if u>=0.0:
        return 1.0
    else:
        return 0.0

def calcHidden(e):
    outHidden=[]
    u=0.0
    wh = [[-2.0,3.0,-1.0],[-2.0,1.0,0.5]] #隠れ層の重み [重み1,重み2,バイアス]
    for i in range(len(wh)):
        for j in range(inputNum):
            u+=wh[i][j]*e[j]
        u-=wh[i][len(wh[i])-1]
        out = transFuncStep(u)
        outHidden.append(out)
    return outHidden

def main():
    wo = [-60.0,94.0,-1.0] #出力層の重み
    data = getdata(sys.argv[1])
    e = data[0] #[[0,0],[0,1],[1,0],[1,1]]
    e_num = data[1] #4
    for i in range(e_num):
        print(i,end=" ")
        for j in range(inputNum):
            print(e[i][j],end=" ")
        hiddenOut = calcHidden(e[i])
        print(hiddenOut,end="\n")

if __name__ == "__main__":
    main()
