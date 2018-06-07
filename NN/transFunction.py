def transFuncStep(u):
    if u>=0.0:
        return 1.0
    else:
        return 0.0

def transFuncSigmoid(u):
    import math
    return 1/(1+math.exp(-u))
