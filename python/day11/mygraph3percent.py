import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pymysql

class MyManager:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
        self.curs = self.conn.cursor()
    
    def __del__(self):    
        self.conn.close()

    def getPrices(self,s_name):
        sql = "select s_price,in_time from stock WHERE s_name = '"+s_name+"' order by in_time desc  "
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        prices = []    
        for row in rows :
            prices.append(row[0])
        return prices
    
    def getPricesPer(self,s_name):
        sql = "select s_price,in_time from stock WHERE s_name = '"+s_name+"' order by in_time desc  "
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        prices = []    
        p_init = 0;
        for idx, row in enumerate(rows) :
            if idx == 0:
                p_init = row[0]
            prices.append((row[0]/p_init)*100)
        return prices
    

mm = MyManager()
fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.array([0,0,0,0,0,0])
y = np.array([0,1,2,3,4,5])

z1s = mm.getPricesPer("삼성전자")
z2s = mm.getPricesPer("삼성전자")
z3s = mm.getPricesPer("삼성전자")

print(z1s)
print(z2s)
print(z3s)


z1 = np.array(z1s)
z2 = np.array(z2s)
z3 = np.array(z3s)

ax.plot(x   , y, z1)
ax.plot(x+1 , y, z2)
ax.plot(x+2 , y, z3)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()