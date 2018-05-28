def forward(w,e):
    from funcSigmoid import transFuncSigmoid
    INPUT_NUM = 2
    u=0
    for i in range(INPUT_NUM):
        u += e[i] * w[i]
    u -= w[INPUT_NUM]
    o = transFuncSigmoid(u)
    # o = transFuncStep(u)
    return o
