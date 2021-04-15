import numpy as np

a = [1,2,3,4,5,6,7,8]
print(a)

b = np.reshape(a,(2,4))
b = b+1
print(b)

c = [
        [1,2,3,4],
        [5,6,7,8]
    ]
print(c[1][2])
print(b[1,2])