from flask import Flask
from flask import request
from flask import Flask, render_template
import pymysql


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask!"

@app.route("/param",methods=['GET','POST'])
def param():
    if request.method == "POST":
        name = request.form.get('name',"kimchulsu")
    if request.method == "GET":
        name = request.args.get('name',"kimchulsu")
#     name = request.args.get('name')
#     name ="hahaha"
    return "param="+name
@app.route('/forward.do')
def forward():
    title = "Good Morning"
    return render_template('forward.html',title=title)
   

@app.route('/db.do', methods=['GET'])
def db():
    
    db = pymysql.connect(host='localhost', user='root', passwd='java', db='python', charset='utf8')
    cursor = db.cursor()
    sql = '''SELECT * FROM stock WHERE s_name ="삼성전자"'''
    cursor.execute(sql)
    row = cursor.fetchall()

    
    return render_template('db.html', data=row)

    
if __name__ == "__main__":
    app.run()