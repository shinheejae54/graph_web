import os
from flask import Flask, render_template,request
from server import columns,food_value,name,year

app = Flask(__name__)



@app.route('/')
def start():
    return render_template('main.html')
#main.html과 연결 시킴 첫번째 페이지 
@app.route('/servise/',methods=['POST','GET'])
#버튼을 활용하기 위해서 post를 메소드로 받음 
def servise():
    if request.method == 'POST':
        return render_template('servise.html',columns=columns,food_value=food_value)
# server.py에서 변수를 받은 것을 전달해줌 
@app.route('/graph/',methods=['POST','GET'])
def graph():
    if request.method == 'POST':
        return render_template('graph.html',name1=list(name[0][2:]),
        name2=list(name[1][2:]),name3=list(name[7][2:]),name4=list(name[8][2:]),
        name5=list(name[9][2:]),year=year)
# server.py에서 변수를 받은 것을 전달해줌 

app.run(debug=True)