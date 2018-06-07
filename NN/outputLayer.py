def calcOutput(hiddenOut):
    from transFunction import transFuncStep
    wo = [-60.0,94.0,-1.0] #出力層の重み
    u=0
    length = len(wo)-1
    for i in range(length):
        u+=wo[i]*hiddenOut[i]
    u-=wo[length]
    return transFuncStep(u)
