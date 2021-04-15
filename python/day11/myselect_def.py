import pymysql

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

if __name__ == '__main__':
    mm = MyManager()
    prices = mm.getPrices("삼성전자")
    print(prices)
    prices = mm.getPrices("삼성전자")
    print(prices)