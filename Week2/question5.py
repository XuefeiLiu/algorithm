import numpy as np
def cardGame():
    f= np.zeros((27,27),dtype = np.float)
    for i in range(27):
        f[i,0] = i
    f[0,:] = 0
    for b in range(1,27):
        for r in range(1,27):
            f[b,r] = max(b-r,r/(b+r)*f[b,r-1]+b/(b+r)*f[b-1,r])
    print(f)
    return f[26,26]

print(cardGame())