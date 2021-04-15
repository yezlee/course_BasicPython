import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from sympy.physics import pring
import pymysql
from day11.myselect_def import MyManager

class MyManager:
    def __init__(self):
        self.conn = pymysql.connect(
        user='root', 
        passwd='java', 
        host='localhost', 
        db='python', 
        charset='utf8'
        )
        self.curs = self.conn.cursor()
    def __del__(self):
        self.conn.close()
    def getPrices(self,s_name):
        sql = "SELECT s_price,in_time FROM stock WHERE s_name = '"+s_name+"' order by in_time DESC"
        self.curs.execute(sql)

        rows = self.curs.fetchall()

        prices = []
        for row in rows:
            prices.append(row[0])
        return prices

mm =MyManager()
conn = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)

curs = conn.cursor() 

sql = "SELECT s_price,in_time FROM stock WHERE s_name = '제넥신' order by in_time DESC"
curs.execute(sql)

rows = curs.fetchall()

prices = []
for row in rows:
    prices.append(row[0])

conn.close()

# make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')

# test data
x = np.array([0,0,0,0,0,0])
y = np.array([0,1,2,3,4,5])

mm = MyManager()
z1 = np.array(mm.getPrices("삼성전자"))
z2 = np.array(mm.getPrices("삼성전자"))
z3 = np.array(mm.getPrices("삼성전자"))
# z2 = np.array([3,4,5,3,3])
# z3 = np.array([4,5,6,4,4])

# plot test data
ax.plot(x,y,z1)
ax.plot(x+1, y, z2)
ax.plot(x+2, y, z3)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()