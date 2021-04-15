import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from sympy.physics import pring
import pymysql

conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)

curs = conn.cursor() 

sql = "SELECT s_price FROM stock"
curs.execute(sql)

rows = curs.fetchall()

print(rows)

conn.close()

# make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')

# test data
x = np.array([0,0,0,0,0])
y = np.array([0,1,2,3,4])

z1 = np.array([rows])
# z2 = np.array([3,4,5,3,3])
# z3 = np.array([4,5,6,4,4])

# plot test data
ax.plot(z1)
# ax.plot(x+1, y, z1)
# ax.plot(x+2, y, z1)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()