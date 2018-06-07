def calcHidden(e):
    from transFunction import transFuncStep
    inputNum = 2
    outHidden=[]
    wh = [[-2.0,3.0,-1.0],[-2.0,1.0,0.5]] #隠れ層の重み [重み1,重み2,バイアス]
    for i in range(len(wh)):
        u=0.0
        for j in range(inputNum):
            u+=wh[i][j]*e[j]
        u-=wh[i][len(wh[i])-1]
        out = transFuncStep(u)
        outHidden.append(out)
    return outHidden
