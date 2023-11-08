import numpy as np


def AND(x):
    # x=np.array([1,1])
    w = np.array(([0.5, 0.5]))
    b = -0.7
    temp = sum(x * w) + b
    print(str(temp))
    if temp >= 0:
        return 1
    else:
        return 0


# Temp >= 0 ; True
# Temp<0 ; False
def OR(x):
    # x=np.array([1,1])
    w = np.array(([0.5, 0.5]))
    b = -0.5
    temp = sum(x * w) + b
    print(str(temp))
    if temp >= 0:
        return 1
    else:
        return 0


def NAND(x):
    # x=np.array([1,1])
    w = np.array(([-0.5, -0.5]))
    b = 0.9
    temp = sum(x * w) + b
    print(str(temp))
    if temp >= 0:
        return 1
    else:
        return 0

def XOR(x):
    s1=NAND(x)
    s2=OR(x)
    s=np.array([s1,s2])
    temp=AND(s)
    print(temp)

print(XOR())